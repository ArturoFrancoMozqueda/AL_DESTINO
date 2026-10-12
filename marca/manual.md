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
