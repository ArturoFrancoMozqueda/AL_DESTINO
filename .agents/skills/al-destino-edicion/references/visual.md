# Gráficos, transiciones y movimiento · v0.5 · BORRADOR

Fuente visual: `marca/manual.md` y tokens v0.6. Para el acabado editorial, consultar `marca/video/v04/catalogo.json`: likes, pin de ubicación, corazón y firma con el logo original; PNG en `marca/exportaciones/video-v04/`. V03 conserva ilustraciones opcionales de alimentos, fuera del kit editorial; V02 es antecedente con papel descartado. El índice `marca/recursos.json` enlaza fuentes y exportaciones.

Dirección vigente: profesional y elegante, con fotografía protagonista, jerarquía tipográfica, espacio y acentos medidos. La referencia anterior de [edición](referencia-video.md) se conserva; la preferencia posterior por gráficos sin fondo sustituye la propuesta de placas para estos insertos. Plus Jakarta Sans sigue llevando los datos. Forma, tamaño y timing concretos se comprueban sobre el material y conservan su revisión propia.

## Preparar el acabado gráfico antes del montaje


El acabado se centra en iconos editoriales y firma: likes, ubicación y logo. Una petición de esos elementos no se resuelve creando ilustraciones de comida u objetos de la escena. Preparar primero la familia funcional necesaria y probarla sobre metraje; usar ilustraciones sólo si una necesidad editorial concreta las justifica.

| Función | Recurso y criterio |
|---|---|
| Like | `video.editorial.like` y `video.editorial.like-activo`. Distinguir opinión de una persona y CTA de interacción. Atribuir la opinión; no fabricar un contador ni asumir una escala de puntuación. El estado lleno es una alternativa gráfica, no aprobación de la experiencia. |
| Ubicación | `video.editorial.ubicacion` junto al lugar confirmado, en texto separado. Alinear ópticamente pin y nombre; mantener ambos estables durante la lectura. La punta no demuestra coordenadas ni una ruta exacta. |
| Firma | `marca.logo.horizontal` o `marca.logo.monograma-video` según legibilidad; sus archivos `png_overlay_contrast` incluyen apoyo de alfa para superposición. Conservar proporciones y colores; no redibujar, recolorear ni añadir el disco de una versión circular al logo horizontal. Revisar contraste y espacio libre sobre la toma. Para la animación con contraste local, usar `motion.logo.horizontal.premium` o `motion.logo.monograma.premium`: 4 s, APNG/WebM con alfa. Las versiones anteriores siguen disponibles. No generar otra identidad para resolver el acabado; verificar en el editor el formato elegido antes de declararlo compatible. |
| Afinidad | `video.editorial.corazon` cuando tenga sentido. No sustituye una reacción real ni obliga a añadir un CTA a cada bloque. |

La revisión de iconos v04 incorpora contraste local dentro del PNG: variante `universal` como punto de partida y otras alternativas disponibles. Su legibilidad debe comprobarse sobre fotogramas claros, oscuros y con detalle, al tamaño final, usando el mismo archivo. Una lámina sobre verde o beige no acredita que funcione sobre video. Una línea de apoyo fina y sombra contenida pueden seguir el alfa del recurso, sin convertirse en placa ni borde grueso de sticker. Conservar el raster original del logo en el frente y separar cualquier apoyo de contraste detrás; no confundirlo con recolorear el dibujo. Los fondos de las mesas de revisión no pertenecen a los PNG. Registrar la función (`cta_like`, `opinion`, `ubicacion` o `firma`), el anclaje editorial y los IDs reales al aplicarlos. Entrada, pausa y salida se adaptan a las herramientas disponibles; los estados estáticos no acreditan animación. No animar continuamente el texto o el pin durante su lectura.

Usar PNG recortados, aislados sobre el metraje, con Alan por el Mundo como referencia de intención y diseño propio de AL DESTINO. No añadir tarjeta, franja, papel recortado, disco de soporte ni borde grueso de sticker por defecto. La barra verde y la propuesta de papel fueron rechazadas. Canva u otra herramienta pueden preparar los elementos cuando haga falta; conservar el logo existente.

