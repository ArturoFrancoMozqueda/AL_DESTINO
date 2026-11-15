---
name: al-destino-edicion
description: "Preparar y refinar la preedición de videos de AL DESTINO: historia, hooks, selección de tomas, montaje, audio, gráficos y movimientos de marca. Usar para editar material real o desarrollar su paquete editorial y visual; ejecutar en Clipo mediante su MCP cuando esté disponible."
---

# Edición de AL DESTINO · v0.1 · BORRADOR

Crear un primer montaje con criterio editorial que Arturo y Liz puedan revisar y terminar. Arturo desarrolla Clipo y su MCP; esta skill consume sus capacidades. No convertir una tarea editorial en desarrollo del editor, ni exigir que su integración esté terminada para diseñar recursos.

## Contexto y fuentes

Trabajar desde la raíz del repositorio AL_DESTINO, resolviéndola desde esta carpeta si hace falta. Leer `AGENTS.md`, `contexto/vision-y-preferencias.md` y `contexto/perfil.json`; consultar `contexto/decisiones.md` ante contradicciones. Marca vigente en `marca/manual.md` y `marca/tokens/brand_tokens.json`. No elevar una propuesta gráfica o un piloto a aprobado.

El [índice común de recursos](../../../marca/recursos.json) une logos, ambas animaciones existentes, fuentes, iconos, componentes y motion propuesto con IDs estables. Las aplicaciones de video se revisan en el [módulo de video del design system](../../../marca/video/v01/index.html). Usar `motion.logo.horizontal`/`motion.logo.circular` para localizar las animaciones originales y `video.componente.*` para los rótulos. Las muestras con corchetes son mockups. No confundir `archivo_disponible` con compatibilidad en Clipo, ni `especificacion_sin_render` con animación implementada. Copiar sólo esta carpeta de skill no incluye los recursos de marca del repositorio.

## Elegir la parte del trabajo

- Dirección vigente: [referencia elegida y acabado profesional/elegante](references/referencia-video.md). Aplicarla al diseñar y montar, conservando los límites de la revisión parcial.
- Historia, apertura y estructura: [narrativa y hooks](references/narrativa.md).
- Selección, ritmo, continuidad, sonido y color: [montaje](references/montaje.md).
- Crear o colocar recursos, transiciones y movimientos: [lenguaje visual](references/visual.md) y catálogo del kit.
- Ejecutar un montaje en Clipo: [uso del MCP](references/clipo.md), sólo cuando la tarea pida aplicarlo. No asumir herramientas, IDs o capacidades a partir de los nombres de este paquete.

Para brainstorming, producir opciones concretas y mostrar la diferencia entre ellas; conservar la elegida por el usuario y las pendientes. Para producir recursos, entregar fuentes y exportaciones, con fecha, estado y catálogo. No pedir grabaciones para dibujar un icono o definir un comportamiento.

## Preparar una preedición

Reutilizar `produccion/plantillas/brief.md`, `guion-flexible.md`, `lista-de-tomas.md` y `edicion.md`, sin duplicarlas. Seguir el [flujo compartido](../../../produccion/flujo.md): un episodio/ID, metadatos e índice, documentos solicitados y referencias a recursos comunes. Los medios pesados y rutas personales se mantienen fuera de Git. Antes de actuar sobre un archivo existente, inspeccionarlo.

Con material real, entregar historia y alternativas de hook, selección con archivo/in/out/motivo y plan de montaje. Usar la [plantilla de plan](../../../produccion/automatizacion/plantilla-plan-montaje.json) como estructura de trabajo; `null` expresa pendiente, no un valor listo para ejecutar. Registrar hablante sólo si se reconoce o se confirma. Vincular datos gráficos a una fuente y fecha; separar opinión real de dato comprobado.

No inventar visitas, reacciones, conflicto, diálogo o recomendaciones para completar un arco. Si falta cobertura, adaptar la historia o registrar la toma pendiente. No rellenar con imágenes generadas que parezcan propias. Proteger direcciones, documentos, placas y datos del hogar.

Usar gráficos para localizar, aclarar o comparar; cada pieza debe tener una razón. La entrada del logo no es una intro obligatoria. Los rangos de tiempos y presets del kit son propuestas editables, no cuotas ni fórmulas de retención.

Después de montar, verificar la historia completa con audio, sincronía, lectura, continuidad, datos y privacidad. Comparar preview y exportación; guardar y reabrir antes de afirmar persistencia. Distinguir «plan preparado», «aplicado», «verificado en preview» y «verificado en exportación». Dejar una lista concreta de correcciones para Liz y registrar tiempo real.

## Mantener el paquete

Actualizar sólo decisiones expresas de Arturo/Liz en `contexto/decisiones.md`; los hallazgos de una prueba van en su episodio. No adjudicar a Liz preferencias que sólo declaró Arturo. Validar cambios con `python3 scripts/validar.py` (en este Windows: `py -3 -X utf8 scripts/validar.py`). Para cambios en composiciones animadas, usar las skills y comprobaciones de HyperFrames aplicables. No confundir una especificación de motion con una animación implementada en Clipo.
