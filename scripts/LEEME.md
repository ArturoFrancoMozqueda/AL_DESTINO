# Herramientas de verificación

`python3 scripts/validar.py` usa sólo la biblioteca estándar: integridad, enlaces propios, JSON, tokens, SVG y PNG.

También comprueba rutas del mapa del proyecto, vigencia del índice de recursos, IDs de episodios, referencias a recursos y evidencia de aprobación/publicación. Los archivos locales, cachés y dependencias se excluyen del recorrido. Lee los archivos en UTF-8 explícito para Windows y Linux. Ejecutar en Windows con `py -3 -X utf8 scripts/validar.py`.

`python3 scripts/catalogar-recursos.py` genera `marca/recursos.json` desde los catálogos y archivos actuales, sin mover ni aprobar recursos. `--check` comprueba que el índice está al día sin escribir. Tras exportar gráficos, regenerar el índice y ejecutar la validación. Este índice usa rutas relativas a la raíz y no contiene rutas privadas del equipo.

La comprobación local no necesita Node, navegador ni Clipo. `.github/workflows/validar.yml` prepara el mismo chequeo para Windows/Linux en CI, con permisos de lectura y acciones fijadas por commit. Configuración basada en la documentación oficial de [checkout](https://github.com/actions/checkout) y [setup-python](https://github.com/actions/setup-python), consultada el 14 de noviembre de 2026. El workflow existente de publicación se conserva separado; esta tarea no hace push ni publica.

## Skills de edición

La fuente de `al-destino-edicion`, `al-destino-edicion-horizontal` y `al-destino-edicion-vertical` está en `.agents/skills/`. `python3 scripts/sincronizar-skills-edicion.py --write` genera sus copias personales desde esa fuente; `--check` detecta diferencias sin escribir. Usa Python 3.9 o superior y sólo la biblioteca estándar. El destino es `CODEX_HOME/skills` o `~/.codex/skills`, configurable con `--dest`. En Windows, ejecutar con `py -3 -X utf8`.

El generador conserva enlaces internos y entre skills, adapta los enlaces a recursos del repositorio e identifica la raíz de trabajo en cada copia instalada. No copia la marca ni los episodios. Si aparecen archivos instalados sin fuente, los informa y no modifica el paquete: revisarlos y archivarlos antes de repetir. Tras mantener estas skills, ejecutar el generador, su `--check` y el validador del repositorio; el de skill-creator requiere PyYAML disponible en su entorno, no como dependencia editorial.

La herramienta histórica `node scripts/archivo/exportar-previews-v03.cjs` requiere Playwright y un navegador Chromium disponible. Puede indicarse su ejecutable mediante `AL_DESTINO_BROWSER`; no requiere servidor ni cambia SVGs. Renderiza previews y prueba edición de textos, visibilidad de guías, descarga y ancho móvil. Las rutas del runtime usado en esta sesión no son dependencias obligatorias del proyecto.

La guía vigente se abre en `marca/design-system.html`. Las herramientas de `scripts/archivo/` sirven para revisiones históricas y no generan el sistema vigente.

## Design system v0.5 y logo por piezas

`node scripts/extraer-piezas-logo.cjs` extrae PNG transparentes del raster original y escribe sus coordenadas en `marca/assets/logos/piezas/catalogo.json`. No crea un vector maestro ni reconstruye zonas ocultas. Requiere Playwright y Chromium; acepta `AL_DESTINO_BROWSER`.

`node scripts/exportar-design-system.cjs` exporta los elementos de `marca/guia-detallada.html` en `marca/exportaciones/v05-png/`, agrupados por uso, y genera catálogo HTML/JSON. También incorpora las piezas extraídas del logo cuando existen. Requiere Playwright y Chromium; acepta `AL_DESTINO_BROWSER`. Los PNG son snapshots de borrador, no editores de texto.

En `marca/motion/logo-al-destino/`, con Node y FFmpeg disponibles:

```sh
npx --yes hyperframes@0.8.145 check .
npx --yes hyperframes@0.8.145 preview --background --port 3017
npx --yes hyperframes@0.8.145 render --format png-sequence --output renders/secuencia-png --fps 30 --quality high --workers 2
```

La animación usa 15 capas PNG: A, L, sol, ola, divisor, nueve letras del nombre y tagline. La conversión de fotogramas a PNG animado conserva RGBA y no pasa por un video comprimido. La URL del editor local es `http://localhost:3017/#project/logo-al-destino` mientras el preview siga activo. La composición y los renders son borradores.

Para renderizar y convertir la secuencia directamente a APNG: `bash scripts/renderizar-logo.sh`. Necesita `npx` o `pnpm` y `ffmpeg` en PATH. El proyecto fija HyperFrames 0.8.145 para reproducibilidad.

## Paquete de edición v0.1

`node scripts/generar-kit-video.cjs` genera 16 iconos SVG originales, 48 PNG transparentes en tres colores, seis muestras de componentes SVG/PNG y la [mesa de revisión](../marca/video/v01/index.html). Requiere Playwright/Chromium; acepta `AL_DESTINO_BROWSER`. `NODE_PATH` puede apuntar a un directorio de dependencias ya instalado. No requiere iniciar ni modificar Clipo. Las fuentes de trabajo del kit están definidas en el script: editarlo y volver a exportar para conservar coherencia, en vez de cambiar un SVG generado y sobrescribirlo después.

Se leen las fuentes y los tokens existentes; el catálogo registra hashes, campos y capas. `motion.json` contiene especificaciones propuestas, no animaciones renderizadas. No cambia los logos, sus animaciones ni el catálogo v05-png. En Windows puede verificarse el repo con `py -3 -X utf8 scripts/validar.py`.

## Gráficos de viaje v0.2

`node scripts/generar-graficos-viaje.cjs` genera tres ilustraciones originales SVG y PNG RGBA en `marca/video/v02/` y `marca/exportaciones/video-v02/`. Requiere Playwright/Chromium ya disponibles; acepta `AL_DESTINO_BROWSER` y `NODE_PATH` hacia dependencias instaladas. No necesita modificar Clipo ni instalar otro editor. Editar este generador para conservar fuentes, exportaciones y hashes coherentes.

Incluye tres composiciones de prueba con texto real del episodio ad-0001; las guarda en su `proyecto-local/graficos-v02/`, fuera de Git y del área pública. Si allí existe `fondo-mesa.png`, también reconstruye un mockup estático. Esto no importa, anima ni aplica los elementos al montaje. Después de generar: reconstruir `marca/recursos.json`, comprobarlo con `--check` y ejecutar `validar.py`.

## Recortes sin placa v0.3

`node scripts/preparar-graficos-sin-placa.cjs` conserva dos maestros raster existentes en `marca/video/v03/fuentes/`, copia los PNG a `marca/exportaciones/video-v03/` y reconstruye su catálogo y mesa de transparencia. Requiere Playwright/Chromium ya disponibles; admite `AL_DESTINO_BROWSER` y `NODE_PATH`. No genera imágenes ni llama a una API: la generación original con `image_gen` integrado y sus prompts están en los archivos de procedencia. No cambiar un maestro sin conservar la procedencia y regenerar catálogo, exportación e índice común.

V02 queda como antecedente con soporte de papel descartado para la dirección vigente; no se borra ni se selecciona por defecto. V03 sigue BORRADOR, sin prueba en Clipo. Los recortes generados son ilustraciones: el genérico no demuestra qué consumieron y el pan almendrado deriva de material propio, conservado en privado. Después de preparar, ejecutar `catalogar-recursos.py`, su `--check` y `validar.py`.

## Kit editorial de iconos y firma v0.4.1

`node scripts/generar-kit-iconos-editoriales.cjs` genera SVG propios y 16 PNG RGBA de like, like en énfasis, pin y corazón, incluyendo variante universal con contraste local y claro/oscuro/turquesa. También copia el logo horizontal existente y recorta su monograma con las coordenadas del catálogo de piezas, sin escalar, redibujar ni recolorear. Fuentes en `marca/video/v04/`, salidas en `marca/exportaciones/video-v04/`. Requiere Playwright/Chromium ya disponibles, admite `NODE_PATH` y `AL_DESTINO_BROWSER`. El catálogo conserva tamaños, hashes, procedencia y referencia a las animaciones. También exporta logo y monograma con apoyo de alfa por detrás; las copias originales permanecen intactas.

La mesa tiene fondos para comprobar contraste; los PNG no los incorporan. Estados de icono y especificaciones de movimiento no equivalen a una animación aplicada. Reconstruir `marca/recursos.json` y comprobar catálogo, sincronización de skills y repositorio después de cambios. El script no modifica Clipo ni genera otro logo.

## Candidatos de baja variación en un MP4

`py -3 -X utf8 scripts/revisar-fluidez.py --input RUTA_MP4 --output INFORME.local.json` usa FFmpeg/ffprobe existentes para decodificar video y localizar candidatos temporales. Opciones: `--min-duration 0.75`, `--noise=-45dB`, `--width 480` y `--roi X Y W H` con valores normalizados. La ROI permite excluir overlays que oculten un fondo trabado. No instala herramientas; si faltan, informa el pendiente.

Guardar el informe con rutas personales junto al episodio, fuera de Git. Revisar candidatos contra fuente, copia y exportación con correspondencia temporal: pueden ser tomas legítimamente quietas. La ausencia de candidatos no descarta bucles, tirones o desincronía. No sustituye reproducción con audio ni certifica fluidez; una decodificación correcta tampoco lo hace. Las verificaciones se documentan por separado.


## Firma animada por piezas

`node scripts/generar-logo-premium.cjs` prepara una variante nueva dentro del proyecto existente, usando 15 piezas originales verificadas por hash. Fuente y comandos de render en [la guía de la variante](../marca/motion/logo-al-destino/premium/LEEME.md). Se entrega horizontal y monograma de 4 s, APNG/WebM con alfa y secuencias PNG. HyperFrames del proyecto pasó de 0.8.145 a 0.9.58, con check de ambas composiciones. Los comandos históricos de la guía anterior conservan la versión con que se produjo aquel render.

El validador del repositorio comprueba que la fuente de la nueva firma coincide con el recibo del render, cantidad y tamaños RGBA de los frames y hashes de los archivos. Esto no sustituye evaluar el movimiento ni probar la importación en Clipo. Los fondos de fotogramas propios y la demo de contraste se conservan privados con ad-0001.

## Editorial animado

`node scripts/generar-editorial-premium.cjs` crea las variantes que falten y actualiza catálogo/mesa conservando los HTML y configuraciones existentes. `--catalog-only` refresca sólo el índice y la mesa; `--write` regenera explícitamente las fuentes a partir de sus `config.json`. Fuentes en `marca/motion/editorial-v01/`; ocho variantes y 27 exportaciones en `marca/exportaciones/editorial-v01/`. Los símbolos de redes se conservan localmente con procedencia y licencia; pin y like reutilizan el kit v04. No se modifica el logo ni se incorporan fotogramas privados al paquete.

Cada variante tiene `index.html`, `config.json`, assets locales y proyecto HyperFrames. Para personalizar una pieza sin sobrescribir las demos, usar `node scripts/generar-editorial-premium.cjs --config CONFIG.local.json --out CARPETA_PRIVADA`. El JSON incluye el `id` del catálogo y los campos de esa variante; `is_mockup: false` exige `confirmed: true` y los datos necesarios. Redes requieren cuenta/enlace; lugar requiere nombre/categoría/localidad/fuente/fecha; mapa requiere imagen, dimensiones, atribución, fuente, enlace del lugar y pin verificado con `pin_x`/`pin_y` normalizados sobre esa imagen. La validación exige declaraciones explícitas, pero no sustituye verificar los datos con fuentes y con Arturo si hay ambigüedad. Conservar rutas personales sólo en archivos locales y respetar la ubicación de exportaciones finales del flujo.

`node scripts/renderizar-editorial-premium.cjs` revisa con HyperFrames y renderiza sólo las variantes del catálogo que lo necesiten; `--only lugar` selecciona una y `--force` fuerza su revisión y render. Usa el launcher de la skill HyperFrames instalada en el perfil; se puede indicar `AL_DESTINO_HYPERFRAMES_LAUNCHER`. Requiere Node, FFmpeg/FFprobe y la instalación local de HyperFrames; no usa servicios de pago. Produce secuencia RGBA temporal privada, WebM VP9 lossless con alfa, APNG y poster; las redes añaden símbolo PNG de 512 px. Comprobar con la skill de HyperFrames vigente antes de ejecutar. Las piezas personalizadas externas se revisan/renderizan desde su propio directorio con las herramientas actuales de HyperFrames.

El catálogo retira exportaciones de la selección vigente si cambia la fuente, falta un archivo o diverge su hash. Conservar un archivo antiguo en disco no acredita que corresponda a la fuente nueva. Después de renderizar, reconstruir `marca/recursos.json`, ejecutar `catalogar-recursos.py --check` y `validar.py`. El primer y último fotograma transparentes son intencionales; el PNG fijo permite previsualizar la pieza. Textos y mapa de demostración son mockups; flechas y like son reutilizables. Todos siguen BORRADOR y sin importación comprobada en Clipo.
