---
name: al-destino-edicion
description: "Definir la dirección de edición y preparar recursos de AL DESTINO cuando el formato no esté definido. También aporta la base compartida a las skills de montaje horizontal y vertical."
---

# Edición de AL DESTINO · Base común v0.5 · BORRADOR

Preparar la edición de AL DESTINO con conversación natural, momentos reales y acabado profesional y elegante. Los montajes y recursos conservan su estado de revisión; esta guía no los aprueba.

## Elegir formato

- Pieza vertical: [edición vertical](../al-destino-edicion-vertical/SKILL.md).
- Pieza horizontal: [edición horizontal](../al-destino-edicion-horizontal/SKILL.md).
- Ambos formatos: aplicar cada especialización a su variante, compartiendo inventario, cobertura y recursos del episodio.
- Dirección común o formato aún no definido: trabajar desde esta base. Inferir orientación cuando el encargo sea claro y resolverla antes de ejecutar un encuadre que dependa de ella; no deducirla sólo de la plataforma.

Si ya se cargó una especialización, conservarla: leer esta base no inicia otro enrutamiento ni exige el otro formato. Aspecto, duración y plataforma son decisiones distintas.

## Contexto y fuentes

Resolver la raíz de AL_DESTINO desde el encargo o la ubicación de la fuente; una copia instalada indica su repositorio de origen. Leer `AGENTS.md`, `contexto/vision-y-preferencias.md` y `contexto/perfil.json`; consultar `contexto/decisiones.md` ante contradicciones. Las rutas entre comillas invertidas se resuelven desde esa raíz. Marca vigente en `marca/manual.md` y `marca/tokens/brand_tokens.json`.

El [índice común de recursos](../../../marca/recursos.json) une logos, ambas animaciones existentes, fuentes, ilustraciones, iconos, componentes y motion propuesto con IDs estables. La [mesa del kit editorial](../../../marca/exportaciones/video-v04/index.html) contiene likes, ubicación y firma en PNG sin placa; las ilustraciones v03 son opcionales; el [módulo v01](../../../marca/video/v01/index.html) conserva componentes/motion de referencia. Aplicar `visual.md` antes de elegir o preparar rótulos; las muestras con corchetes son mockups. Usar `motion.logo.horizontal`/`motion.logo.circular` para localizar las animaciones originales. No confundir `archivo_disponible` con compatibilidad en Clipo, ni `especificacion_sin_render` con animación implementada. Copiar sólo esta carpeta de skill no incluye los recursos de marca del repositorio.

## Elegir la parte del trabajo

- Contrastar la dirección con el referente declarado: [observaciones parciales y adaptación](references/referencia-video.md). Leer sólo si ayuda a una decisión de estilo; no es un requisito para cada montaje.
- Historia, apertura y estructura: [narrativa y hooks](references/narrativa.md).
- Con material real nuevo, inventario completo, exploración de clips grandes y selección por historia: [cobertura y selección](references/cobertura.md).
- Selección, ritmo, continuidad, sonido y color: [montaje](references/montaje.md), incluidas las fuentes preferidas de SFX gratuitos, Mixkit y Freesound CC0, y su registro de licencia.
- Crear o colocar recursos, transiciones y movimientos: [lenguaje visual](references/visual.md) y catálogo del kit.
- Ejecutar un montaje en Clipo: [uso del MCP](references/clipo.md), sólo cuando la tarea pida aplicarlo. No asumir herramientas, IDs o capacidades a partir de los nombres de este paquete.

Para brainstorming, mostrar opciones concretas y conservar la elegida y las pendientes. Para recursos, entregar fuente y exportación con estado y catálogo; no exigir grabaciones para definir un icono o movimiento.

## Preparar una preedición

Reutilizar `produccion/plantillas/brief.md`, `guion-flexible.md`, `lista-de-tomas.md` y `edicion.md`, sin duplicarlas. Seguir el [flujo compartido](../../../produccion/flujo.md): un episodio/ID, metadatos e índice, documentos solicitados y referencias a recursos comunes. Los medios pesados y rutas personales se mantienen fuera de Git. Antes de actuar sobre un archivo existente, inspeccionarlo.

Guardar los videos exportados según [ubicación de exportaciones finales](../../../produccion/flujo.md#ubicación-de-exportaciones-finales), fuera del repositorio y de las carpetas de skills. Las skills contienen instrucciones y referencias; los recursos gráficos reutilizables mantienen su ubicación en `marca/`.

Con material real, entregar historia, apertura, selección con archivo/in/out/motivo y plan de montaje según el encargo. Usar la [plantilla de plan](../../../produccion/automatizacion/plantilla-plan-montaje.json); `null` expresa pendiente. La referencia de cobertura define inventario, exploración y `story_beats`; la de Clipo define tiempos de origen, prueba representativa y aplicación real. No duplicar esos procedimientos aquí.

Conservar el contexto de acciones, reacciones y hablantes. No inventar experiencias ni usar imágenes generadas como si fueran propias. Si falta cobertura, adaptar la historia o registrar el pendiente. Atribuir opiniones a quien las expresa; los datos gráficos necesitan fuente y fecha. Proteger direcciones, documentos, placas y datos del hogar.

Usar gráficos para localizar, aclarar o comparar; cada pieza debe tener una razón. La entrada del logo no es una intro obligatoria. Los rangos de tiempos y presets del kit son propuestas editables, no cuotas ni fórmulas de retención.

Después de montar, verificar la historia completa con audio, sincronía, lectura, continuidad, datos y privacidad. Comparar preview y exportación; guardar y reabrir antes de afirmar persistencia. Distinguir «plan preparado», «aplicado», «verificado por muestras» y «revisión continua»; identificar en cuál hubo escucha real o sólo ASR. Dejar una lista concreta de correcciones para Liz. Registrar tiempo editorial, desarrollo técnico y esperas por separado cuando se midan; marcar lo no medido, sin convertir tiempo de agente en horas conjuntas.

## Dependencias según la tarea

- Dirección y plan: repositorio, contexto y referencias pertinentes; no requieren conexión con un editor.
- Montaje en Clipo: MCP disponible y estado/capacidades actuales, según `references/clipo.md`. Arturo desarrolla el editor; esta skill no autoriza desarrollarlo ni instalar herramientas. Sin conexión, entregar el plan y declarar lo no aplicado.
- Crear o renderizar composiciones animadas: skill `hyperframes` y sus dependencias sólo para esa tarea. Colocar recursos existentes no exige regenerarlos.
- Obtener SFX: acceso a la ficha y licencia de Mixkit o Freesound CC0; son bibliotecas web, no dependencias MCP. No instalar ni asumir una API para descargarlos.

## Mantener el paquete

La fuente mantenida de las tres skills de edición está en `.agents/skills/`; generar las copias personales con `py -3 -X utf8 scripts/sincronizar-skills-edicion.py --write` y comprobarlas con `--check`. No editarlas por separado. Actualizar decisiones sólo con instrucciones expresas; los hallazgos de una prueba van en su episodio. Validar el repositorio con `py -3 -X utf8 scripts/validar.py` y ejecutar el validador de skill-creator cuando sus dependencias estén disponibles.
