# Informe de validación · BORRADOR

Fecha del proyecto: 11 de octubre de 2026, America/Mexico_City.

## Comprobaciones realizadas

- `python3 scripts/validar.py`: 297 comprobaciones, cero fallos antes de añadir este informe. Integridad SHA-256 de originales, enlaces locales propios, JSON, coincidencia manual/tokens/CSS, tamaños/proporciones, SVG con contornos y grupos editables, previews y límites de archivo.
- Validador oficial de skill-creator: las tres skills válidas; nombre, descripción y frontmatter comprobados.
- Navegador Chromium: ocho previews renderizados, fuentes locales/embebidas, edición de texto mediante diálogo, mostrar/ocultar guías, descarga de SVG con tamaño maestro y sin guías; sin desbordamiento horizontal a 390 px.
- Inspección visual: logo heredado frente al vector, escritorio/móvil, tres familias de miniaturas, banner, avatar, vertical y rótulos. Los titulares son la información principal a tamaño pequeño; las etiquetas y tagline no se esperan legibles a cualquier tamaño.
- PNG: logo horizontal, monograma y rótulo con alfa entre 0 y 255, dimensiones correctas.
- Canva: ocho conversiones creadas. Inspección de YT02 confirmó cinco regiones de texto y seis rellenos editables. La conversión alteró el monograma y debe cotejarse; los SVG/PNG locales son la referencia.
- Casos de las skills revisados en `casos.md`: ubicación variable, presupuesto abierto, fechas flexibles, perro, datos antiguos, acceso limitado y carga semanal. Revisión estática y razonada; no evaluación independiente ni investigación en vivo de alojamientos.

## Límites explícitos

Instagram redirigió a login y no se verificaron recortes actuales de TikTok. Las guías verticales son internas. El logo sigue como reconstrucción de trabajo; no maestro aprobado. Las conversiones Canva no se certifican equivalentes al SVG y requieren reemplazar cualquier logo mal interpretado con el asset correcto.

La investigación heredada no se actualizó ni se reejecutaron sus scripts. Las skills investigarán fuentes actuales bajo demanda. No se cotizaron estancias, no se confirmó una reinauguración, no se generó calendario definitivo y no se publicaron videos.

Para reproducir las comprobaciones: ver `../scripts/LEEME.md`. Los originales tienen sus hashes y fechas ZIP en `../contexto/manifiesto-originales.json`.
