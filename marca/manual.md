# AL DESTINO · Design system v0.6 · BORRADOR

Actualización: 12 de octubre de 2026. Dirección: pareja protagonista, lugares atractivos, momentos reales y consejos cercanos. Referente elegido por Arturo: @elmundoenpareja_, con alcance de observación documentado en `direccion-editorial-redes.md`. Las decisiones de diseño son propuestas; no implican resultados de alcance ni aprobación definitiva.

## Identidad y voz

Arturo y Liz son el centro de la historia. Promesa propuesta: «Lugares bonitos. Momentos nuestros». Comunicar descubrimiento, disfrute y aprendizajes desde lo vivido, con conversación natural. Morelia es la base y no limita destinos. Lifestyle y perro aparecen cuando forman parte de la experiencia; respetar intimidad y mencionar trabajo sólo superficialmente.

## Logo y animaciones

Conservar el logo original, sus proporciones, lettering, sol y ola. `assets/logos/logo-original-referencia.png` es la referencia intacta; `assets/logos/piezas/logo-horizontal-transparente.png` es la extracción de trabajo. Las partes ocultas no se reconstruyeron y el pie compartido A/L tiene una separación propuesta documentada. No existe un vector maestro nuevo.

Dos aplicaciones principales: horizontal sobre beige arena y circular para perfil. Usar el monograma cuando el tagline no sea legible; protección inicial de 20% de la altura del monograma. No deformar ni recolorear el dibujo. La paleta v0.6 gobierna gráficos y textos; los píxeles del logo conservan sus colores originales.

Dos animaciones HyperFrames por elementos, sin audio y con 3.2 segundos a 30 fps: horizontal 1920 × 1080 en `motion/logo-al-destino/`; circular 1080 × 1080 en `motion/logo-circular/`. El APNG horizontal es transparente; el circular lleva círculo beige y exterior transparente. Ambos incluyen secuencia de 96 PNG. Usar como cierre o firma breve cuando aporte; no retrasar el gancho con una intro obligatoria.

## Paleta gráfica natural

- Terracota #C65D3B: un detalle cálido, sin llenar todas las portadas.
- Turquesa #287C7A: agua y descubrimiento; acento de apoyo.
- Mostaza #C49A43: luz y detalle, uso ocasional.
- Beige arena #E3DEC9: placas de logo y superficies gráficas.
- Verde petróleo #244B49: contraste, fondos oscuros y llamadas a la acción.
- Café oscuro #302722: lectura principal y datos.

Las fotos conservan su color real: no teñir todo de beige. La imagen propia es la primera capa de identidad; los colores gráficos acompañan. Un acento por pieza suele bastar; la firma de dos autores puede utilizar dos como código opcional.

Contraste calculado sobre colores sólidos: café/arena 10.81:1; arena/petróleo 7.14:1; café/mostaza 5.59:1. Terracota/arena 3.09:1, turquesa/arena 3.66:1 y café/terracota 3.50:1 sirven sólo para texto grande, no texto pequeño. Objetivo de lectura: 4.5:1 para texto pequeño y 3:1 para grandes titulares. Sobre fotografía, comprobar el fondo real y usar placa sólida si hace falta. Los valores exactos y permisos figuran en `tokens/brand_tokens.json`.

## Tipografía y espaciado

Plus Jakarta Sans es la voz principal: 500–600 para datos, subtítulos y texto; 700–800 para ganchos legibles. Cormorant Garamond 400–600 aporta un acento editorial ocasional, sin hacer que todas las piezas parezcan una revista de lujo. Fuentes y licencias locales en `assets/fuentes/`.

Escala de espacios: 8, 16, 24, 32, 48 y 64 px en base 1280. Para YouTube, titular inicial 80–112 px, una promesa y hasta dos líneas, con prueba a 160 y 320 px. Para video 1920 × 1080: etiqueta inicial 36 px. Para vertical 1080 × 1920: subtítulos iniciales 48–64 px. Son puntos de partida, no tamaños universales; acortar copy cuando no quepa.

## Fotografía y composición

Fotos propias de experiencias reales: un plano abierto del lugar, ustedes dentro de la acción y detalles que transmitan la experiencia. Luz natural, blancos neutros, pieles fieles y contraste moderado. No simular reacciones ni presentar imágenes generadas como una visita real. No publicar direcciones, documentos, placas ni datos identificables del hogar.

