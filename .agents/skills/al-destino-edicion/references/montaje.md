# Montaje, sonido y color · BORRADOR

## Elegir fragmentos

Inventariar y explorar los archivos siguiendo [cobertura del material](cobertura.md), incluidos los grandes. Registrar duración, orientación, fps/códec si se pueden leer, audio, contenido, personas reconocidas y exclusiones; distinguir metadata del original y de la copia. La transcripción ayuda a localizar, pero hay que contrastarla con imagen y escucha. No afirmar que una toma está nítida, estable o bien microfonada sólo por metadata.

Priorizar: momento que cambia la historia; conversación con personalidad; demostración de una afirmación; toma que ubica; detalle que completa una acción. Una toma bonita sin relación puede quedar fuera. Guardar entrada/salida en segundos del archivo original y explicar el motivo. No usar una puntuación automática como sustituto del juicio; marcar dudas concretas.

## Construir continuidad

El corte directo es la base propuesta. Cortar donde termina una idea, cambia una acción o se necesita una toma de apoyo. Buscar continuidad de mirada, dirección, posición y sonido. Evitar repetir la misma acción como si hubiera ocurrido dos veces o mezclar platos/habitaciones de forma engañosa. Un plano de apoyo puede cubrir un recorte de voz si mantiene el sentido de esa frase.

J-cut: empieza el audio de la escena siguiente antes de verla. L-cut: la voz/ambiente de la escena anterior continúa sobre otra imagen. Usarlos para unir ideas o conservar presencia humana; no extender música/ambiente que sugiera otra experiencia. Si el editor no permite separar y recortar ese audio, registrar la limitación y usar un corte simple, sin afirmar que se aplicó el puente.

No imponer una toma cada N segundos. En un recorrido visual probar planos breves; en una reacción o explicación dejar respirar la frase. Acortar cuando el plano ya no añade; alargar cuando necesitamos ver, entender, leer o sentir. Cambiar la escala general/medio/detalle por una razón, sin fabricar cobertura.

## Una acción desde varias perspectivas

Antes de descartar comienzos, repeticiones o tomas cortas, buscar grupos que cubren una misma acción: acercarse al coche, tocar la manija, abrir, entrar y continuar desde dentro, por ejemplo. No confundir una repetición preparada para otro ángulo con material redundante. Explorar desde antes del contacto hasta después del movimiento, aunque no haya diálogo reconocido.

Registrar en `action_sequences` los archivos y fases disponibles, los tiempos de origen y el orden narrativo propuesto. Comparar fotogramas alrededor del punto de enlace: mano que actúa, contacto, posición y estado de la puerta/objeto, dirección de movimiento, mirada y eje. Elegir fases equivalentes y cortar durante el movimiento cuando permita percibir una sola acción. Evitar repetir la apertura completa o saltar una fase necesaria; el orden de nombres de archivo no decide el corte.

Probar primero un corte directo con sonido propio continuo o un puente J/L cuando el editor lo permita. Revisarlo a velocidad normal, con audio y fotograma a fotograma en el enlace; registrar los cortes e IDs realmente aplicados. Un cambio de perspectiva no necesita un efecto gráfico. Una disolución no corrige estados incompatibles. Si falta la fase complementaria, buscar otra cobertura real o hacer una elipsis comprensible, sin invertir material ni simular una continuidad que no existe. Distinguir intención de rodaje, correspondencia comprobada y enlace aún pendiente.

## Sonido

Escuchar voz y ambiente antes de elegir música. Identificar saturación, ruido, viento y cambios entre cámaras. Mantener tono y pausas naturales; no prometer restauración de material irrecuperable. Conservar ambiente propio donde ayude a estar en el lugar, y no colocar sonidos de acciones que no ocurrieron.

