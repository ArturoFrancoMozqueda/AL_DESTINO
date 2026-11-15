#!/usr/bin/env python3
"""Indexa fuentes existentes para el agente; no mueve, copia ni aprueba recursos."""
from pathlib import Path
import argparse
import hashlib
import json
import struct

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / 'marca/recursos.json'


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def relative(base, value):
    """Una ruta de catálogo se normaliza dentro del repositorio, nunca fuera."""
    resolved = (ROOT / base / value).resolve()
    return resolved.relative_to(ROOT).as_posix()


def describe_file(path, role):
    file = ROOT / path
    data = file.read_bytes()
    result = {'role': role, 'path': path, 'sha256': hashlib.sha256(data).hexdigest()}
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        width, height = struct.unpack('>II', data[16:24])
        result.update(width=width, height=height, has_alpha=data[25] in (4, 6))
    return result


def build_catalog():
    tokens = read_json('marca/tokens/brand_tokens.json')
    video = read_json('marca/video/v01/catalogo.json')
    motion = read_json('marca/video/v01/motion.json')
    resources = []

    def add(resource_id, title, kind, files, **metadata):
        resources.append({'id': resource_id, 'title': title, 'kind': kind,
                          'status': 'borrador', 'availability': 'archivo_disponible',
                          'files': [describe_file(p, role) for role, p in files], **metadata})

    add('marca.logo.original', 'Logo de referencia intacto', 'logo_reference',
        [('reference', 'marca/assets/logos/logo-original-referencia.png')],
        usage='Referencia de integridad, conservar intacta. Aplicaciones con extracción de trabajo.')
    add('marca.logo.horizontal', 'Logo horizontal', 'logo',
        [('raster_transparent', 'marca/assets/logos/piezas/logo-horizontal-transparente.png'),
         ('raster_arena', 'marca/exportaciones/v05-png/logos/logo-horizontal.png')],
        editability='raster; capas PNG originales disponibles en el catálogo de piezas',
        usage='Identificación/firma; conservar proporciones y píxeles originales.')
    add('marca.logo.circular', 'Logo circular', 'logo',
        [('raster_arena', 'marca/exportaciones/v05-png/logos/avatar-1080.png')],
        editability='raster', usage='Avatar/aplicación circular; no confundir con animación.')
    add('marca.logo.monograma', 'Monograma', 'logo',
        [('raster_arena', 'marca/exportaciones/v05-png/logos/monograma.png')],
        editability='raster', usage='Aplicaciones pequeñas cuando el tagline no se lee.')
    for name, font_file, license_file in [
        ('principal', 'PlusJakartaSans[wght].ttf', 'plusjakartasans-OFL.txt'),
        ('editorial', 'CormorantGaramond[wght].ttf', 'cormorantgaramond-OFL.txt')
    ]:
        add('marca.fuente.' + name, 'Fuente ' + name, 'font',
            [('variable_font', 'marca/assets/fuentes/' + font_file),
             ('license', 'marca/assets/fuentes/' + license_file)],
            usage='Instalar/cargar en el editor y comprobar pesos; consultar manual para su función.')

    for name, folder, filename, poster in [
        ('horizontal', 'logo-al-destino', 'AL-DESTINO-logo-animado.png', 'logo-poster.png'),
        ('circular', 'logo-circular', 'AL-DESTINO-logo-circular-animado.png', 'logo-circular-poster.png')
    ]:
        base = 'marca/motion/' + folder
        details = read_json(base + '/renders/catalogo.json')
        add('motion.logo.' + name, 'Animación del logo ' + name, 'logo_animation',
            [('editable_composition', base + '/index.html'),
             ('animated_png', base + '/renders/' + filename),
             ('poster', base + '/renders/' + poster)],
            catalog=base + '/renders/catalogo.json', sequence_directory=base + '/renders/secuencia-png',
            duration_seconds=details.get('duration_seconds', details.get('duration')),
            fps=details['fps'], audio=False, compatibility='pendiente_de_prueba_en_editor',
            usage='Firma/cierre opcional. Reutilizar la animación por elementos; no imponer intro al gancho.')

    base = 'marca/video/v01'
    for group, prefix in [('icons', 'video.icono.'), ('components', 'video.componente.')]:
        for item in video[group]:
            files = [('svg_source', relative(base, item['source']))]
            if group == 'icons':
                files.extend(('png_' + variant, relative(base, export['file']))
                             for variant, export in item['png'].items())
                metadata = {'editability': 'SVG geométrico; PNG aplanado', 'generator': 'scripts/generar-kit-video.cjs'}
            else:
                files.append(('png_preview', relative(base, item['preview']['file'])))
                metadata = {'fields': item['fields'], 'layers': item['layers'],
                            'motion_id': 'motion.video.' + item['motion_preset'],
                            'editability': item['editability'], 'is_mockup': True,
                            'generator': 'scripts/generar-kit-video.cjs'}
            add(prefix + item['id'], item['title'], 'icon' if group == 'icons' else 'video_component', files, **metadata)
    for preset in motion['presets']:
        add('motion.video.' + preset['id'], 'Movimiento: ' + preset['id'], 'motion_specification',
            [('specification', 'marca/video/v01/motion.json')],
            availability='especificacion_sin_render', selector=preset['id'],
            implementation='pendiente', usage='Valor de ensayo propio; no medido del referente ni validado en Clipo.')

    return {
        'schema_version': '1.0', 'brand': 'AL DESTINO', 'status': 'borrador',
        'updated_at': read_json('proyecto.json')['updated_at'], 'path_base': 'repository_root',
        'brand_version': tokens['version'], 'generated_by': 'scripts/catalogar-recursos.py',
        'rules': 'Índice derivado. Editar la fuente/generador correspondiente; disponibilidad no equivale a aprobación ni compatibilidad.',
        'catalogs': [
            {'id': 'marca.png', 'path': 'marca/exportaciones/v05-png/catalogo.json', 'role': '72 PNG de marca; incluye láminas de referencia y placeholders'},
            {'id': 'marca.piezas-logo', 'path': 'marca/assets/logos/piezas/catalogo.json', 'role': 'Coordenadas y PNG extraídos del logo original'},
            {'id': 'video', 'path': 'marca/video/v01/catalogo.json', 'role': 'Iconos y componentes editables/muestras'},
            {'id': 'motion.logo.horizontal', 'path': 'marca/motion/logo-al-destino/renders/catalogo.json', 'role': 'Animación horizontal existente'},
            {'id': 'motion.logo.circular', 'path': 'marca/motion/logo-circular/renders/catalogo.json', 'role': 'Animación circular existente'}
        ],
        'resources': resources,
        'excluded_by_default': ['marca/archivo/', '**/originales/', 'revelacion-en-bloque-descartada.mp4'],
        'legacy_package': {'path': 'marca/exportaciones/AL-DESTINO-kit-marca.zip',
                           'scope': 'Kit de marca existente. No incluye la nueva skill ni todo el paquete de edición.'}
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Comprueba vigencia sin escribir.')
    args = parser.parse_args()
    result = build_catalog()
    if args.check:
        if not DESTINATION.is_file() or json.loads(DESTINATION.read_text(encoding='utf-8')) != result:
            parser.exit(1, 'Índice de recursos desactualizado: ejecutar scripts/catalogar-recursos.py.\n')
        print(f'Índice vigente: {len(result["resources"])} recursos, sin modificar archivos.')
    else:
        DESTINATION.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
        print(f'Índice creado: {len(result["resources"])} recursos; fuentes originales conservadas.')


if __name__ == '__main__':
    main()
