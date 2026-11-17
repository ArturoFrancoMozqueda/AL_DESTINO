# Pátzcuaro · revisión aplicada v02 · BORRADOR

16 de noviembre de 2026. Episodio `ad-0001`, variante `horizontal-viaje-completo`. Encargo expreso de Arturo: aplicar los iconos y la animación que le gustaron, corregir el trabón de 2:00 y ordenar las perspectivas del coche. Su valoración del kit no se interpreta como aprobación del episodio.

El [plan vigente](plan-montaje-youtube.json) conserva la historia y los 44 clips del montaje largo. La revisión se aplicó mediante MCP a una copia de Clipo; el proyecto y MP4 anteriores permanecen conservados. Entrega local: MP4 v02 de 1080p `patzcuaro-youtube-v02-1080p.mp4`, en la carpeta externa de videos, 9:44.62. IDs reales, rutas, recibos y hashes: `exportacion-youtube.local.json` y `proyecto-local/revision-v02/`.

## Gráficos aplicados

- Retiradas todas las placas y los iconos antiguos del episodio.
- Pin transparente del kit v04 en 2:18–2:23.5, con «Pátzcuaro · Michoacán» separado.
- Like transparente en 9:27.2–9:32.2 como invitación «¿Te gustó el viaje?», sin contadores ni opiniones inventadas.
- Monograma animado en 0:00.3–0:04.3 y firma horizontal premium en 9:40.3–9:44.3, con alfa y las piezas originales del logo.
- Rótulos en PNG transparentes con Plus Jakarta Sans y Cormorant Garamond locales, sombra localizada y entrada/salida por keyframes. No dependen de un preset tipográfico del editor. El texto se cambia regenerando su PNG; fuente reproducible en `proyecto-local/revision-v02/generar-rotulos.cjs`.

Recursos comunes: [kit editorial v04](../../../marca/video/v04/catalogo.json) y [firma premium](../../../marca/motion/logo-al-destino/premium/renders/catalogo.json). La comprobación en este episodio acredita esta importación/exportación; no garantiza todos los formatos o editores.

## Trabón de 2:00

El fallo previo no era exclusivo del render: el original recuperado de la caché de medios también presenta huecos entre timestamps. Los de 12.455–13.256667 s y 53.208333–56.06 s coinciden con las pausas de la copia SDR y del MP4 previo. No se modifica ni se intenta inventar movimiento en el original.

Se reemplazan los dos cortes de IMG_9105 por 2.2–7.7 s y 57.5–64 s, normalizados por la importación nativa de Clipo a H.264 SDR BT.709. El bloque conserva sus 12 s en la timeline: 1:55.1–2:07.1. Primero se exportó una prueba de 12 s a 1080p; luego el episodio completo. El avance de carretera, conductor y paneo se contrastó por secuencias de imágenes del MP4 final. El detector de baja variación no encontró candidatos en la prueba corta (umbral 0.25 s) ni en el archivo completo (0.75 s); ese resultado se interpreta junto con la comparación visual, no como certificado autónomo.

## Perspectivas del coche

| Timeline | Original | Decisión |
|---|---|---|
| 9:06.35–9:08.8 | IMG_9135, 0.7–3.15 s | Mano a la manija, apertura y entrada de Liz en cuadro. |
| 9:08.8–9:12.4 | IMG_9136, 2.2–5.8 s | Liz sentada, vista desde fuera a través de la ventana cerrada. |
| 9:12.4–9:36.1 | IMG_9137, 5.2–28.9 s | Ventana y espejo desde dentro, paneo hacia la pareja y despedida. |

Se recuperaron 1.9 s útiles del paneo interior que el recorte anterior omitía. Se conservan íntegros los 7.1–28.9 s de la despedida previamente elegida. La ventana sirve de referencia para cambiar de perspectiva. Entre apertura y Liz sentada hay una elipsis: en estas tomas no aparece una apertura interior equivalente que permita un corte continuo del mismo gesto. No se invierte la acción ni se oculta la diferencia mediante disolución. La música de ese bloque se extendió hasta el inicio de la conversación y el cierre se retimó al nuevo final.

## Comprobado y pendiente

Exportación nativa MCP terminal, descarga y SHA-256 local coincidentes. MP4 H.264/AAC de 1920×1080 a 30 fps, SDR BT.709; 17 538 fotogramas y audio completos decodificados sin errores. Muestreo del archivo final en rótulos, pin, like, entrada por piezas y salida del logo, bloque de 2:00 y enlaces del coche. Alfa conservado, sin rectángulos de fondo. Audio medido: −14.8 LUFS integrados, −0.8 dBTP y LRA 19.5 LU; medir no equivale a escuchar.

Proyecto guardado, cambio a otro proyecto y reapertura desde almacenamiento: 44 clips, 8 stickers, 2 overlays, 11 elementos de audio y cero medios ausentes. Quedó abierto en 9:06.35 para revisar el coche.

Pendientes: escucha crítica, sincronía y visionado audiovisual continuo de Arturo/Liz, además de la revisión continua de privacidad antes de publicar. Las comprobaciones de esta revisión no los sustituyen. No se publicó el video.
