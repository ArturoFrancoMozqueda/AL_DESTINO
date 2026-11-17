# Aplicar el paquete mediante el MCP de Clipo · BORRADOR

## Alcance y estado real

Arturo desarrolla el editor y su MCP. Esta skill consume sus capacidades; una petición de edición no autoriza por sí sola desarrollar Clipo, reinstalarlo o cambiar de transporte. Si ese trabajo ya está autorizado en la conversación, resolver el bloqueo de forma acotada, distinguirlo del avance editorial y volver al montaje. Si se reproduce el mismo fallo sin evidencia nueva, detener esa repetición y revisar la causa antes de otra conversión o exportación completa.

Cuando el usuario pida montar, descubrir las herramientas disponibles y comenzar por el estado del editor, con `clipo_status` si está expuesto. Respetar «sólo MCP»: una CLI es válida si actúa como cliente del protocolo MCP; un comando directo de FFmpeg o Computer Use no se convierte en MCP por editar el mismo proyecto. No ampliar las alternativas autorizadas desde esta skill.

Leer proyecto, revisión, medios y capacidades actuales. Preparar un proyecto de prueba separado cuando se ensaye una variante; no sobrescribir un montaje del usuario sin que el alcance lo pida. Mantener tabla entre ID editorial, archivo y ID devuelto por el editor. Releer tras una edición del usuario, conflicto o timeout antes de repetir cambios.

Leer respuestas de forma compacta: revisión, IDs, duración, estado, errores y campos necesarios. No volcar el proyecto entero, miniaturas, `coverThumb`, data URLs ni Base64 de artefactos en texto. Pedir imágenes o audio sólo para la inspección concreta. Los límites y esquemas pueden cambiar entre versiones del editor y del cliente: comprobar los actuales, sin fijar en la skill un máximo de archivo o un parámetro heredado.

## Cobertura y prueba representativa

Seguir [cobertura del material](cobertura.md) para inventariar todos los archivos pedidos y explorar los tramos pertinentes. Comprobar los momentos obligatorios, especialmente en clips que fallaron al importar. No convertir un límite técnico en una decisión de descartar contenido.

Con medios o representaciones nuevos, probar un fragmento representativo antes del lote: importación real, búsqueda dentro del clip, decodificación, audio y exportación leída de vuelta. Si se pretende exportar mientras el chat está delante, verificar también el avance en segundo plano. Un archivo importado o un trabajo encolado no acredita reproducción ni entrega. Un recorte ordinario puede reutilizar una ruta ya comprobada; no necesita repetir todo el catálogo del MCP.

En HDR, verificar metadata de origen y de la copia; no deducirla de MOV, HEVC o modelo de cámara. Comparar el mismo momento de fuente, preview y muestra exportada, mirando piel, blancos, textura y continuidad con otras tomas. Si una conversión quema blancos o altera el color, corregir y volver a probar la muestra antes de multiplicarla. Una receta que funcionó en un episodio no es un ajuste universal ni una decisión de marca.

## Aplicar y conservar tiempos

Aplicar el plan del episodio conservando cortes, textos, fondos/iconos y audio en elementos editables cuando sea posible. Una entrada `component_id` es una referencia a nuestro diseño, no una operación MCP inventada. Traducir sus capas y comportamiento sólo a capacidades comprobadas. Cuando falte una función, registrar el hueco exacto para Arturo y ofrecer una versión posible; no rediseñar la marca en silencio ni bloquear la definición editorial.

Tras explorar el material y elegir la historia, preparar las copias de calidad sólo para los fragmentos necesarios cuando sea útil, con márgenes para ajustes si corresponden. Registrar corte original, intervalo original convertido, corte dentro de la copia, ID del editor, inicio de timeline y velocidad. Si la copia empieza en cero, no reutilizar como `in` el tiempo absoluto del original. Para palabras reconocidas en origen, situarlas según el recorte y la velocidad, conservando el contexto y cualquier desfase medido de audio. Verificar los límites de cada corte.

Comprobar fuente real, tamaños, fondos, transparencia, separación de audio, curvas y búsqueda por tiempo. Tras cambiar duración/orden de clips, revisar todos los tiempos de las otras pistas: no asumir ripple. Usar la preview para verificar imagen, reproducción/escucha para sincronía, exportación para entrega y reapertura para persistencia. Publicar/subir contenido requiere la instrucción expresa correspondiente.

## Comprobar avance de imagen en la exportación

La decodificación sin errores, duración, hash y capturas aisladas no prueban que la imagen avance: un MP4 válido puede contener fotogramas repetidos, bucles o tirones. Revisar temporalmente cada fragmento usado y sus enlaces en el archivo entregado, además de entradas/salidas gráficas y los tramos con fallos previos. Verificar resolución/fps reales con metadata, independientemente del nombre del preset. Imagen, sincronía, escucha y reapertura son comprobaciones distintas.

Si hay congelamiento reportado, ubicar su tiempo en el MP4 y mapearlo a original, copia de trabajo y timeline. Comparar el mismo intervalo con márgenes a ambos lados. Comprobar la imagen base en una zona con movimiento: un overlay animado puede ocultar una toma trabada. Distinguir una pausa real de cámara, repetición de fotogramas, bucle y retraso del reproductor. Un detector de baja variación sólo produce candidatos; ni una alerta demuestra fallo ni la ausencia de alertas lo descarta.

Cuando las herramientas autorizadas lo permitan, `scripts/revisar-fluidez.py` auxilia la inspección local con FFmpeg/ffprobe existentes, sin instalar dependencias. Guarda metadata, decodificación de video y candidatos con parámetros explícitos; no certifica continuidad ni revisa audio. Usar una región de imagen si hay gráficos y contrastar visualmente los resultados. No imponer sus umbrales a todas las escenas ni convertir análisis externo en una supuesta ejecución MCP.

Corregir la etapa donde se reproduzca el problema y exportar una muestra corta del tramo antes de repetir el render completo. Si falta el original o no se reproduce el fallo, dejar causa y resolución pendientes con evidencia, sin declarar reparado el video. No repetir renders completos sin evidencia nueva ni desarrollar el editor por defecto. Un fallo temporal comunicado reabre esa comprobación aunque el recibo previo indique decodificación correcta.

## Cerrar con evidencia

Esperar el estado terminal de los trabajos e inspeccionar sus errores y recibos. Revisar el archivo exportado en los momentos críticos, incluidos los medios que dieron problemas. Guardar y comprobar una carga desde almacenamiento; abrir el proyecto que ya está abierto puede ser sólo una lectura del estado actual. Dejar el proyecto editable correcto abierto, con un punto de revisión útil.

Entregar al final qué se aplicó, qué se adaptó y qué quedó pendiente, con tiempos y elementos localizables para Liz. Si no hay MCP conectado, seguir produciendo historia, recursos y plan; informar que no se aplicaron al editor. La inspección del 14 de noviembre está en `produccion/automatizacion/revision-inicial.md`, como antecedente fechado que puede quedar obsoleto.
