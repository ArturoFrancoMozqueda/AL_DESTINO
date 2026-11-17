# Intento con vidIQ · Registro histórico · Sin completar

Diagnóstico conservado fuera del paquete activo de edición. No es una instrucción para los montajes futuros.

Fecha: 16 de noviembre de 2026, zona America/Mexico_City.

**Registro histórico del intento con vidIQ.** Después, Arturo pidió otro método y se obtuvo un [complemento visual directo](../../../../.agents/skills/al-destino-edicion-horizontal/references/revision-visual-directa.md), incorporado provisionalmente en v0.3. Los resultados y la v0.2 citados abajo corresponden al cierre del intento inicial. La revisión audiovisual completa sigue sin completarse; no se reemplaza este diagnóstico por el avance visual.

## Resultado y alcance

La revisión audiovisual completa solicitada no pudo iniciarse mediante vidIQ. No se obtuvieron análisis, identificadores de trabajo, imágenes en movimiento ni audio. La skill horizontal permanece en **v0.2 BORRADOR, sin cambios editoriales**. Este documento registra el intento y permite retomarlo sin atribuirle resultados inexistentes.

Se leyeron `AGENTS.md`, visión y perfil, la skill horizontal, su base común, sus [referentes parciales](referentes-previos.md), la [referencia histórica](../../../../.agents/skills/al-destino-edicion/references/referencia-video.md), skill-creator y las instrucciones de análisis y diagnóstico de vidIQ. Los cambios existentes en el repositorio se preservaron.

