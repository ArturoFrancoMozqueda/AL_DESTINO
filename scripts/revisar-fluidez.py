#!/usr/bin/env python3
"""Analiza un archivo solicitado; señala baja variación, no certifica fluidez."""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


def analyze(args):
    media = args.input.resolve(strict=True)
    if args.output.resolve() == media:
        raise ValueError('El informe no puede sobrescribir el medio de entrada.')
    for command in ('ffmpeg', 'ffprobe'):
        if not shutil.which(command):
            raise RuntimeError(f'Falta {command}; revisión temporal pendiente. No se instala automáticamente.')
    probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                            'format=duration:stream=codec_type,codec_name,width,height,avg_frame_rate,nb_frames',
                            '-of', 'json', str(media)], capture_output=True, text=True, check=True)
    metadata = json.loads(probe.stdout)
    filters = []
    if args.roi:
        x, y, w, h = args.roi
        if min(x, y) < 0 or min(w, h) <= 0 or x+w > 1 or y+h > 1:
            raise ValueError('ROI fuera de la imagen; usar x y ancho, y y alto normalizados.')
        filters.append(f'crop=iw*{w}:ih*{h}:iw*{x}:ih*{y}')
    filters += [f'scale={args.width}:-2', f'freezedetect=n={args.noise}:d={args.min_duration}']
    command = ['ffmpeg', '-hide_banner', '-nostats', '-i', str(media),
               '-vf', ','.join(filters), '-an', '-progress', 'pipe:1', '-f', 'null', '-']
    decoded = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace')
    starts = []
    candidates = []
    for kind, number in re.findall(r'lavfi\.freezedetect\.freeze_(start|duration|end): ([\d.]+)', decoded.stderr):
        if kind == 'start':
            starts.append(float(number))
        elif kind == 'end' and starts:
            start = starts.pop(0)
            candidates.append({'start_seconds': start, 'end_seconds': float(number),
                               'duration_seconds': round(float(number)-start, 6),
                               'classification': 'baja_variacion_por_revisar'})
    for start in starts:
        candidates.append({'start_seconds': start, 'end_seconds': None,
                           'duration_seconds': None, 'classification': 'baja_variacion_hasta_fin_por_revisar'})
    frame_counts = re.findall(r'^frame=(\d+)$', decoded.stdout, re.MULTILINE)
    return {'input': str(media), 'metadata': metadata, 'decode_exit_code': decoded.returncode,
            'decoded_video_frames': int(frame_counts[-1]) if frame_counts else None,
            'parameters': {'noise': args.noise, 'min_duration_seconds': args.min_duration,
                           'analysis_width': args.width, 'roi_xywh': args.roi},
            'candidates': candidates,
            'limitations': ['Detecta baja variación: una toma quieta puede producir un candidato legítimo.',
                            'Un overlay animado puede ocultar una imagen congelada; revisar también una ROI del metraje.',
                            'No descarta bucles cortos, tirones, pérdida de frames ni desincronía.',
                            'Decodificar sin errores y tener hashes distintos no acredita movimiento correcto.',
                            'Contrastar candidatos con original, representación de trabajo y exportación en el mismo tiempo.',
                            'No equivale a reproducción continua con escucha.'],
            'decode_error_tail': decoded.stderr[-2000:] if decoded.returncode else None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path, help='Guardar fuera del área pública si incluye rutas personales.')
    parser.add_argument('--min-duration', type=float, default=.75, help='Umbral de candidato, ajustable al material.')
    parser.add_argument('--noise', default='-45dB')
    parser.add_argument('--width', type=int, default=480)
    parser.add_argument('--roi', nargs=4, type=float, metavar=('X', 'Y', 'W', 'H'))
    args = parser.parse_args()
    if args.min_duration <= 0 or args.width < 64:
        parser.error('Duración positiva y ancho de análisis de al menos 64 px.')
    try:
        result = analyze(args)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
        print(f"{result['decoded_video_frames']} fotogramas decodificados; {len(result['candidates'])} candidatos; revisión visual pendiente.")
        return 0 if result['decode_exit_code'] == 0 else 1
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        parser.exit(2, str(error)+'\n')


if __name__ == '__main__':
    raise SystemExit(main())
