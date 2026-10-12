# AL DESTINO · Design system v0.2 · BORRADOR

Fecha: 11 de octubre de 2026. Dirección: editorial cálida, cercana y visualmente cuidada. La fotografía y la experiencia tienen prioridad. No implica aprobación definitiva de logo, copy ni plantillas.

## Logo

El lockup conserva monograma AL, sol, ola, divisor, nombre y tagline. El vector de trabajo se trazó desde `originales/extraido/AL_DESTINO_Design_System_v0.1/04_Referencias_visuales/Logo_horizontal_composicion_aprobada.png`, normalizando a la paleta. No es una tipografía recompuesta ni un PNG dentro de un SVG: contiene contornos editables. Sus bordes y pequeños detalles necesitan revisión de Arturo y Liz antes de adoptarlo como maestro.

Usar monograma para avatar, rótulos y firma pequeña. Lockup horizontal sólo donde el tagline sea legible; como regla inicial, mínimo 420 px en exportación de 1280 px, o usar monograma. Espacio de protección inicial: 20% de la altura del monograma. No deformar, girar, cambiar símbolos ni recolorear arbitrariamente. Variantes claras/oscuras se usan según contraste. En avatar mantener el símbolo dentro del círculo central.

## Color y contraste

Terracota #E65F3C; turquesa #158A8A; mostaza #D9A21B; arena #F6EBDD; verde petróleo #1F4D4D; café oscuro #2B211D.

Lectura principal: café oscuro sobre arena, o arena sobre verde petróleo. Terracota y mostaza son acentos; no usarlos para texto pequeño sobre arena. Turquesa/arena tampoco alcanza el objetivo de 4.5:1 para texto pequeño. Las mediciones exactas están en `tokens/brand_tokens.json`. Para texto pequeño se usa 4.5:1 como objetivo de legibilidad; para titulares grandes 3:1. No garantiza lectura sobre fotos: usar un panel sólido y revisar la composición.

Normalmente uno o dos acentos por pieza. La foto no necesita adoptar todos los colores de marca.

## Tipografía y escala

Cormorant Garamond Semibold para titulares; Plus Jakarta Sans Medium/Semibold para etiquetas, subtítulos y datos. Fuentes oficiales y licencias en `assets/fuentes/`. No sustituir sin registrar revisión.

En miniatura con viewBox 1280×720: titular inicial 88 px, máximo dos líneas, interlineado aproximado 0.95; etiquetas 20–22 px. Escala de espacios 8, 16, 24, 32, 48, 64 px. Los SVG maestros de 3840×2160 escalan todo 3×. Si el texto se desborda, acortarlo primero; revisar a 320 y 160 px. Etiquetas pequeñas son apoyo, no la promesa que debe leerse en móvil.

Rótulos 1920×1080: etiqueta 36 px y explicación 38 px; titular de tarjeta 96–130 px según extensión. Evitar rótulos simultáneos y datos innecesarios.

## Fotografía y composición

Fotos propias de Arturo y Liz, lugares, comida y detalles. Luz natural, color moderado, reacciones auténticas. Elegir una escena dominante y espacio negativo; evitar múltiples recortes compitiendo. En el kit, formas abstractas son placeholders identificados, no lugares reales ni rostros.

YT01: estancia/lugar con historia. YT02: comida y recomendación personal. YT03: vlog/lifestyle en pareja. El panel editorial es una base reemplazable; no obliga a que todas las miniaturas tengan idéntico montaje. Limitar a una promesa clara, título corto y marca discreta. El título del video completa el mensaje sin repetir todo el texto de la imagen.

## Formatos y recortes

Ver `formatos-y-fuentes.md`. El banner 2560×1440 mantiene marca y frase dentro de una zona central conservadora de 1540×420. Portada vertical 1080×1920: guía interna de trabajo, nunca garantía de interfaces cambiantes. Previsualizar recortes reales antes de subir. Rótulo horizontal tiene fondo transparente salvo su panel.

## Edición y exportación

`plantillas/` contiene SVG con grupos separados y fuentes embebidas para lectura local. La vista previa permite cambiar textos y descargar copia; Canva será el editor gráfico habitual. Reemplazar placeholder por foto propia, ajustar encuadre, verificar texto y eliminar guías antes de exportar.

Maestros: SVG. Preview: PNG, sin guías. Exportación ligera de miniatura 1280×720; maestro 3840×2160. Para móvil conservar archivo por debajo de 2 MB según documentación consultada. Banner menor de 6 MB. Avatar 1080×1080, revisar a 98×98 y en círculo.

## Motion propuesto

Rótulo de entrada breve, aparición de 150–250 ms y permanencia suficiente para lectura; transición sencilla o corte. Es una propuesta, no motion pack implementado. No añadir intro larga antes del gancho. Mantener ambiente y voz como centro.

## Versionado

Guardar original, archivo editable y exportación por separado; registrar ID de episodio, fuentes de fotos, licencia y estado. Un SVG convertido por Canva puede sufrir cambios: revisar fuentes, contornos, tamaños y separación de elementos. No marcar «aprobado» por completar una exportación.
