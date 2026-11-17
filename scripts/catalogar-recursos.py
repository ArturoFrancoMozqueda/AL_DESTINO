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
         ('raster_arena', 'marca/exportaciones/v05-png/logos/logo-horizontal.png'),
         ('png_overlay_contrast', 'marca/exportaciones/video-v04/logo-horizontal-contraste.png')],
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
                            'generator': 'scripts/generar-kit-video.cjs',
                            'visual_selection': 'Muestra v01; no usar como acabado premium por defecto. Consultar visual.md y preparar el texto real.'}
            add(prefix + item['id'], item['title'], 'icon' if group == 'icons' else 'video_component', files, **metadata)
    for preset in motion['presets']:
        add('motion.video.' + preset['id'], 'Movimiento: ' + preset['id'], 'motion_specification',
            [('specification', 'marca/video/v01/motion.json')],
            availability='especificacion_sin_render', selector=preset['id'],
            implementation='pendiente', usage='Valor de ensayo propio; no medido del referente ni validado en Clipo.')

    travel = read_json('marca/video/v02/catalogo.json')
    for item in travel['items']:
        add('video.ilustracion.' + item['id'], item['title'], 'illustration',
            [('svg_source', relative('marca/video/v02', item['source'])),
             ('png_transparent', relative('marca/video/v02', item['png']))],
            generator=travel['generator'], editability='SVG fuente; PNG transparente independiente',
            selection_status='descartado_para_direccion_vigente',
            compatibility='pendiente_de_prueba_en_editor',
            usage='Antecedente v02 con fondo de papel rechazado por Arturo. Conservar para trazabilidad; no seleccionar como acabado vigente.')

    cutouts = read_json('marca/video/v03/catalogo.json')
    for item in cutouts['items']:
        add('video.ilustracion.' + item['id'], item['title'], 'illustration',
            [('raster_source', relative('marca/video/v03', item['source'])),
             ('png_transparent', relative('marca/video/v03', item['png'])),
             ('provenance', 'marca/video/v03/' + cutouts['provenance'])],
            generator=cutouts['generator'], editability='Maestro raster y prompts; sin capas vectoriales',
            compatibility='pendiente_de_prueba_en_editor', selection_status='ilustracion_opcional_fuera_del_kit_editorial',
            usage=item['usage'] + ' PNG sin fondo; revisar tamaño y oportunidad sobre la toma. BORRADOR.')

    editorial = read_json('marca/video/v04/catalogo.json')
    for item in editorial['items']:
        add('video.editorial.' + item['id'], item['title'], 'editorial_icon',
            [('svg_source', relative('marca/video/v04', item['source']))] +
            [('png_' + variant, relative('marca/video/v04', data['file'])) for variant, data in item['png'].items()],
            generator=editorial['generator'], editability='SVG geométrico propio; PNG transparente por variante',
            compatibility='pendiente_de_prueba_en_editor', selection_status='propuesta_kit_editorial',
            default_variant='universal',
            usage=item['role'] + ' Contraste local incorporado, sin placa. Prueba sobre metraje requerida; no implica movimiento implementado ni aprobación.')
    add('marca.logo.monograma-video', 'Monograma original transparente para video', 'logo',
        [('raster_source', 'marca/assets/logos/piezas/logo-horizontal-transparente.png'),
         ('png_transparent', relative('marca/video/v04', editorial['logos']['monogram']['file'])),
         ('png_overlay_contrast', relative('marca/video/v04', editorial['logos']['monogram_overlay']['file']))],
        generator=editorial['generator'], editability='recorte raster; conserva los píxeles del original',
        catalog='marca/video/v04/catalogo.json', compatibility='pendiente_de_prueba_en_editor',
        usage='Firma pequeña cuando se lea mejor que el logo completo. No recolorear ni deformar; reutilizar animaciones existentes si corresponde.')

    premium_base = 'marca/motion/logo-al-destino/premium'
    premium = read_json(premium_base + '/renders/catalogo.json')
    add('motion.logo.horizontal.premium', 'Firma por piezas con contraste local', 'logo_animation',
        [('editable_composition', premium_base + '/index.html'),
         ('animated_png', premium_base + '/renders/' + premium['animated_png']),
         ('webm_alpha', premium_base + '/renders/' + premium['webm']),
         ('poster', premium_base + '/renders/' + premium['poster'])],
        catalog=premium_base + '/renders/catalogo.json', sequence_directory=premium_base + '/renders/secuencia-png',
        duration_seconds=premium['duration_seconds'], fps=premium['fps'], audio=False,
        compatibility='pendiente_de_prueba_en_editor', generator='scripts/generar-logo-premium.cjs',
        usage='Piezas raster originales con apoyo de alfa detrás; entrada coordinada, pausa y salida transparente. APNG/WebM renderizados y alfa verificado, sin prueba de importación en Clipo. BORRADOR.')
    add('motion.logo.monograma.premium', 'Monograma animado para firma en esquina', 'logo_animation',
        [('editable_composition', premium_base + '/index.html'),
         ('animated_png', premium_base + '/renders/' + premium['monogram']['animated_png']),
         ('webm_alpha', premium_base + '/renders/' + premium['monogram']['webm']),
         ('poster', premium_base + '/renders/' + premium['monogram']['poster'])],
        catalog=premium_base + '/renders/catalogo.json', selector='monogram',
        sequence_directory=premium_base + '/renders/monograma-png', duration_seconds=4, fps=30, audio=False,
        compatibility='pendiente_de_prueba_en_editor',
        usage='Recorte de la misma animación, sin redibujar ni recolorear. Usar cuando el logo completo no se lea en pequeño; BORRADOR con alfa verificado.')

    # Parametric overlays keep example renders distinct from production assets.
    # File paths are resolved from the maintained catalog, never guessed by an agent.
    overlays_base = 'marca/motion/editorial-v01'
    overlays = read_json(overlays_base + '/catalogo.json')
    for item in overlays['items']:
        files = [(entry['role'], relative(overlays_base, entry['file']))
                 for entry in item['source_files'] + item.get('validation_files', [])]
        files.extend((role, relative(overlays_base, export['file']))
                     for role, export in item['exports'].items())
        files.append(('provenance', relative(overlays_base, item['provenance_file'])))
        add('motion.editorial.' + item['id'], item['title'], item['kind'], files,
            generator='scripts/generar-editorial-premium.cjs',
            catalog=overlays_base + '/catalogo.json',
            composition_file=relative(overlays_base, item['composition_file']),
            config_file=relative(overlays_base, item['config_file']),
            editability='Composición HyperFrames y configuración; texto y símbolo separados.',
            is_mockup=item['is_mockup'], fields=item['fields'],
            duration_seconds=item['duration_seconds'], fps=item['fps'],
            render_status=item['render_status'],
            availability='archivo_disponible' if item['render_status']=='render_verificado' else 'especificacion_sin_render',
            compatibility='pendiente_de_prueba_en_editor',
            selection_status='plantilla_con_demostracion' if item['is_mockup'] else 'recurso_editorial_reutilizable',
            usage=('BORRADOR. Configurar y volver a renderizar con datos confirmados; '
                   'los nombres, cuentas y mapa de demostración no se colocan en un episodio.'
                   if item['is_mockup'] else
                   'BORRADOR. Superposición transparente sin placa; elegir por función editorial y probar sobre la toma.'))

    return {
        'schema_version': '1.0', 'brand': 'AL DESTINO', 'status': 'borrador',
        'updated_at': read_json('proyecto.json')['updated_at'], 'path_base': 'repository_root',
        'brand_version': tokens['version'], 'generated_by': 'scripts/catalogar-recursos.py',
        'rules': 'Índice derivado. Editar la fuente/generador correspondiente; disponibilidad no equivale a aprobación ni compatibilidad.',
        'catalogs': [
            {'id': 'marca.png', 'path': 'marca/exportaciones/v05-png/catalogo.json', 'role': '72 PNG de marca; incluye láminas de referencia y placeholders'},
            {'id': 'marca.piezas-logo', 'path': 'marca/assets/logos/piezas/catalogo.json', 'role': 'Coordenadas y PNG extraídos del logo original'},
            {'id': 'video', 'path': 'marca/video/v01/catalogo.json', 'role': 'Iconos y componentes editables/muestras'},
            {'id': 'video.graficos-viaje', 'path': 'marca/video/v02/catalogo.json', 'role': 'Antecedente con fondo de papel descartado para la dirección vigente'},
            {'id': 'video.recortes', 'path': 'marca/video/v03/catalogo.json', 'role': 'PNG recortados sin placa; propuestas BORRADOR'},
            {'id': 'video.editorial', 'path': 'marca/video/v04/catalogo.json', 'role': 'Likes, pin, corazón y firma original; kit editorial BORRADOR'},
            {'id': 'motion.editorial', 'path': overlays_base + '/catalogo.json', 'role': 'Redes, lugares, plantilla de mapa, flechas y like animados; distinguir demos y recursos reutilizables'},
            {'id': 'motion.logo.horizontal.premium', 'path': premium_base + '/renders/catalogo.json', 'role': 'Firma de 4 s en APNG y WebM con transparencia verificada'},
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
