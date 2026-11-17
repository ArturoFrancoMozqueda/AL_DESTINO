---
name: al-destino-edicion-horizontal
description: "Planificar, montar y revisar videos horizontales de AL DESTINO con historia, rótulos animados y capturas reales de lugares en Google Maps e Instagram. Usar para edición horizontal de material real o su plan de montaje, habitualmente para YouTube."
---

# AL DESTINO · Edición horizontal · v1.7 · BORRADOR

Ampliación de rótulos, redes y capturas reales de establecimientos; conserva el procedimiento operativo anterior. Los recursos, su compatibilidad en el editor y cada episodio mantienen revisión independiente.

## Base y alcance

Trabajar desde la raíz del repositorio AL_DESTINO. Leer una vez su base vigente en `.agents/skills/al-destino-edicion/SKILL.md`, también si esta especialización se cargó desde una instalación personal. La base concentra contexto, marca, cobertura de medios, audio/color, ejecución MCP y conservación del episodio; aplicar sus referencias según la tarea.

Usar `produccion/automatizacion/plantilla-plan-montaje.json` para el plan. Realizar las etapas correspondientes al encargo: un plan termina con decisiones trazables; un montaje exige aplicación y revisión. Conservar episodio e inventario compartidos y relacionar las variantes solicitadas.

Destino habitual: YouTube. Si no se especifica otro formato, partir de 16:9 y 1920 × 1080, sujeto a la capacidad real del editor. Respetar otro destino o formato explícito.

## Duración según material e historia

Explorar todo el material del encargo antes de fijar duración. Armar primero la historia con contexto, intención, desarrollo de las experiencias, acciones, conversaciones, respuestas y cierre que realmente existan. Cada objetivo planteado encuentra resultado, reflexión o pendiente honesto; no saltar a la conclusión por reducir minutos. El episodio de YouTube debe permitir acompañar y entender la experiencia, no quedarse en un avance de sus mejores imágenes.

Después recortar repeticiones y tiempos sin aporte, conservando momentos sustantivos y su contexto. Fijar `output.duration_target_seconds` a partir de ese primer armado y explicar cualquier compresión importante. Sin material suficiente, dejar la duración pendiente. No usar una cuota por clip ni un objetivo universal de minutos; si el usuario fija un máximo, priorizar dentro de él y señalar qué desarrollo queda fuera.

## Construir la experiencia

La dirección es profesional y elegante, conservando conversación natural, personalidad de pareja y momentos reales.

Elegir una apertura que el episodio desarrolle: lugar y momentos de la pareja antes del contexto a cámara; intención a cámara seguida de la experiencia; o una acción real que plantee la pregunta. Comparar alternativas sólo cuando haya opciones útiles. Evitar repetir el mismo contexto en avance, saludo y primer bloque; el logo es una firma opcional.

Organizar `story_beats` por lo vivido o descubierto, sin seguir automáticamente el orden de archivos ni una lista de instalaciones. Cada bloque precisa qué aporta a la pregunta del episodio, qué momento lo sostiene, qué imagen demuestra lo contado y cómo enlaza con el siguiente.

| Material | Decisión de montaje |
|---|---|
| Explicación o recorrido | Mostrar aquello de lo que hablan y la relación entre espacios antes de acumular detalles. Volver a la persona cuando un gesto, opinión o cambio de intención aporte. |
| Conversación de Arturo y Liz | Conservar quién responde a qué y los matices reales. Ambos pueden participar en imagen o voz; no exigir igualdad de tiempo ni fabricar consenso. |
| Comida o actividad | Mantener elección/preparación, acción y respuesta cuando aporten. Revisar desde antes del bocado hasta el gesto posterior; el apoyo no debe ocultar la reacción sustantiva. |
| Una acción con varios ángulos | Agrupar sus fases antes de recortar repeticiones. Aplicar la guía de continuidad de `montaje.md` de la base y registrar `action_sequences`: comprobar gesto, estado del objeto y dirección para que el cambio de perspectiva continúe la acción. |
| Pausa visual | Usarla para descubrir, reposar un momento o cambiar de entorno. Darle entrada y salida relacionadas con el bloque y retirar imágenes que repitan lo ya entendido. |
| Cierre | Responder o matizar la pregunta con lo mostrado: qué vivió cada uno, límites y consejo que pueden sostener. Separar conclusión, despedida y firma sin prolongarlas por obligación. |

