---
name: al-destino-contenido
description: "Crear y planificar contenido de AL DESTINO desde una idea o experiencia: concepto, brief, guion flexible, copies, títulos, miniaturas y adaptaciones a redes. Usar para trabajo editorial; las búsquedas de lugares y el montaje de video tienen skills específicas."
---

# Contenido de AL DESTINO · BORRADOR

Convertir una idea, notas o material de Arturo y Liz en contenido con una promesa clara, conversación natural y consejos desde lo vivido. La dirección de edición declarada es profesional y elegante; no equivale a formalizar su manera de hablar ni a inventar una experiencia aspiracional.

## Entrar con el contexto justo

Leer [instrucciones](../../../AGENTS.md), [visión](../../../contexto/vision-y-preferencias.md) y [perfil](../../../contexto/perfil.json). El [mapa del proyecto](../../../proyecto.json) indica rutas y fuentes; el [flujo de producción](../../../produccion/flujo.md) define cómo guardar el trabajo. Consultar decisiones ante contradicciones. Reutilizar una idea o episodio existente antes de abrir uno nuevo sobre el mismo concepto.

Si se necesitan datos actuales de lugares, usar la skill local, Airbnb u hoteles de playa según la consulta y su metodología. Para seleccionar/editar grabaciones, usar [al-destino-edicion](../al-destino-edicion/SKILL.md). Las aplicaciones gráficas consultan [manual](../../../marca/manual.md), tokens e [índice común de recursos](../../../marca/recursos.json); no usar las reconstrucciones históricas como logo vigente.

## Trabajar según la petición

| Petición | Resultado útil | Fuente de trabajo existente |
|---|---|---|
| Ideas o cartera | Conceptos distintos, por qué interesan, evidencia/hipótesis y esfuerzo viable. | [Plantilla de idea](../../../planificacion/plantilla-idea.json), [cartera](../../../planificacion/plantilla-cartera.json). |
| Preparar salida | Pregunta central, escenas posibles y datos/tomas pendientes. | [Brief](../../../produccion/plantillas/brief.md), [guion flexible](../../../produccion/plantillas/guion-flexible.md), [tomas](../../../produccion/plantillas/lista-de-tomas.md), [logística](../../../produccion/plantillas/logistica.md). |
| Títulos y miniatura | Variantes con promesa cumplible y fotografía propia identificada. | [Packaging](../../../produccion/plantillas/packaging.md). |
| Copy, descripción o adaptación social | Mensaje adecuado al formato solicitado, fuente de sus afirmaciones y llamada pertinente. | Brief y material de la experiencia; [revisión de publicación](../../../produccion/plantillas/publicacion.md). |
| Aprendizaje editorial | Qué ocurrió, qué se midió y qué probar después. | [Evaluación](../../../produccion/plantillas/evaluacion.md), [resultados](../../../resultados/plantilla-episodio.json). |

No generar todos los formatos por defecto. Elegir lo que se pidió y lo que aporta dentro de las ocho horas conjuntas iniciales. La cartera usa 90 días y detalle de cuatro semanas cuando se solicita planificación; una petición de copy breve no necesita una estrategia completa.

## Criterio editorial

Antes de redactar, identificar experiencia, audiencia tentativa, promesa y material disponible. Separar lo registrado en cámara, lo declarado por Arturo/Liz, lo comprobado en fuentes y las propuestas. Las frases propuestas para grabar no son citas ya dichas. Si sólo hay una idea futura, escribir en futuro/condicional; no describirla como visita realizada.

Conservar voces naturales, opiniones con autor, humor cuando exista y consejos específicos. No atribuir a uno los gustos del otro. No inventar conflicto, reacciones, cifras, tendencias o resultados de audiencia para mejorar un gancho. Describir el atractivo sin superlativos que no podamos sostener. Al adaptar un largo a un corto, conservar el contexto necesario para no cambiar el sentido de una opinión.

Registrar afirmaciones con fuente/fecha y marcar incertidumbre. Para precios, incluir qué comprende y cuándo aplica. Fotos generadas sirven como mockups identificados; no reemplazan fotografías propias de experiencias reales. Respetar límites de privacidad al redactar y elegir escenas.

## Guardar y entregar

El [flujo de producción](../../../produccion/flujo.md) distingue consultas, ideas, episodios y resultados. Crear sólo los archivos útiles para el encargo; no duplicar un proyecto entre carpetas. Mantener estado BORRADOR hasta una decisión expresa. Entregar el contenido, sus pendientes relevantes y rutas de trabajo. La revisión de publicación no publica ni programa. Comprobar cambios con `python3 scripts/validar.py`; en Windows, `py -3 -X utf8 scripts/validar.py`.
