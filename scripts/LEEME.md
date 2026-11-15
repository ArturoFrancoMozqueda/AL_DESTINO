# Herramientas de verificación

`python3 scripts/validar.py` usa sólo la biblioteca estándar: integridad, enlaces propios, JSON, tokens, SVG y PNG.

También comprueba rutas del mapa del proyecto, vigencia del índice de recursos, IDs de episodios, referencias a recursos y evidencia de aprobación/publicación. Los archivos locales, cachés y dependencias se excluyen del recorrido. Lee los archivos en UTF-8 explícito para Windows y Linux. Ejecutar en Windows con `py -3 -X utf8 scripts/validar.py`.

`python3 scripts/catalogar-recursos.py` genera `marca/recursos.json` desde los catálogos y archivos actuales, sin mover ni aprobar recursos. `--check` comprueba que el índice está al día sin escribir. Tras exportar gráficos, regenerar el índice y ejecutar la validación. Este índice usa rutas relativas a la raíz y no contiene rutas privadas del equipo.

La comprobación local no necesita Node, navegador ni Clipo. `.github/workflows/validar.yml` prepara el mismo chequeo para Windows/Linux en CI, con permisos de lectura y acciones fijadas por commit. Configuración basada en la documentación oficial de [checkout](https://github.com/actions/checkout) y [setup-python](https://github.com/actions/setup-python), consultada el 14 de noviembre de 2026. El workflow existente de publicación se conserva separado; esta tarea no hace push ni publica.

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
