# Aplicar el paquete mediante el MCP de Clipo · BORRADOR

Arturo desarrolla el editor y su MCP. Aquí se describen necesidades editoriales; no construir/modificar ese repositorio para resolver una tarea de contenido. Cuando el usuario pida montar, descubrir las herramientas reales disponibles y comenzar por el estado del editor. No usar los IDs del catálogo gráfico como si fueran IDs de medios o controles.

Leer proyecto, revisión, medios y capacidades actuales. Preparar un proyecto de prueba separado cuando se ensaye una variante; no sobrescribir un montaje del usuario sin que el alcance lo pida. Mantener tabla entre ID editorial, archivo y ID devuelto por el editor. Releer tras una edición del usuario, conflicto o timeout antes de repetir cambios.

Aplicar el plan del episodio conservando cortes, textos, fondos/iconos y audio en elementos editables cuando sea posible. Una entrada `component_id` es una referencia a nuestro diseño, no una operación MCP inventada. Traducir sus capas y comportamiento sólo a capacidades comprobadas. Cuando falte una función, registrar el hueco exacto para Arturo y ofrecer una versión posible; no rediseñar la marca en silencio ni bloquear la definición editorial.

Comprobar fuente real, tamaños, fondos, transparencia, separación de audio, curvas y búsqueda por tiempo. Tras cambiar duración/orden de clips, revisar todos los tiempos de las otras pistas: no asumir ripple. Usar la preview para verificar imagen, reproducción/escucha para sincronía, exportación para entrega y reapertura para persistencia. Publicar/subir contenido requiere la instrucción expresa correspondiente.

Entregar al final qué se aplicó, qué se adaptó y qué quedó pendiente, con tiempos y elementos localizables para Liz. Si no hay MCP conectado, seguir produciendo historia, recursos y plan; informar que no se aplicaron al editor. La inspección del 14 de noviembre está en `produccion/automatizacion/revision-inicial.md`, como antecedente fechado que puede quedar obsoleto.