La toma puede funcionar sin gráfico. No convertir cada bloque en un rótulo ni ilustrar lo que ya se entiende. Elegir un inserto puntual cuando localiza, aclara o aporta un acento pertinente; darle entrada, pausa y salida contenidas. La ausencia de placa no obliga a añadir textos flotantes. Cuando hagan falta, mantener texto y recorte independientes, con palabras mínimas y contraste suficiente. Reubicar, acortar o retirar antes de reconstruir una tarjeta por comodidad. Evitar contornos gruesos; una sombra local y discreta en letras puede ensayarse si la toma la necesita.

Diseñar por función: ubicación, sabor, consejo o atribución. Buscar silueta reconocible, ilustración pertinente y pocos acentos. «Premium» no se resuelve añadiendo serif, dorado, sombra o una placa grande. Al estudiar un referente, observar momentos concretos y registrar qué se vio; no atribuirle formatos PNG, fuentes o técnicas que la imagen no permite comprobar ni copiar su identidad.

Distinguir el gráfico incrustado del contenido y los controles del reproductor: barra de avance, botones de YouTube y sus contadores no son recursos de la edición del creador. Estudiar el elemento que el usuario señaló, sin generalizar desde una firma a toda la identidad del referente.

Antes del lote, preparar una pieza representativa y verla sobre un fotograma propio, a tamaño completo y reducido; usar texto real sólo si corresponde. Ajustar lectura, contraste, proporción y espacio para caras, manos, producto y reacción. Consultar `selection_status` en el catálogo: el kit editorial v04 es una propuesta BORRADOR; las ilustraciones v03 son opcionales; los recursos con papel v02 quedan fuera de la selección vigente. Un archivo disponible no es un estilo aprobado ni un paquete obligatorio.

Exportar PNG RGBA y comprobar transparencia por composición sobre claro, oscuro y metraje: tener canal alfa no descarta una placa opaca o halos. Revisar agujeros interiores y márgenes; el RGB de píxeles con alfa cero no es un fondo visible y algunas vistas lo muestran mal. Conservar maestro, procedencia/prompts cuando se genere, tamaño y hash. Un raster no se declara vector editable. Para alimentos, conservar las características del producto real si el inserto lo identifica; distinguir una ilustración genérica de una derivada del material propio y de una foto exacta. No usar un recorte generado como prueba de una visita.

Preparar el texto en otra capa cuando haga falta. Un texto en PNG sin soporte puede preservar la tipografía si el editor no la reproduce; no obliga a integrar ilustración y texto ni a añadir fondo. Nunca colocar muestras con datos de ejemplo. Elegir el recurso por su resultado sobre el video, no por pertenecer a un catálogo.

Una mesa visual o mockup acredita diseño estático. Después del montaje, comprobar importación, escala, transparencia, movimiento completo y exportación en el editor real; no afirmar esas pruebas por tener un PNG disponible.

## Familia gráfica v01, conservada como referencia

Iconos de línea, extremos redondos, rejilla 32 × 32, trazo 1.8. Las flechas tienen una curvatura suave propia; no simulan un mapa preciso. PNG transparentes en café oscuro, arena y turquesa; SVG fuente con `currentColor`. Emplear café/arena o arena/petróleo para datos pequeños. Terracota/turquesa como detalles, comprobando contraste sobre la toma. No depender de rojo/verde para expresar una opinión.

Un gráfico debe localizar, explicar, atribuir o comparar. Mostrar el mínimo necesario. Mantener un dato protagonista por inserto. Evitar rótulo + subtítulos + valoración + precio simultáneos; desplazar o escalonar según el audio. Los iconos acompañan texto cuando su significado sea ambiguo.

## Componentes v01 de referencia, sin imponer su soporte

| ID | Campos editables deseados | Uso y condición |
|---|---|---|
| `lugar` | nombre, ciudad/categoría, icono | Primera referencia clara al sitio o cambio de lugar. No repetir en cada corte. |
| `precio` | importe, moneda, unidad, fecha y condiciones | Junto a la mención o demostración. No mostrar importe sin qué incluye ni fuente/fecha. |
| `consejo` | título breve, dato, icono | Consejo práctico comprobado; no opinión inventada. |
| `opinion` | autor, criterio, comentario, pulgar opcional | Atribuir a quien lo dijo. Pulgar arriba/abajo = opinión contextual, no nota objetiva ni consenso. |
| `presentacion` | Arturo, Liz, descripción opcional | Primer contexto/conversación; no ocupa la apertura entera. |
| `cierre` | pregunta o mensaje, cuenta opcional | Cierre de la historia; cuenta/URL sólo confirmada. Reutilizar el logo existente si aporta. |