| Referente | Duración de referencia previa, no verificada de nuevo | Cobertura audiovisual nueva obtenida | Pendiente |
|---|---|---|---|
| H01 · [El Mundo en Pareja — Hard Rock Vallarta](https://www.youtube.com/watch?v=vPsSfW0X_sI) | 38:01 | Ningún tramo; sin resultado de vidIQ | 00:00–38:01, sujeto a confirmar duración; español original frente a doblaje automático |
| H02 · [Viaja Vip — Hard Rock Hotel Vallarta, tour completo](https://www.youtube.com/watch?v=ve0gSCrhuyQ) | 37:27 | Ningún tramo; sin resultado de vidIQ | 00:00–37:27, sujeto a confirmar duración; identificar idioma y pista |

Las ventanas pendientes expresan el alcance solicitado, no tramos procesados. No se hizo un nuevo visionado directo ni escucha crítica. La frecuencia de muestreo, omisiones internas y pista utilizada por vidIQ son desconocidas: no hubo análisis que las declarase.

## Comprobación del servicio

| Operación realizada | Resultado observado |
|---|---|
| `vidiq_video_watch`, una solicitud para H01 | Error MCP `-32001: Unknown tool`, nombre devuelto `vidiq.vidiq_video_watch`; sin `mcpJobId` |
| `vidiq_video_watch`, una solicitud para H02 | Mismo error; sin `mcpJobId` |
| `vidiq_media_file_info`, URL de H01 | Error MCP `-32001: Unknown tool`, nombre devuelto `vidiq.vidiq_media_file_info` |
| Búsqueda de vidIQ en Plugin Management | `installed: true`, `status: ENABLED` |
| `vidiq_jobs_list`, filtro de análisis en curso, límite 5 | Error MCP `-32001: Unknown tool`, nombre devuelto `vidiq.vidiq_jobs_list`; no se obtuvo una lista |
| `vidiq_user_channels` | Error MCP `-32001: Unknown tool`, nombre devuelto `vidiq.vidiq_user_channels`; autorización sin comprobar |

Las herramientas se anuncian en la sesión, pero sus llamadas no se resuelven. Esto no identifica la causa ni demuestra un problema de credenciales, créditos o permisos de YouTube. No hubo un trabajo confirmado que se pudiera esperar o consultar por ID; tampoco se puede afirmar que la cuenta carezca de otros trabajos. No se reenviaron solicitudes de análisis para intentar resolver el error. Las respuestas no incluyeron `_credits.used`; cargos y devoluciones no comprobados.

## Qué se pidió a los análisis

Las dos solicitudes incluyeron el mismo encargo detallado, aplicado a cada URL:

- Procesar el video entero y declarar duración, tramos realmente procesados, acceso a imagen en movimiento y audio real frente a muestreo/ASR, idioma/pista, omisiones y límites. Distinguir español original y doblaje automático en H01.
- Cubrir de inicio a despedida la estructura, progresión de la estancia, presencia de los conductores, opiniones y relación entre lugar, acción, conversación y tomas de apoyo.
- Registrar ventanas completas de cada familia encontrada: transiciones, animaciones, iconos/gráficos, música/sonido y ritmo. Describir escenas conectadas, comportamiento, función y limitaciones; identificar listas parciales.
- Separar movimiento de cámara de efecto de edición, gráficos incrustados de interfaz/anuncios/subtítulos activables, y hechos de propuestas de adaptación.
- Describir entradas, permanencias y salidas de gráficos, posición y escala; analizar voz, ambiente, silencios, puentes, fades y efectos sólo con evidencia audible. No inventar canciones, licencias, BPM, niveles, ducking medido ni rendimiento.
- Responder en español y Markdown; conservar un enfoque profesional y elegante con conversación natural y dos voces, sin imponer la estructura de un hotel a todos los vlogs.

Enviar estas instrucciones no equivale a que vidIQ las haya ejecutado.

## Comparación disponible y límites

Sólo sigue disponible la comparación parcial anterior de [referentes.md](referentes-previos.md). Sus observaciones son registros de la revisión previa, **no observaciones directas nuevas ni resultados de vidIQ**:

| Diferencia provisional | Evidencia histórica puntual | Lo que no permite concluir |
|---|---|---|
| H01 combina vistas del lugar y presencia de pareja antes de la presentación | 00:00/00:05, vistas aéreas; 00:20, pareja caminando; 00:40, pareja a cámara con nombres | Duración de planos, enlaces entre esas imágenes, curvas de animación o mezcla |
| H02 muestra pronto al conductor y desarrolla un recorrido explicado | 00:05–00:30 contiene puntos muestreados del conductor; 03:00, demostración de habitación; 05:00, restaurante | Una toma continua de 25 segundos, velocidad de cortes o calidad de los puentes |
| Ambos incluyen recursos informativos distintos | H01 01:30, mapa; H02 15:00, imagen insertada sobre fondo con conductor | Entrada, permanencia, salida o sonido de esos recursos |
| El registro previo incluye conversación final en H01 y pantalla final en H02 | H01 35:00/37:00; H02 37:20 | Desarrollo completo de las conclusiones, despedida o duración de pantalla final |

Cada tiempo anterior es una posición histórica muestreada; el intervalo 00:05–00:30 no es una ventana audiovisual revisada. No hay inventario nuevo de transiciones, animaciones, iconos, música o ritmo. Tampoco existe base nueva para conservar, matizar o sustituir las propuestas previas por hallazgos de una revisión profunda. No se propusieron aplicaciones gráficas nuevas ni se cambiaron recursos de marca.

## Reanudación necesaria

Hace falta restablecer la resolución de las herramientas de vidIQ en el cliente. Sus instrucciones de diagnóstico contemplan recargar o reconectar y comprobar la lista vigente; esto es un siguiente paso de diagnóstico, no una solución comprobada. No se desinstaló el plugin ni se cambió su autorización.

Al retomar:

1. Confirmar una respuesta válida de una consulta gratuita de vidIQ. Si aparece una petición de autenticación real, resolverla mediante el flujo del cliente; no suponerla por este error.
2. Consultar trabajos antes de repetir solicitudes si hay incertidumbre sobre una ejecución anterior. Obtener un ID válido por video y esperar su estado terminal; conservar el resultado, no sólo la confirmación de envío.
3. Evaluar la declaración de cobertura, movimiento, audio y pista original. Si el resultado es muestreado, parcial o no acredita audio real, mantener esas carencias pendientes y no denominarlo revisión completa.
4. Contrastar secuencias continuas cuando las herramientas lo permitan. Registrar por recurso URL, inicio/fin, comportamiento visual/sonoro, función, procedencia y límites; separar adaptación a AL DESTINO. Una captura sólo confirma una imagen estática.
5. Sólo después de satisfacer y evaluar la revisión, revisar las propuestas anteriores, actualizar la skill concisa y llevar el detalle a referencias. Mantener BORRADOR y probar las decisiones con material propio sin asumir compatibilidad de Clipo.

## Validación

- Antes de este registro: `py -3 -X utf8 scripts/validar.py` → 2139 comprobaciones; 0 fallos.
- Validador de skill-creator: se intentó `py -3 -X utf8 <skill-creator>/scripts/quick_validate.py .agents/skills/al-destino-edicion-horizontal`; no ejecutó las comprobaciones porque falta `yaml` (PyYAML): `ModuleNotFoundError`. No se instalaron dependencias.
- La validación documental no acredita visionado, escucha ni mejora editorial. El resultado posterior al registro se comunica en la entrega.