Música opcional, con archivo y licencia registrados. Elegirla por función de la escena; bajar o retirar bajo conversación. Juzgar ducking y fades por escucha, sin tomar un porcentaje de volumen como nivel comparable entre archivos. Evitar un SFX en cada entrada gráfica; un acento puntual sólo cuando mejora el énfasis. Medir loudness/picos cuando haya herramientas; anotar qué se midió, sin inventar valores. Las metas de entrega se eligen al definir el formato, no se deducen del preset del editor.

Elegir o generar música después de estabilizar el montaje de la historia. Dimensionarla por los tramos donde cumple una función; no generar una pista larga sólo por la duración máxima que se mencionó al empezar. Reutilizar material válido cuando encaje.

### Efectos gratuitos preferidos

Instrucción de Arturo del 16 de noviembre de 2026: usar SFX cuando aporten a la edición, tanto horizontal como vertical, sin pedir autorización de nuevo para cada efecto ni imponer una cuota. Reutilizar primero un archivo ya documentado si encaja; para nuevas búsquedas:

- [Mixkit](https://mixkit.co/free-sound-effects/): primera opción para acentos gráficos, clics y transiciones discretas. Su [licencia de SFX](https://mixkit.co/license/modal/sfxFree/) permite incorporarlos a videos comerciales y personales; no exige atribución. No redistribuir el sonido aislado, en paquetes, herramientas, plantillas o archivos fuente, ni registrarlo como propio en sistemas de gestión de derechos.
- [Freesound](https://freesound.org/): alternativa para sonidos específicos. Filtrar por **CC0** y comprobar esa licencia en la ficha de cada archivo antes de descargar. En este flujo no seleccionar CC BY, CC BY-NC ni Sampling+; no todo Freesound es CC0. Consultar sus [licencias](https://freesound.org/help/faq/#licenses) y [CC0](https://creativecommons.org/publicdomain/zero/1.0/).

Consultar la licencia vigente al seleccionar un recurso. Registrar en `audio` del plan el archivo/ID, autor, URL de la ficha, licencia y URL, fecha de consulta y ruta de su comprobante local, además del evento, tiempos y mezcla. Conservar el audio y comprobante fuera de Git según el flujo de medios; no copiar una biblioteca completa ni convertir sonidos descargados en recursos públicos de marca. Si no puede verificarse la licencia del archivo, elegir otro verificable o dejar ese acento pendiente.

Insertar sólo lo seleccionado en una pista editable y comprobar sincronía y nivel por escucha y en la exportación; si falta acceso auditivo, declarar esa revisión pendiente. Un clic o whoosh puede reforzar un gráfico; no sustituir el ambiente propio ni fabricar una experiencia con stock. Estas fuentes se eligieron para SFX: sus condiciones no autorizan automáticamente música u otros tipos de recurso. Licencias consultadas el 16 de noviembre de 2026; no equivalen a una garantía de ausencia de reclamaciones automáticas.

Subtítulos: corregir nombres, ñ, signos, hablante y sincronía. Hasta dos líneas como punto de partida; segmentar por unidades de sentido. No aplicar karaoke a todas las conversaciones por defecto. No resumir una cita como si fuera transcripción literal. Comprobar que ninguna palabra o rótulo queda fuera del video tras mover cortes.

Desconfiar de repeticiones anómalas o interjecciones producidas en ruido, música o bocados. No convertirlas automáticamente en diálogo ni concluir que un tramo sin palabras reconocidas está en silencio. Revisar otra ventana/contexto con las herramientas disponibles. Si no se resuelve, conservar el audio y anotar la duda con archivo y tiempos de origen/timeline; no inventar la frase ni declarar escucha real a partir del ASR.

## Color y encuadre

Conservar color real del lugar y pieles fieles. Igualar exposición/balance entre cámaras con una referencia de escena; no aplicar beige uniforme. Verificar HDR/SDR y transformaciones disponibles antes de elegir un look; no afirmar que se preservó HDR por conservar la extensión MOV. Corregir encuadre sin perder un gesto o taparlo con datos. No intensificar color de comida/habitación de modo que cambie lo mostrado.

## Calidad de fuente a entrega

Preservar originales sin sobrescribirlos y distinguir original, proxy, copia de calidad y exportación. Trabajar con proxies cuando convenga, pero reconectar el render a originales o a un máster verificado; confirmar qué archivos usó realmente el editor. No exportar desde miniaturas, previews, descargas de menor calidad ni sucesivas versiones comprimidas. Evitar generaciones de recompresión: corregir desde la fuente de mayor calidad disponible.

Comprobar metadata real de fuente, copia y entrega: dimensiones, aspecto, fps/cadencia, códec, profundidad de bits y características de color (rango, primarias, transferencia y matriz cuando existan). Elegir resolución y cadencia según fuentes y destino explícito; documentar escalados, reencuadres, cámara lenta y conversiones de fps. No bajar resolución/fps o profundidad de color por comodidad ni aplicar interpolación, denoise o enfoque agresivo para aparentar detalle conservado. Un original de mayor resolución no se reduce a 1080p por un preset predeterminado; aumentar dimensiones tampoco recupera información. En mezclas de fuentes, registrar qué se adapta sin atribuir a todas la calidad de la mejor cámara.

Preservar HDR y su señalización si forman parte de la entrega; si el destino requiere SDR, comprobar una transformación deliberada, evitando blancos quemados, sombras aplastadas, banding y cambios de piel. Una conversión HDR/SDR o de profundidad no equivale a conservación exacta. Comprobar también que el audio proviene de la fuente de calidad, sin nuevas saturaciones ni conversiones degradantes innecesarias; la modulación editorial prevista no es por sí misma una pérdida.

Antes del lote o render completo con una ruta nueva, exportar una muestra exigente con textura fina, movimiento, pieles y luces/sombras según el material. Comparar los mismos instantes de original, copia y export a tamaño de visualización equivalente y al 100% de píxel para inspeccionar detalle, teniendo en cuenta el encuadre y las transformaciones previstas. Revisar compresión en movimiento además de fotogramas quietos. Repetir la comparación en el archivo final y para cada tipo de fuente o conversión distinto; metadata o bitrate alto no prueban por sí solos calidad conservada.

«Calidad 100%» no se demuestra con el nombre del preset, el tamaño del archivo ni una inspección visual favorable. Para conservación exacta de la señal, comprobar una ruta sin pérdidas con formato de píxel, profundidad, cadencia y color compatibles, y comparar muestras decodificadas equivalentes en tramos sin transformaciones editoriales; el hash del contenedor sólo identifica el archivo. Cortes, gráficos y ajustes deliberados cambian el resultado: documentarlos sin confundirlos con degradación involuntaria. Una codificación con pérdidas puede resultar visualmente fiel, pero no se presenta como idéntica al original. No fijar un bitrate universal ni suponer que cualquier códec/preset es sin pérdidas.

Registrar `quality_review` por archivo de entrega y tipo de fuente: medios realmente usados, metadata comprobada, transformaciones, configuración real, intervalos comparados, método, hallazgos y limitaciones. Mantener `review.source_quality` pendiente o fallido si falta la comparación, hay degradación involuntaria o la capacidad disponible no cumple el requisito. Corregir y validar una muestra antes de repetir el render; no resolver congelamientos bajando calidad silenciosamente. Una alternativa reducida se identifica como propuesta y no satisface por sí sola la exigencia de conservación exacta. Cada nuevo archivo requiere su propia comprobación; no trasladar el estado verificado de una versión anterior.

## Revisión de Liz

Entregar montaje, alternativa de apertura cuando valga la pena y lista de dudas con tiempo exacto. Distinguir hueco real de cobertura de un corte que simplemente puede mejorarse. Comprobar al menos: promesa respondida, voces reconocibles, datos con contexto, recursos legibles, licencia de música, privacidad y medios presentes tras guardar/reabrir. Registrar minutos reales de selección, montaje, gráficos y revisión para ajustar el alcance a las ocho horas conjuntas iniciales.
