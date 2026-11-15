# Revisión inicial de edición automatizada · BORRADOR

Fecha: 14 de noviembre de 2026 · Arturo solicita explorar un primer montaje editable para revisión de Arturo y Liz. Alcance de esta entrega: inventario y viabilidad; implementación, integración definitiva y paquete de skill pendientes.

Actualización de alcance, misma fecha: Arturo aclara que desarrolla Clipo/MCP por su cuenta. El trabajo activo aquí es crear el paquete editorial y visual; esta revisión se conserva como antecedente técnico. Ver D-AUTO-02 en [decisiones](../../contexto/decisiones.md) y la [skill de edición](../../.agents/skills/al-destino-edicion/SKILL.md).

## Resultado

La identidad existente permite empezar sin rediseñarla. Clipo está accesible y tiene operaciones suficientes para ensayar cortes, audio, textos y gráficos editables. El trabajo pendiente principal es convertir material real en una propuesta narrativa trazable y comprobar el resultado dentro del editor y en una exportación. La conexión disponible no selecciona por sí sola los mejores momentos ni comprende la experiencia.

## Evidencia y límites

- Leídos: [instrucciones](../../AGENTS.md), [visión](../../contexto/vision-y-preferencias.md), [perfil](../../contexto/perfil.json), [decisiones](../../contexto/decisiones.md), manual, tokens y plantillas de producción. Preferencias declaradas: conversación natural, pareja y lugares protagonistas, consejos desde lo vivido; ocho horas conjuntas iniciales y Liz como editora. Clipo está en evaluación, todavía no elegido como editor definitivo.
- Revisión de archivos y código local el 14 de noviembre de 2026. Clipo: `C:/Users/fkr2d/Documents/repos/clipo`, versión de package.json 0.13.0, HEAD `b62a8f0`. Hay cambios locales sin commit, incluidos MCP/automatización; los hallazgos describen este árbol de trabajo y la app conectada, no una versión distribuida verificada. No se modificó ese repositorio.
- `clipo_status` respondió mediante conexión `desktop-local`: proyecto «Prueba IA - Clipo - 14 nov 2026», revisión 7, 16:9, un MOV de 1920 × 1080, tres cortes de cuatro segundos, una pista de música, textos y subtítulos; guardado informado como `saved`. Esto demuestra lectura de un montaje existente, no que lo haya creado esta revisión ni que los subtítulos sean correctos.
- En una observación posterior, la captura mostró Inicio y `clipo_get_ui` devolvió proyecto nulo/revisión 0. El estado cambió durante la inspección. No se atribuye una causa; cualquier edición futura debe volver a leer el proyecto. No se abrió ni modificó un proyecto para este diagnóstico.
- La captura es de la interfaz, no un render. No se escuchó el audio ni se verificaron reproducción, exportación o persistencia tras reiniciar. Los subtítulos observados incluyen un elemento que termina en 12.6 s frente a 12 s de pista principal: revisar límites en el piloto, sin diagnosticar una causa desde esa muestra.
- [Video de referencia](https://www.youtube.com/watch?v=vPsSfW0X_sI): el intento de acceso web falló. Se conservan como referencia provisional los hallazgos aportados por Arturo: planos generales/detalles/reacciones; logo blanco y marca de agua; presentación de conductores; rótulos de lugares y restaurantes; precios; flechas curvas; pulgares; Instagram; QR/reservas y algunos fundidos. No se validaron nuevamente ni se deducen audio, tiempos, curvas o resultados de audiencia.

## Inventario reutilizable

Rutas relativas a la raíz de AL_DESTINO, salvo indicación expresa.

| Recurso | Ruta concreta | Estado y uso posible |
|---|---|---|
| Guía esencial vigente | `marca/design-system.html` | v0.6, BORRADOR; entrada principal. |
| Reglas y datos de marca | `marca/manual.md`, `marca/tokens/brand_tokens.json`, `marca/tokens/brand_tokens.css` | Paleta, contraste, tamaños de partida y funciones tipográficas. Arena vigente #E3DEC9. |
| Fuente reproducible de gráficos | `marca/guia-detallada.html`, `scripts/exportar-design-system.cjs` | La guía detallada alimenta exportaciones; no sustituirla por capturas de la guía concisa. |
| Logo original y extracción | `marca/assets/logos/logo-original-referencia.png`, `marca/assets/logos/piezas/logo-horizontal-transparente.png` | Original intacto y extracción de trabajo. No hay nuevo vector maestro. |
| Capas originales de trabajo | `marca/assets/logos/piezas/catalogo.json` y PNG vecinos | Coordenadas, tamaños y hashes; separación A/L y bordes aún revisables. |
| Fuentes locales | `marca/assets/fuentes/PlusJakartaSans[wght].ttf`, `marca/assets/fuentes/CormorantGaramond[wght].ttf` | También versiones itálicas y licencias OFL. Jakarta principal; Cormorant como acento. |
| PNG y manifiesto | `marca/exportaciones/v05-png/catalogo.json`, `marca/exportaciones/kit-manifiesto.json` | 72 PNG, revisión 0.6 pese al nombre v05. Incluyen láminas, muestras y placeholders; no son 72 plantillas de video. |
| Gráficos candidatos | `marca/exportaciones/v05-png/logos/`, `firma/`, `notas/` | Logos y firma reutilizables; notas de autor como punto de partida. Se inspeccionó `notas/nota-arturo.png`: contiene texto de ejemplo, no una opinión real. |
| Motion horizontal | `marca/motion/logo-al-destino/index.html`, `renders/catalogo.json` | HyperFrames editable; APNG transparente y 96 PNG a 30 fps, 3.2 s, sin audio. |
| Motion circular | `marca/motion/logo-circular/index.html`, `renders/catalogo.json` | 1080 × 1080, 3.2 s, 30 fps; círculo arena y exterior transparente. |
| Referencias visuales | `marca/direccion-editorial-redes.md`, `marca/investigacion-redes.json` | Observación parcial de Instagram de octubre; no análisis audiovisual del video indicado. |
| Referencias de investigación | `investigacion/LEEME.md`, `investigacion/guias/metodologia.md` | Antecedentes con límites documentados; no evidencia de retención o CTR privados. |
| Preparación y edición | `produccion/flujo.md`, `produccion/plantillas/brief.md`, `guion-flexible.md`, `lista-de-tomas.md`, `edicion.md` | Reutilizar promesa, momentos, datos, privacidad y registro de esfuerzo. Las últimas cuatro plantillas están dentro de `produccion/plantillas/`. |
| Skills del repositorio | `.agents/skills/al-destino-local/SKILL.md`, `.agents/skills/al-destino-airbnb/SKILL.md`, `.agents/skills/al-destino-hoteles-playa/SKILL.md` | Investigación específica; no existe todavía una skill editorial de montaje de AL DESTINO. |

Skills disponibles en el entorno: `skill-creator` para el futuro paquete; HyperFrames y sus flujos de motion, audio y medios para adaptaciones que realmente lo necesiten. Están instaladas fuera del repositorio; no equivalen a un paquete reproducible propio de AL DESTINO. Esta revisión no crea una skill ni modifica composiciones.

Se inspeccionó la hoja de fotogramas `marca/motion/logo-al-destino/snapshots/por-elementos/contact-sheet.jpg`; sirve como antecedente visual, no como verificación nueva de la reproducción. `marca/archivo/`, originales y la revelación en bloque descartada no son fuentes vigentes por defecto. No se localizaron grabaciones de una experiencia en este repositorio; el único MP4 localizado es esa animación descartada. El MOV del proyecto Clipo no está documentado aquí como material de un episodio.

## Listo, por adaptar y faltante

**Listo para ensayar:** reglas de identidad, logos raster, paleta, fuentes locales, composiciones motion originales, estructura de brief y criterios editoriales básicos. Todo conserva su estado BORRADOR.

**Por adaptar:** rótulo de lugar, presentación de Arturo/Liz, tarjeta de precio y subtítulos con jerarquía de marca. Notas/firma aportan lenguaje visual, pero hay que comprobar escala sobre video, contraste, márgenes y duración de lectura. El logo blanco de la referencia no autoriza recolorear el propio. El logo original requiere una superficie que mantenga contraste sobre cada toma.

**Pendiente de comprobar en Clipo:** animación APNG y secuencias PNG. El código trata PNG como imagen mediante `HTMLImageElement`; no se encontró un importador de secuencias ni decodificación temporal de APNG ligada a la timeline. No asumir reproducción, búsqueda por tiempo o exportación correctas. Alternativa para el piloto: una pieza PNG existente con keyframes nativos de posición/opacidad. Así se ensaya animación editable sin trasladar todavía el logo completo. Una conversión a video con alfa también exigiría comprobar formato y decodificador.

**Falta para automatizar una experiencia:** carpeta de medios elegida, inventario estable con duraciones/formato/fps, transcripción revisable del material fuente, descripción visual y selección con in/out y motivo, datos reales con fecha/fuente, exclusiones de privacidad y plan narrativo. No se encontró un contrato de episodio que enlace todo eso a la timeline. Faltan asimismo criterios medidos de calidad/tiempo y un ensayo de exportación con sus archivos reales, especialmente HEVC/HDR o clips grandes.

**Gráficos no encontrados como plantillas vigentes específicas:** flechas curvas, valoraciones de pulgares, Instagram, QR/reservas y precio con campos editables. Los estilos genéricos «precio» y «ubicacion» de Clipo no equivalen a versiones AL DESTINO. Son candidatos opcionales para pruebas posteriores; QR, precios, valoraciones y cuentas sólo con datos suministrados/verificados. Música/SFX con licencia no están reunidos como biblioteca operativa del canal.

## Clipo: capacidades y límites encontrados

Rutas de esta sección dentro de `C:/Users/fkr2d/Documents/repos/clipo`.

| Área | Evidencia de código/documentación | Implicación |
|---|---|---|
| Persistencia | `src/types.ts`, `src/db.ts`, `src/autosave.ts` | Proyecto estructurado y medios como blobs separados en IndexedDB `clipo`, versión 2: stores `projects`, `blobs`, `meta`. JSON de proyecto solo no transporta sus medios. Escritorio y web/PWA tienen almacenamiento separado. |
| Medios | `src/media.ts`, `src/convertVideo.ts`, `src/proxies.ts` | Importación local, inspección/posible conversión según decodificador y proxies para preview. Mantener originales externos; no inferir compatibilidad de una cámara por su modelo. |
| Timeline | `src/types.ts`, `src/automation/schema.ts`, `src/automation/edits.ts` | Principal consecutiva: duración `(out-in)/speed`. Audio, texto, stickers y overlays tienen inicio absoluto. Cambiar cortes requiere retimar esas pistas explícitamente. |
| Texto y marca | `src/fonts.ts`, `src/fontFiles.ts`, `src/brand.ts` | Texto editable, color, tamaño, posición y estilos. Kit de marca local fuera del proyecto. Cormorant está en catálogo, configurada a peso 700; los pesos de marca 400–600 requieren ajuste/verificación. Plus Jakarta Sans no aparece en el catálogo observado. No sustituirla silenciosamente. |
| Animaciones | `src/types.ts`, `src/render.ts`, `src/automation/schema.ts` | Entradas/salidas de texto y keyframes de posición, tamaño, giro y opacidad para textos/stickers/overlays. Easing expuesto: `linear` o `ease`; no equivalencia automática con GSAP. |
| Sonido/subtítulos | `src/automation/captionJobs.ts`, `src/captions.ts`, `src/audioFx.ts` | Whisper local para clips principales recortados; requiere revisar texto y tiempos. Hay fades, roles de audio, ducking y normalización; no escuchados ni medidos en esta revisión. La transcripción del bruto para selección editorial es otra necesidad. |
| Previews/export | `src/engine.ts`, `src/render.ts`, `src/exporter.ts`, `src/exportSupport.ts` | Preview canvas, proxies y captura de ventana. Exportación WebCodecs con fallback a grabación en tiempo real. FPS del exportador fijado en 30; el código de conversión documenta salida máxima 1080p. No asumir entrega 4K/HDR/60 fps ni que una captura valida audio/export. |
| Plantillas | `src/templates/build.ts`, `src/templates/types.ts` | Plantillas con slots y textos; guardadas en localStorage. No equivalen a intercambio íntegro de proyectos con todos sus medios y pistas. |
| CapCut | `src/components/CapcutImport.tsx`, `src/importers/capcut.ts`, `src/importers/capcutProject.ts` | Importa borradores y medios seleccionados, con pérdidas informadas; fuentes, colores y animaciones de texto originales no se conservan. No usarlo como formato maestro de AL DESTINO. |
| Automatización existente | `docs/MCP.md`, `mcp/server.mjs`, `src/automation/bridge.ts`, `electron/automation.cjs` | MCP STDIO disponible y conectado. Puente HTTP privado local autenticado, activado en modo agente. No es una API pública de servicio. |

Límites documentados del acceso automatizado: 8 archivos por importación, 128 MiB por archivo, 200 operaciones por lote, 1 MiB por comando y un comando simultáneo. Importar un clip grande manualmente y usar su ID es una opción documentada; no exige reducir el original. Los lotes requieren proyecto y revisión actuales, se aplican como un paso de Deshacer y guardan. Tras conflicto/error/timeout, releer antes de repetir. Metadatos, textos y capturas sí se comparten con el cliente IA, aunque el puente mantiene los medios locales.

## Importación, API y MCP

| Vía | Qué existe realmente | Coste para esta prueba | Evaluación provisional |
|---|---|---|---|
| Importar proyecto | CapCut, con pérdidas; no se encontró importador/exportador nativo portátil completo ni EDL/FCPXML/OTIO en las rutas revisadas. | Habría que definir e implementar intercambio nativo, versionado y resolución de medios, o aceptar pérdidas de CapCut. | Buena candidata futura para portabilidad y reproducibilidad; más trabajo previo que usar las operaciones existentes. No escribir IndexedDB desde fuera. |
| Script/API local | Puente HTTP privado de `electron/automation.cjs`; `mcp/bridge-client.mjs` llama a `/command`. Es posible reutilizarlo desde un script local sin protocolo MCP. | Adaptador pequeño, pero acoplado a un contrato interno, credenciales efímeras, app abierta y revisiones. | Válido si preferimos ejecutar un plan determinista desde terminal. No hace falta crear un servicio remoto ni otra API. |
| MCP existente | Herramientas de lectura, medios, lotes, UI semántica, subtítulos, previews y guardado. | Ya conectado; permite el piloto sin desarrollar transporte. Comparte el mismo motor/puente y límites de la vía directa. | Recomendación sólo para la primera prueba por disponibilidad actual. No es un requisito del sistema editorial ni una decisión definitiva. |

Propuesta: separar las decisiones editoriales del mecanismo que las aplica. El futuro plan debe poder conservar fuentes, in/out, orden, textos y motivos aunque después cambiemos de adaptador. Todavía no definir un esquema extenso sin haber probado un caso real.

## Información exacta pendiente de Clipo

No hace falta pedir acceso genérico: el repositorio y la conexión ya se encontraron. Para el siguiente ensayo hay que resolver:

1. Qué build/árbol de trabajo será la base y si los cambios locales de automatización forman parte de ella. No congelar el contrato sobre un HEAD que no contiene esos cambios.
2. Cómo incorporar Plus Jakarta Sans y los pesos necesarios si exigimos fidelidad de marca con texto editable. Un PNG sirve para una prueba visual, pero su texto deja de ser editable.
3. Si existe otra rama con intercambio nativo de proyectos o soporte temporal de APNG/secuencias que no se haya identificado aquí. Mientras tanto, tratar ambas capacidades como no verificadas.
4. Comportamiento real con los medios elegidos: tamaño, códec, HDR/SDR, fps, sincronía, capacidad de disco y exportación. Portabilidad Windows/Mac y respaldo completo siguen pendientes.

No son preguntas bloqueantes para documentar el diagnóstico; algunas sólo importan cuando se elija el piloto.

## Siguiente paso propuesto: un montaje mínimo de 20–30 segundos

Una sola experiencia real, 3–5 clips breves: contexto, acción/detalle y conversación o reacción auténtica, más un dato confirmado. Si sólo se usa el MOV del ensayo anterior, validaríamos mecánica de edición, no selección narrativa entre escenas.

1. Elegir la carpeta y registrar qué cuenta la escena, qué dato es cierto y qué debe excluirse. Mantener medios pesados fuera de Git, como establece el flujo actual.
2. Revisar esos clips y proponer una secuencia con archivo, in/out, razón de selección y vacíos de cobertura. Un plan pequeño, legible y conservado junto al episodio.
3. En un proyecto separado de prueba, aplicar cortes, sonido directo, un rótulo editable y una pieza PNG existente animada con keyframes. Resolver la fuente del rótulo o declarar explícitamente una sustitución temporal para la prueba técnica. Sin biblioteca gráfica completa ni música obligatoria.
4. Comprobar inicio/mitad/final en preview y escuchar de principio a fin; exportar una muestra 1080p/30 y compararla. Guardar, reabrir y comprobar que Liz puede cambiar un corte, el texto y la animación.

Criterios de aceptación propuestos: cada corte remite al original correcto; textos dentro de sus tiempos y legibles; voz comprensible y sincronizada; transparencia y animación consistentes al buscar por tiempo y exportar; medios presentes tras reabrir; edición manual posible. Registrar minutos reales de preparación y correcciones. Son criterios del ensayo, no resultados ya obtenidos.

Después de esa prueba, redactar una primera skill pequeña de AL DESTINO que reutilice brief/selección/revisión y separe las referencias de marca del adaptador de Clipo. Ampliarla con historia, audio/color y recursos gráficos según los problemas observados. La petición actual autoriza la exploración; ninguna integración, recurso nuevo o estilo queda aprobado por esta propuesta.
