# Validación de la revisión visual v0.3 · BORRADOR

Fecha: 11 de octubre de 2026. Arturo pidió conservar el logo original y producir aquí; descartó la reconstrucción v0.2 y los diseños Canva.

## Resultado

`python3 scripts/validar.py`: 313 comprobaciones, cero fallos. Incluye originales preservados, enlaces, tokens y proporciones, y comparación SHA-256 de la copia del logo original y cada inserción dentro de las ocho aplicaciones.

`node scripts/exportar-previews.cjs`: ocho previews renderizados. Pruebas reales en Chromium de edición de texto, sustitución de fotografía, visibilidad de guías, descarga SVG maestro 3840×2160 y PNG de miniatura 1280×720, y ausencia de desbordamiento móvil a 390 px.

Inspección visual del tablero, miniaturas, banner, avatar, portada vertical y rótulos. El logo se incorpora como raster original sin vectorizarlo ni regenerarlo. El monograma usa un recorte del mismo raster en un viewport SVG. Se conservaron los originales y el historial descartado.

La transparencia del rótulo se comprobó en el PNG exportado. Las escenas de muestra se generaron con la herramienta integrada image_gen: son ficticias y están documentadas con prompts y procedencia en `../marca/archivo/v03-aplicaciones/assets/procedencia.json`. No representan viajes, establecimiento, hogar ni perro reales.

## Límites

No es aprobación visual del usuario ni garantiza desempeño del canal. Las guías verticales requieren comprobar recortes en las aplicaciones antes de publicar. No se verificaron tarifas ni disponibilidad. Las tres skills y el kit editorial permanecen como borradores. Canva ya no forma parte del flujo gráfico recomendado.

El informe anterior se conserva en `informe-v02.md` como historial de pruebas técnicas; dichas pruebas no demostraron la calidad visual de la versión rechazada.
