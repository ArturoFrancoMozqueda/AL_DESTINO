# PNG, motion y organización · BORRADOR

Fecha: 11 de octubre de 2026.

- 72 PNG del sistema exportados por categoría; catálogo con dimensiones y SHA-256. Incluyen 16 piezas del logo y composición transparente, además del original intacto y los recursos de la guía.
- Las piezas se extrajeron del raster original: coordenadas, fuente y método registrados. No son un vector maestro; la separación A/L en el pie compartido y el matte de tinta se identifican como propuestas.
- HyperFrames 0.8.145: `check` pasó con cero errores/advertencias de lint, runtime, layout y motion. Se inspeccionaron poses a 0.35, 0.6, 1.1, 1.6, 2 y 3.15 segundos; prueba visual del final sobre arena en `../marca/motion/logo-al-destino/renders/logo-poster.png`.
- La animación tiene 15 capas PNG con entradas propias. Keyframes registrados en `../marca/motion/logo-al-destino/snapshots/por-elementos/keyframes.json`. No se anima un contenedor de logo como bloque.
- Render HyperFrames: 96 fotogramas PNG RGBA, 1920 × 1080, 30 fps. APNG de 96 fotogramas, 3.2 s, con transparencia y repetición, generado desde la secuencia sin video intermedio.
- Historial de 62 traslados registrado en `../contexto/organizacion-repo.json`. Los originales mantienen rutas y SHA-256. Las revisiones v0.2 y v0.3 se guardan en `marca/archivo/`.
- `python3 scripts/validar.py` comprueba originales, enlaces, snapshots/tokens, catálogo PNG, piezas, secuencia RGBA, APNG y presencia de archivos trasladados.

Estado: BORRADOR. Verificación técnica y visual no equivale a aprobación del usuario. No se ha publicado ni comprado nada. El APNG requiere un visor compatible; se entregan también los fotogramas PNG individuales.

Catálogo comprobado en Chromium: 72 recursos, APNG decodificado a 1920 px y móvil de 390 px sin desbordamiento. Ambos ZIP pasan comprobación de integridad. El APNG suma 3.2 segundos al leer sus 96 duraciones de fotograma.