Instagram: fotografía protagonista; portadas limpias; texto breve cuando aclara una promesa. Alternar de forma natural lugar, pareja y detalle sin una cuadrícula rígida. Historias destacadas con fotos propias y nombres de experiencias realmente documentadas.

YouTube: una historia que se entiende, miniatura con escena dominante y gancho legible. La miniatura adapta el mensaje, no copia automáticamente una portada de Instagram. La firma y el logo son opcionales si compiten con la escena.

Firma auxiliar: dos trazos terracota/turquesa, proporción 32 × 4 px y separación 4 px. No reemplaza el logo. Las notas A/L identifican quién habla sin atribuir personalidad o gustos. Los ejemplos «Vamos por pan», «Nos vamos a Vallarta», «Nos mudamos» y «Y viene el perro» son exploraciones pendientes de grabación, no testimonios.

## Formatos, edición y descargas

Ver `formatos-y-fuentes.md` para fuentes y límites consultados. Banner 2560 × 1440 y zona central conservadora 1540 × 420; avatar 1080 × 1080. Miniatura ligera 1280 × 720 y maestro 3840 × 2160. Vertical 1080 × 1920 con pruebas de recortes. Las guías internas no garantizan encaje con interfaces cambiantes.

Entrada: `design-system.html`; catálogo completo: `exportaciones/index.html`; kit: `exportaciones/AL-DESTINO-kit-marca.zip`. Los 72 PNG se agrupan por uso. La ruta `exportaciones/v05-png/` y el nombre del ZIP de elementos se conservan por compatibilidad de enlaces; el catálogo registra versión 0.6. Los PNG son assets o referencias raster; no se presentan como proyectos editables de fotografía.

Fuentes del sistema: HTML, tokens JSON/CSS y composiciones HyperFrames. `guia-detallada.html` mantiene las pruebas y es la fuente de exportación. Las fotografías de aplicaciones v0.3 son mockups ficticios y permanecen en archivo, fuera de las propuestas vigentes. Conservar originales sin modificarlos.

## Flujo sostenible

Una salida puede producir video, Reel, carrusel e historias, sin prometer todas las piezas cada semana. Priorizar un video largo semanal dentro de ocho horas conjuntas iniciales, ajustando al esfuerzo real. Registrar lo observado y el consejo verificable. Los presupuestos y destinos siguen abiertos por consulta.

Verificar con `python3 scripts/validar.py`. Exportar PNG con `scripts/exportar-design-system.cjs` y reconstruir el kit con `scripts/empaquetar-marca.py`. Guardar fuentes y exportaciones por separado; no cambiar BORRADOR a aprobado por haber publicado la guía.

## Aplicaciones de video y uso por el agente · 14 de noviembre de 2026

El apartado de video de `design-system.html` lleva a `video/v01/index.html`. Es una aplicación de esta misma identidad: reutiliza tokens, fuentes, logo y ambas animaciones existentes. Arturo pide acabado profesional y elegante; tipografía clara, espacio y acentos contenidos son propuestas de aplicación, no una aprobación de cada muestra. La voz sigue siendo natural y cercana.

`recursos.json` es el índice común generado para el agente: IDs estables, rutas de fuentes/exportaciones, hashes y limitaciones. Vincula el material existente, sin mover originales ni crear otro logo. Los catálogos detallados conservan sus rutas. `video/v01/motion.json` contiene movimientos propuestos; las animaciones del logo en `motion/` sí tienen renders, pero su importación/reproducción en Clipo sigue pendiente de prueba. Usarlas como firma/cierre cuando aporten y conservar su duración/fps originales al importarlas.

La skill de contenido trabaja concepto y voz; la de edición decide selección, montaje y colocación de recursos; Clipo/MCP aplica lo que sus capacidades permitan. La aprobación de una pieza, la prueba técnica y la autorización de publicar son hechos distintos y se registran por separado.

## Dirección de gráficos de viaje · 16 de noviembre de 2026

Arturo pide PNG ilustrados con intención profesional y elegante y Alan por el Mundo como referente. La barra verde con texto blanco contorneado fue rechazada como solución por defecto. Preparar los elementos antes de montarlos, con tipografía propia y prueba sobre la toma; Canva u otra herramienta pueden utilizarse cuando hagan falta. La ilustración acompaña la experiencia sin copiar la identidad del referente. Las muestras v01 se conservan como referencia, sin imponerlas al episodio.