Los SVG de componentes son muestras con capas identificadas y textos de ejemplo editables en su fuente. Los PNG son referencias visuales aplanadas; Clipo debe colocar texto, fondo e icono por separado cuando sus herramientas lo permitan. Mapas/rutas, QR y rótulos de plataforma se diseñarán cuando tengamos el contenido concreto. `redes` es un icono genérico de cámara; no es el logo oficial de Instagram.

## Posición y lectura

Maestro de trabajo propuesto: 1920 × 1080 para el largo. Margen interior inicial 96 px; componente preferente abajo a izquierda, salvo caras, acción o subtítulos. Datos de lectura desde 36 px de la marca; dato protagonista 60–72 px según longitud. Las etiquetas secundarias de los mockups ensayan 28 px: si no se leen en el encuadre real, ampliar o acortar, sin perder datos necesarios. Estos puntos de partida se prueban a escala de teléfono; no son zonas oficiales de todas las plataformas. En vertical, hacer otra composición conforme a los márgenes de trabajo del token, no reducir la horizontal entera.

Duración visible: suficiente para leer a voz natural y volver a mirar la escena. Probar 3–5 s para un rótulo breve y 5–7 s para un precio con condiciones; acortar contenido antes de encoger texto. Entrada/salida son adicionales a la pausa de lectura. Los presets del JSON usan tiempo relativo al comienzo de cada pieza; el plan del episodio fija su tiempo absoluto.

## Movimiento propuesto

| ID | Construcción | Uso |
|---|---|---|
| `aparecer` | Opacidad 0→1 en 180 ms; salida de 140 ms. | Datos secundarios sin llamar demasiado la atención. |
| `deslizar` | Traslado local X de −24→0 px y opacidad 0→1 en 240 ms; salida de 160 ms. | Lugar, consejo, presentación. Mantener texto estable durante la lectura. |
| `enfatizar` | Escala 0.96→1 y opacidad 0→1 en 220 ms, sin rebote ni loop. | Precio o una valoración puntual; no animar cada cifra de la escena. |
| `trazar` | Longitud visible de trazo 0→1 en 360 ms; pausa; fade de 140 ms. | Flecha que señala algo visible. Requiere máscara/revelado real. Si no existe, usar aparición del icono completo y declarar la adaptación. |

Easing creativo deseado de entrada: ease-out; salida: ease-in. La equivalencia depende del editor. No afirmar una curva exacta cuando el MCP sólo expone un easing genérico. Las piezas dentro de un rótulo pueden entrar como conjunto; separación de capas se conserva para futuros ajustes. No animar continuamente elementos de lectura. Presets en `motion.json` son especificaciones, sin render ni validación todavía en Clipo.

## Transiciones entre tomas

| Recurso | Propuesta de uso | Punto de partida |
|---|---|---|
| Corte directo | Cambio de encuadre/acción/idea dentro de la experiencia. | Sin efecto. Elegir el fotograma por continuidad. |
| Puente de audio J/L | Conversación sobre tomas de apoyo o anticipo de la siguiente escena. | Ajustar por frase y ambiente, sin duración fija. |
| Fundido | Elipsis o pausa de paisaje cuando el contraste temporal tenga sentido. | 8–12 fotogramas a 30 fps; ajustar a la toma. |
| Corte por correspondencia | Una forma, gesto o dirección enlaza dos planos existentes. | Alinear la acción. No necesita una transición gráfica. |
| A negro | Cierre de bloque o elipsis explícita. | Breve y deliberado; evitar entre todos los sitios. |

Whips, flashes, glitches y zooms fuertes quedan para propuestas específicas cuando la escena los justifique; no hay obligación de usarlos ni se consideran prohibidos. La alternancia entre planos y la comprensión de la experiencia llevan el ritmo principal.

## Cómo revisar esta versión

Primero juzgar forma de iconos, jerarquía, cantidad de información y voz de los rótulos en la mesa visual. Después probar lectura sobre una toma propia. Finalmente ajustar velocidad/curva con una muestra de movimiento en Clipo. Registrar si el cambio es una preferencia declarada, una hipótesis o un resultado observado. El tablero tipográfico no demuestra integración ni fidelidad de una animación ejecutada.
