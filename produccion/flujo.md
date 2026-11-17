# Producción sostenible · BORRADOR

Liz editará y ambos están aprendiendo. Arturo desarrolla Clipo/MCP y el paquete de edición lo utilizará cuando corresponda; la integración con material real sigue pendiente de prueba. Ocho horas semanales conjuntas fuera de salidas son un límite de planificación inicial. Dirección de edición declarada: profesional y elegante, con conversación natural y momentos reales.

## Entrar y guardar según la tarea

El [mapa del proyecto](../proyecto.json) y las skills enlazan las fuentes compartidas. No generar toda la cadena de entregables cuando sólo se pide una pieza.

| Trabajo | Destino al guardar | Reutilizar |
|---|---|---|
| Investigación de lugares | `investigacion/consultas/<id>/` | [Metodología](../investigacion/guias/metodologia.md), informe/fuentes/ideas según [salida](../investigacion/guias/salida.md). |
| Ideas y cartera | `planificacion/consultas/<id>/` | [Idea](../planificacion/plantilla-idea.json) y [cartera](../planificacion/plantilla-cartera.json); enlazar investigación, sin copiarla. |
| Episodio elegido para trabajar | `produccion/episodios/<id>/` | [Metadatos](plantillas/episodio.json), brief y sólo las plantillas necesarias. |
| Resultados propios | `resultados/<id>/` | [Plantilla de resultados](../resultados/plantilla-episodio.json), vinculada al episodio. |
| Recurso de marca reutilizable | Fuente y exportación en `marca/` | [Índice de recursos](../marca/recursos.json); actualizar generador/catálogo, sin duplicarlo por episodio. |

Los directorios de consulta se crean sólo cuando exista una entrega que guardar. Usar un ID estable y buscar antes por concepto/experiencia. Una idea no se convierte en episodio grabado por tener una carpeta. Las fechas tentativas y el estado de experiencia se registran por separado.

## Contrato de episodio

Crear `episodio.json` desde la plantilla y registrar su `episode_id` y ruta en el [catálogo](episodios/catalogo.json). Convención inicial de IDs: `ad-0001`, `ad-0002`…; son identificadores, no fechas ni orden de publicación. Reutilizar el ID en guion, plan, gráficos, derivados y resultados.

- `status`: `borrador`, `en_revision`, `aprobado` o `descartado`. Aprobar requiere persona, fecha, alcance y evidencia de la decisión en `approval`; un comentario positivo no aprueba automáticamente todo.
- `stage`: `idea`, `preparacion`, `captura`, `preedicion`, `revision`, `entrega` o `publicado`. Describe el trabajo; no equivale a aprobación o visita realizada. `experience_status` distingue `por_confirmar`, `planificada` y `realizada` según evidencia.
- `documents`: rutas relativas al directorio del episodio; crear sólo brief/guion/packaging/copy/plan que el encargo necesite. El plan usa [la estructura existente](automatizacion/plantilla-plan-montaje.json).
- `resource_ids`: IDs de `marca/recursos.json`, por ejemplo `motion.logo.horizontal` o `video.componente.precio`. El archivo de marca se referencia; no se copia como nueva fuente del episodio.
- `sources`: afirmación, URL/documento o declaración, fecha de consulta y límites. Separar hecho verificado, preferencia, opinión, hipótesis y propuesta. Los desconocidos son `null`/pendiente, no cero.
- `pending`: duda concreta, momento/elemento afectado y responsable si está definido. No colocar documentos privados ni su contenido como evidencia pública.

Conservar el inventario portable de medios como `medios.json` (ID, nombre, metadata verificada y notas mínimas). Guardar rutas absolutas personales en `rutas.local.json` y planes de ejecución con rutas locales en archivos `*.local.json`, excluidos de Git. En Clipo, los IDs reales se consultan en cada sesión; no se confunden con nuestros IDs editoriales.

## Variantes vertical y horizontal

Usar la [skill vertical](../.agents/skills/al-destino-edicion-vertical/SKILL.md) o la [horizontal](../.agents/skills/al-destino-edicion-horizontal/SKILL.md) según el formato real. Ambas reutilizan la [base común](../.agents/skills/al-destino-edicion/SKILL.md), la marca, el inventario y la cobertura del episodio. Un nombre de plataforma no sustituye esa elección.