Alternar explicación, demostración, conversación y pausa según su función. La cronología puede agruparse por tema si se entiende el salto; conservar la relación entre situación y reacción. No equiparar ritmo con cortes frecuentes ni elegancia con cámara lenta constante.

## Componer y enlazar

Aprovechar el ancho para relacionar a la pareja con el lugar sin perder gestos, manos o acción. Con fotos o tomas verticales, conservar el aspecto o elegir un reencuadre deliberado; no estirar ni recortar contenido necesario sólo para llenar 16:9.

Aplicar las transiciones de la base según función: corte para continuar, disolución para relacionar imágenes y paso por negro para una elipsis deliberada. Revisar siluetas y horizontes superpuestos. Distinguir movimiento de cámara de efecto de edición.

En los rótulos, presentar categoría y precio sucesivamente si compiten; conservar una zona de lectura estable entre entrada y salida. Para un recuerdo o mapa, elegir inserto o pantalla completa según la lectura y la acción; posponerlo si tapa un gesto necesario. Relacionar las fotografías con el momento vivido y conservar su aspecto. Usar recursos de marca existentes y evitar que datos, subtítulos, firma y CTA compitan.

## Identificar lugares y situarlos

Tomar del prompt el destino y el establecimiento y reutilizar los datos del episodio. Buscar el sitio, abrir su ficha real en Google Maps y preparar una captura con ubicación verificada; buscar también su Instagram oficial y capturar el perfil público. No exigir enlaces al usuario si pueden resolverse mediante búsqueda. Al presentar cada lugar, combinar rótulo de categoría/nombre, mapa y perfil de forma sucesiva. Mostrar estas capturas en la primera mención relevante; repetirlas cuando cambie la ubicación, ayuden a explicar un traslado o aporten información nueva, sin reiterarlas por cada corte. Para un lugar apenas citado, anclar su primera presentación al momento en que el espectador necesite situarlo.

Aplicar [rótulos, redes y mapas](../al-destino-edicion/references/rotulos-mapas.md) para resolver nombre, sucursal, cuenta, captura, presentación y registro. Preguntar con candidatos concretos sólo si queda ambigüedad; mantener ese inserto pendiente y continuar el trabajo independiente. Un pin decorativo o el esquema de demostración no sustituyen la captura real. Distinguir el Instagram del establecimiento de los CTA de AL DESTINO.

Presentar las capturas con acabado de vlog de viajes inspirado en Alan por el Mundo y adaptado a AL DESTINO: entradas ágiles, acercamiento suave, pausa legible y salida coordinada, con SFX breves cuando aporten. Conservar las animaciones de redes valoradas favorablemente por Arturo. Mapa y perfil deben acompañar la conversación y dejar visibles las reacciones; elegir inserto o pantalla completa según lectura. No transformar esta referencia de estilo en una afirmación de que una técnica concreta fue observada o medida.

## Insertar FX e iconos animados

Preparar el kit necesario según `visual.md` de la base: likes, pin, firma original y los rótulos/redes/flechas que aporte la historia. No sustituir esos recursos por ilustraciones de la comida o del lugar. Usar elementos transparentes sin placa, tarjeta ni fondo de papel, con contraste local y prueba del mismo archivo sobre tomas claras, oscuras y con detalle. Una lámina sobre colores de marca no basta. Texto separado y sólo cuando aporte. Conservar la imagen despejada; no imponer decoración a cada bloque. Alan por el Mundo y El Mundo en Pareja aportan funciones observadas que se adaptan a AL DESTINO. Canva o HyperFrames pueden usarse cuando hagan falta; colocar un render existente no exige regenerarlo. Consultar `selection_status` del catálogo para no reintroducir propuestas descartadas. Un preset del editor no sustituye el diseño preparado.

Hacer una pasada de acabado después del montaje narrativo para seleccionar **e insertar** efectos sonoros (SFX), efectos visuales e iconos animados con función editorial. Un acabado solicitado no queda aplicado por enumerar recursos en el plan: deben existir en la timeline y comprobarse. Elegir oportunidades reales, sin una cantidad fija de efectos ni decoración en cada corte.

