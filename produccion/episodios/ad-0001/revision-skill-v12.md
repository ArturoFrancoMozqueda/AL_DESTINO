# Revisión de la skill horizontal y del piloto · 16 de noviembre de 2026 · BORRADOR

## Petición y alcance

Fuente: Arturo, revisión en esta conversación. Rechaza el acabado de la placa verde con texto blanco contorneado; pide PNG con intención profesional y elegante, con Alan por el Mundo como referente, y autoriza Canva u otra herramienta si hace falta. Reporta congelamiento en el **MP4 descargado** y explica que rodaron acciones desde varias perspectivas para enlazarlas. Arturo precisó posteriormente que ocurre aproximadamente en 2:00. No se presume fallo del renderizador.

Se actualiza el procedimiento horizontal a v1.2 y sus referencias compartidas. Esta entrega prepara recursos estáticos y diagnostica el archivo existente; no modifica el proyecto de Clipo ni produce otro MP4. Los originales, montajes anteriores y recibos se conservan.

## Referencia visual observada

Se consultaron el [sitio oficial de Alan por el Mundo](https://alanxelmundo.com/), su [canal oficial](https://www.youtube.com/@alanxelmundo/videos) y el video [Ya visité el NUEVO MUSEO EGIPCIO 4K, Egipto #10](https://www.youtube.com/watch?v=jh8DZVnYeg8), el 16 de noviembre de 2026. Inspección visual por fotogramas en 20, 45, 95, 125, 185, 245, 260, 305, 365, 425, 485, 605, 725 y 845 segundos; sin escucha ni visionado continuo.

En esas muestras predomina metraje despejado con firma pequeña; en 2:05 aparece un inserto temático de jeroglíficos y «likes» abajo a izquierda. La muestra permite observar escala e integración temática; no demuestra formato PNG, técnica de animación ni una norma para todo el canal. Los recursos nuevos son una propuesta propia con ilustración, recorte y tipografía de AL DESTINO, no una reproducción de aquel inserto. Capturas de consulta privadas: `proyecto-local/alan-ref-*.png` y `alan-ref-contacto.jpg`.

## Propuestas gráficas preparadas

- Tres ilustraciones originales: mapa/ubicación, pan/café y cuaderno/brújula. SVG editables y PNG transparentes 280 × 280; catálogo común con hashes. [Mesa de marca](../../../marca/exportaciones/video-v02/index.html).
- Tres rótulos del episodio: Pátzcuaro, Una mesa para dos y Así lo vivimos un domingo, 1200 × 320, con la fuente Plus Jakarta Sans incorporada al render.
- Mockup de la mesa sobre un fotograma propio de IMG_9124, sin el rótulo viejo. Fuente y PNG en `proyecto-local/graficos-v02/`; el generador es `scripts/generar-graficos-viaje.cjs`.

Verificado: generación, dimensiones/transparencia, catálogo y lectura visual de la mesa y del mockup. Son BORRADOR. Pendientes: gusto de Arturo/Liz, importación, escala en timeline, animación, escucha e inspección de una nueva exportación. Una imagen estática no acredita esos pasos.

## MP4: evidencia y límites

Archivo analizado: `patzcuaro-youtube-borrador-1080p.mp4`, H.264/AAC, 1920 × 1080, 30 fps, 584.066667 s. SHA256 del recibo: `f17db76fc33bbb0b88525f49a5db685f1b2a109b6b985bcd8a9ca4bda0e4a7a9`. El análisis temporal decodificó 17 522 fotogramas de video sin error; **eso no acredita fluidez**.

FFmpeg freezedetect, ancho de análisis 480, duración mínima 0.75 s y ruido −45 dB encontró baja variación en 119.566667–120.366667, 122.3–125.166667 y 125.2–125.966667 s. El script nuevo repitió el análisis con ROI x=.1/y=.15/w=.8/h=.6 y −40 dB, con los mismos tres candidatos. Informes y logs en `proyecto-local/`; no equivalen a tres fallos confirmados y el primero coincide con la localización aproximada de 2:00 comunicada posteriormente por Arturo.

Los candidatos también aparecen en la copia SDR usada de IMG_9105: 4.666016–5.466016 y 45.399349–48.266016, entre otros. La correspondencia usa inicio de copia original 7.8 s; selección original 8–14 en timeline 115.1 s y selección original 52–58 en timeline 121.1 s. Por tanto, estos candidatos no pueden atribuirse exclusivamente al render final. En 45.5–47.9 s de la copia, 72 fotogramas reducidos producen 28 hashes distintos y ninguna repetición idéntica consecutiva: no prueba una congelación idéntica sostenida ni descarta ciclos/tirones.

El original IMG_9105 de la unidad E: no está disponible ahora. La localización comunicada de 2:00 coincide con el primer candidato; falta comparar con ese original y revisar la reproducción temporal con audio. No se ha determinado causa ni corregido el archivo. Se reabre la comprobación temporal del recibo, conservando los resultados válidos de metadata y decodificación anteriores.

## Cambios de perspectiva del coche

El plan existente agrupa IMG_9134 (estacionamiento), IMG_9135 (manija/exterior), IMG_9136 (Liz a través de ventana cerrada) e IMG_9137 (interior/despedida, seleccionado desde 7.1 s). Son candidatos para revisar la intención de continuidad, no una correspondencia ya comprobada. La ventana cerrada no acredita una fase de apertura y el arranque descartado de IMG_9137 debe revisarse antes de concluir que falta la toma complementaria. No se inventa un tiempo de corte sin el material pertinente.

La nueva guía exige localizar fases, mano, estado de puerta, dirección y eje antes de elegir el corte durante el movimiento. Si no corresponden, hacer una elipsis comprensible con material real. Pendiente aplicar y comprobar el enlace en Clipo cuando estén disponibles las tomas necesarias.

## Comprobaciones de mantenimiento

La fuente de las skills permanece en `.agents/skills/`; se generan sus copias personales. La plantilla añade `action_sequences` y `temporal_review`, sin reescribir los planes históricos como si hubieran usado esos procedimientos. Ninguna comprobación documental aprueba el episodio.

Resultados: `validar.py`, 2166 comprobaciones y 0 fallos; `catalogar-recursos.py --check`, 37 recursos vigentes; `sincronizar-skills-edicion.py --check`, tres skills sin diferencias. El script temporal se ejecutó sobre el MP4 y la copia SDR (17 522 y 1504 fotogramas respectivamente), y rechazó usar el propio medio como ruta de informe. Los seis PNG de ilustraciones/rótulos tienen RGBA con alfa de 0 a 255 y márgenes transparentes; se inspeccionaron muestras de bordes de los tres iconos sobre fondos claros u oscuros y el rótulo sobre la toma propia.

El validador adicional `quick_validate.py` de skill-creator se intentó en Python 3.12 y requiere PyYAML, ausente también en Python 3.10. Esa comprobación queda pendiente; no se instalaron herramientas para el mantenimiento documental. La validación propia del repositorio y la sincronización sí se completaron.

## Corrección posterior de gráficos · v1.3

Arturo rechazó también el soporte tipo papel y aportó el video del resort de Alan por el Mundo. La propuesta v02 queda descartada para la dirección vigente, conservando sus archivos históricos. Ver [revisión posterior y recursos sin placa](../../automatizacion/revisiones/2026-11-16-alan-sin-placa.md). Los PNG v03 no se han aplicado a Clipo y el MP4 anterior sigue sin corregirse.
