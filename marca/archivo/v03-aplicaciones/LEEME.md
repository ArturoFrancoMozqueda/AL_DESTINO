# Aplicaciones v0.3 · BORRADOR

Nueva revisión solicitada por Arturo: mantener el logo original y producir aquí, sin Canva. Los diseños v0.2 y conversiones Canva quedaron descartados por su calidad visual; se conservan como historial.

## Archivos

- `index.html`: editor local con cambio de textos y fotos, descarga SVG maestro y PNG ligero.
- `plantillas/`: ocho SVG con fotografía, tipografía, logo y gráficos en capas/grupos independientes.
- `previews/`: PNGs y tablero de revisión.
- `assets/`: fotografías de mockup generadas, referencia original y procedencia/prompts.

El logo se usa desde `logo-referencia-original.png`, copia byte a byte de la composición heredada. Para el monograma se recorta ese mismo raster mediante un viewport SVG: no se redibuja, recolorea ni genera. Algunos PNG transparentes del ZIP tienen artefactos y no se usan como maestros. Los SVG son contenedores editables de composición; el logo dentro sigue siendo raster, no vector nuevo.

Las escenas son ficticias: no son hoteles, panaderías, hogar ni perro reales de Arturo y Liz. Títulos, locaciones y frases de muestra son hipótesis creativas, no testimonios. Sustituir la foto mediante «Cambiar foto» antes de producir una pieza documental.

Las miniaturas SVG son 3840×2160; PNG desde el editor 1280×720 para archivo ligero. Banner 2560×1440; portada 1080×1920; avatar 1080×1080; gráficos de video 1920×1080. El editor permite modificar texto y fotografía, no mover elementos con drag-and-drop. Los SVG permiten cambiar posiciones y tamaños en un editor compatible o mediante cambios del archivo.

La exportación local usa fuentes embebidas y fotografía dentro del SVG. No requiere red, API, Canva ni servidor. Antes de publicar, comprobar recortes de la plataforma y peso de archivo, quitar guías y revisar a tamaño pequeño. El rótulo de video conserva transparencia.