Crear sólo las variantes solicitadas. Conservar un `episode_id` y planes/proyectos identificables por `variant_id`; por ejemplo, un plan horizontal existente y un plan vertical derivado cuando se encargue. `source_variant_id` vincula el origen del derivado y `source_coverage_reference` enlaza evidencia de exploración reutilizada. No duplicar el episodio ni reconstruir la revisión de todos los archivos por cada encuadre. Si se usan otros tramos, ampliar su cobertura real.

Cada variante conserva aspecto, dimensiones, duración, selección y tiempos propios de textos, música y otros elementos. Registrar sus documentos en `episodio.json`; el plan anterior puede mantenerse con su nombre. No sobrescribir una orientación para entregar la otra ni asumir que cambiar el tamaño del lienzo produce una adaptación terminada.

## Presupuesto de tiempo propuesto

| Actividad | Horas conjuntas |
|---|---:|
| Elegir idea, investigar y preparar brief/tomas | 1 |
| Descargar, respaldar y seleccionar clips | 1 |
| Montaje de historia | 3 |
| Audio, color y rótulos sencillos | 1 |
| Miniatura, título y descripción | 1 |
| Revisión, publicación manual y registro | 1 |

Total propuesto: 8 h. La salida y grabación se calculan aparte. No es una medición ni promesa; registrar tiempo real. Si se supera, simplificar, agrupar captura o espaciar publicaciones. Los cortos son oportunidades, no una cuota adicional obligatoria.

## Grabación inicial con celulares

Probar micrófonos y escuchar una muestra antes de salir. Elegir una configuración que ambos dispositivos puedan mantener; no inferir capacidades por el nombre del modelo. Mantener orientación horizontal para largos y capturar algunos encuadres verticales útiles. Grabar establecimiento/contexto, acción, detalles, conversación y reflexión final; evitar producir todo en cámara lenta. No necesitan actuar reacciones.

Capturar sonido ambiente y tomas estables. Trípode pendiente, no es requisito para empezar. Conservar originales y separar clips descartados por privacidad. Verificar permiso de grabación si el lugar lo requiere.

## Archivo por episodio

ID estable + fecha + tema. Subcarpetas de captura, selección, proyecto editable y gráficos; exportaciones finales en una carpeta externa según la regla siguiente. Mantener material pesado fuera de Git y guardar aquí el índice/brief. Dos copias antes de borrar del celular. Música y gráficos con fuente/licencia registrada.

### Ubicación de exportaciones finales

Guardar los videos finales fuera del repositorio y de cualquier carpeta de skill, incluida su copia personal instalada. Usar la carpeta externa indicada por el usuario; si no existe una preferencia, usar `Videos/AL_DESTINO/<episodio>/` dentro del perfil del sistema. No crear `exports/`, `renders/` ni salidas de episodios dentro de `.agents/skills/` o de las skills personales. Registrar la ruta absoluta y el recibo en archivos `*.local.json` excluidos de Git; los documentos portables identifican el entregable sin incorporar rutas personales ni exigir que el MP4 exista al clonar el repo.

Los PNG, SVG y animaciones reutilizables de marca conservan sus fuentes y exportaciones en `marca/`, con sus catálogos. Son recursos compartidos para montar videos, distintos de los exports finales de un episodio. Los originales, cachés y muestras privadas conservan sus reglas de archivo y exclusión de Git.

Para aplicar recursos, la skill lee el índice común: logos y ambas animaciones existentes, fuentes, iconos, componentes y especificaciones de motion. Los APNG disponibles y los presets sin render tienen estados distintos. Confirmar transparencia, tipografía, búsqueda por tiempo y exportación al usar un editor; no sustituir los logos porque falte compatibilidad.

## Cierre del trabajo del agente

Entregar lo solicitado con su estado, archivos editables, fuentes y pendientes relevantes. Registrar por separado qué se aplicó, qué se vio en preview, qué se escuchó, qué se exportó y qué se reabrió. Guardar/revisar no publica. Tras cambios en recursos o estructura, regenerar el índice y ejecutar el validador. Mantener el episodio una sola vez y enlazar adaptaciones; no crear otro brief por cada red.

La revisión final comprueba experiencia honesta, datos con contexto, audio inteligible, privacidad, derechos y promesa del título cumplida. Publicar sólo cuando el usuario lo solicite fuera de la generación de borradores.
