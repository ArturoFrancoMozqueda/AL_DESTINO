# Herramientas de verificación

`python3 scripts/validar.py` usa sólo la biblioteca estándar: integridad, enlaces propios, JSON, tokens, SVG y PNG.

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