| Recurso | Aplicación |
|---|---|
| Icono editorial | Likes, pin y afinidad: consultar `video.editorial.*` en el índice común. Distinguir CTA y opinión atribuida; no inventar contadores ni puntuaciones. Importar PNG independiente y comprobar entrada, pausa y salida con las capacidades reales. |
| Rótulo de lugar y redes | Consultar `motion.editorial.lugar` y `motion.editorial.redes.*` y su catálogo. Renderizar con nombre/categoría o cuenta confirmados antes de colocarlos; las muestras son mockups. Mantener texto nítido y quieto durante la lectura; conservar el gráfico entre tomas si sigue identificando el mismo lugar. |
| Capturas de lugar y señalamiento | Usar capturas reales de Google Maps e Instagram según la referencia compartida. `motion.editorial.mapa` es una plantilla con demo esquemática, no una captura lista de la visita; comprobar sus límites antes de personalizarla. `motion.editorial.flecha-curva` / `motion.editorial.flecha-bucle` señalan algo visible mediante revelado de trazo. Una flecha sobre metraje no representa una ruta geográfica. |
| Firma de AL DESTINO | Reutilizar `marca.logo.horizontal`, `marca.logo.monograma-video` o las animaciones `motion.logo.horizontal.premium` / `motion.logo.monograma.premium` según legibilidad y función. Conservar dibujo y colores; colocar como firma contenida sin imponer una intro. |
| SFX | Acento breve para una aparición gráfica, cambio de bloque o énfasis que aporte. Elegir del catálogo real o un archivo con licencia; colocarlo en su pista, sincronizarlo con el evento y ajustar por escucha sin tapar voces ni simular acciones que no ocurrieron. |
| FX visual | Movimiento o énfasis que dirija la mirada, aclare un detalle o enlace escenas. Aplicarlo al elemento o corte pertinente con intensidad contenida; evitar competir con un movimiento de cámara o perjudicar la lectura. |

Usar `marca/video/v01/motion.json` como intención de movimiento, no como animación ya ejecutada. Distinguir esos presets de los renders disponibles en `motion.editorial.*`; disponibilidad no prueba compatibilidad. Si el editor no revela trazos, usar la exportación transparente ya dibujada cuando sea compatible; adaptar a aparición del icono completo sólo cuando haga falta y registrarlo. No crear otro logo ni colocar muestras con textos de ejemplo.

Registrar en `graphics` y `audio` recurso/archivo, motivo, evento de anclaje, tiempos y elementos reales del editor; indicar adaptaciones o bloqueo concreto. Verificar la animación completa en reproducción y exportación, y los SFX por escucha. Una captura sólo acredita un estado. Si no hay una oportunidad pertinente, dejar brevemente el motivo; no omitir esta pasada por defecto.

## Aplicación y cierre

Ejecutar con la referencia `clipo.md` de la base y las capacidades actuales, sin trasladar IDs o presets de pruebas anteriores. Tras modificar duración u orden, comprobar límites y solapamientos de textos y otras pistas. Al buscar una posición, confirmar que la imagen ya decodificada corresponde al cabezal antes de usar una captura como evidencia.

Aplicar las comprobaciones de historia, sonido, exportación y reapertura de la base según la entrega. Registrar qué se aplicó y verificó, y localizar faltantes por archivo/tiempo. Una sesión sin acceso auditivo puede entregar preedición con escucha pendiente; para declarar resueltos mezcla, sincronía e historia audiovisual hace falta reproducción continua con audio. El procedimiento conservado y esta ampliación no aprueban cada episodio.

Comprobar avance de imagen en el MP4 entregado siguiendo `clipo.md` de la base y registrar `temporal_review`. Decodificar sin errores y revisar capturas no basta para descartar congelamientos. Ante un fallo, contrastar fuente/copia/exportación en el mismo intervalo y probar una corrección corta antes de repetir el render completo; mantener pendiente lo que no se haya resuelto.

## Referentes y mantenimiento

Consultar la [evidencia visual de los referentes](references/revision-visual-directa.md) sólo para contrastar una decisión concreta o estudiar su estilo. La [ampliación de iconos y rótulos](../../../produccion/automatizacion/revisiones/2026-11-16-iconos-horizontal.md) detalla restaurantes, redes, flechas, likes y mapa del video indicado por Arturo. Contienen ventanas y límites de observación; no hace falta cargarlas en cada montaje. La revisión es visual y parcial, sin escucha crítica ni visionado continuo: adaptar funciones, no copiar hoteles, promociones, colores, duraciones o técnicas sonoras no comprobadas.

Mantener la fuente, sincronización y validación según la base común.