Corrección posterior de Arturo: también rechaza el fondo de papel. La dirección vigente es el elemento recortado sobre el metraje, sin soporte ni borde blanco; texto independiente sólo si aporta. La imagen puede quedar sin gráfico. La [mesa v02](exportaciones/video-v02/index.html) se conserva como antecedente descartado para esta dirección.

Propuestas BORRADOR actuales: [recortes sin placa v03](exportaciones/video-v03/index.html). Fuentes raster, procedencia/prompts y catálogo en `video/v03/`; PNG transparentes en `exportaciones/video-v03/`. Incluyen pan/café genéricos y una ilustración de pan almendrado basada en material propio. No son fotos exactas de la experiencia. No cambian logos ni tokens y aún no tienen importación/animación comprobadas en Clipo. Las pruebas sobre grabaciones propias se conservan con el episodio, fuera del área pública.


### Alcance aclarado: iconos editoriales y firma

Arturo precisa que busca sobre todo likes, pin de ubicación y nuestro logo, con un acabado coherente sobre el metraje. El [kit editorial v04](exportaciones/video-v04/index.html) es la propuesta principal: SVG propios y PNG transparentes, con variantes claras/oscuras para los iconos. El logo horizontal es copia de la extracción existente; el monograma se recorta de ella conservando sus píxeles, formas y colores. No se recolorea el logo para hacerlo coincidir con los iconos. Ambas animaciones existentes siguen disponibles por referencia.

Los recortes alimentarios v03 son exploración opcional; no sustituyen el kit de likes, ubicación y firma. No se aprueba una escala de valoraciones ni se inventan contadores. Se comprueban lectura, transparencia, posición y movimiento sobre la toma; los recursos siguen BORRADOR, sin prueba de importación/animación en Clipo.


### Revisión para funcionar sobre video · 16 de noviembre de 2026

Arturo pide que los recursos no dependan de un fondo verde o beige para lucir y solicita animación premium del logo. El kit v04.1 incorpora contraste local dentro del alfa de los PNG; la variante universal se prueba sobre claro, sombra y detalle, sin placa. El raster original del logo se conserva delante y una capa fina de apoyo va detrás. Las versiones originales sin apoyo siguen disponibles.

La [firma animada por piezas](motion/logo-al-destino/premium/revision.html) entrega logo completo y monograma de 4 s, en APNG y WebM transparentes, con secuencias PNG. La ola, el sol y las letras entran coordinados, sostienen lectura y salen a transparencia. Se conserva la versión anterior. Son recursos BORRADOR, renderizados y con alfa comprobado; su uso e importación en Clipo todavía necesitan prueba. Los fotogramas del viaje usados para contraste y la demo permanecen privados con el episodio.

### Rótulos y orientación geográfica · 16 de noviembre de 2026

La [mesa editorial animada](exportaciones/editorial-v01/index.html) amplía el kit con redes sociales, nombres de lugares, plantilla de mapa, flechas curvas y like. Fuente editable y configuración en [editorial-v01](motion/editorial-v01/catalogo.json). Sigue la dirección sin placa y conserva la firma original. Los ejemplos de cuentas, restaurantes y mapa son demostraciones identificadas, no datos de AL DESTINO ni archivos listos para un episodio; personalizarlos con información confirmada y volver a exportar. Flechas y like son elementos reutilizables sin datos ficticios.

Presentar el mapa en la primera referencia relevante a cada lugar, con nombre y sucursal verificados; repetir sólo cuando ayude a explicar un traslado o cambio. Ante ambigüedad, confirmar el lugar con Arturo antes de fijar el pin. La plantilla conserva atribución y relación entre mapa y marcador; no representa una ruta real por tener una línea dibujada. Fuente, fecha y atribución acompañan el mapa concreto. La [guía de rótulos y mapas](../.agents/skills/al-destino-edicion/references/rotulos-mapas.md) concentra el procedimiento editorial.

Las animaciones y sus parámetros conservan estado BORRADOR. Disponibilidad de PNG, APNG o WebM no demuestra importación en Clipo. Las pruebas sobre grabaciones propias se mantienen privadas fuera del área pública de marca.
