# AL DESTINO · Design system v0.5 · BORRADOR

Fecha: 11 de octubre de 2026. Actualización: 12 de octubre de 2026. Dirección: editorial cálida, cercana y visualmente cuidada. La fotografía y la experiencia tienen prioridad. No implica aprobación definitiva de logo, copy ni plantillas.

## Logo

La referencia original del ZIP es la fuente de marca vigente para esta revisión. Se conserva byte a byte en `assets/logos/logo-original-referencia.png`. Los contornos reconstruidos de v0.2 fueron rechazados por Arturo y no se recomiendan.

Para las aplicaciones vigentes, usar `assets/logos/piezas/logo-horizontal-transparente.png` dentro de un viewport SVG, sobre arena #E3DEC9. El monograma es un encuadre de esa extracción del original; no una nueva versión dibujada. El archivo original con fondo claro queda como referencia y no se utiliza como placa blanca en las aplicaciones. Los archivos SVG contienen capas editables de composición, texto y fotografía, pero no convierten el logo en un vector maestro. Algunos PNG transparentes del paquete heredado presentan artefactos y no se usan como fuente visual.

Usar monograma para avatar, rótulos y firma pequeña. Lockup horizontal sólo donde el tagline sea legible; como regla inicial, mínimo 420 px en exportación de 1280 px, o usar monograma. Espacio de protección inicial: 20% de la altura del monograma. No deformar, girar, cambiar símbolos ni recolorear arbitrariamente. No se crean variantes claras/oscuras nuevas mediante recoloreado; usar la extracción del logo sobre una placa arena cuando haga falta contraste. En avatar mantener el símbolo dentro del círculo central.

## Color y contraste

Terracota #E65F3C; turquesa #158A8A; mostaza #D9A21B; beige arena #E3DEC9; verde petróleo #1F4D4D; café oscuro #2B211D.

Lectura principal: café oscuro sobre arena, o arena sobre verde petróleo. Terracota y mostaza son acentos; no usarlos para texto pequeño sobre arena. Turquesa/arena tampoco alcanza el objetivo de 4.5:1 para texto pequeño. Las mediciones exactas están en `tokens/brand_tokens.json`. Para texto pequeño se usa 4.5:1 como objetivo de legibilidad; para titulares grandes 3:1. No garantiza lectura sobre fotos: usar un panel sólido y revisar la composición.

Normalmente uno o dos acentos por pieza. La foto no necesita adoptar todos los colores de marca.

## Tipografía y escala

Cormorant Garamond Semibold para titulares; Plus Jakarta Sans Medium/Semibold para etiquetas, subtítulos y datos. Fuentes oficiales y licencias en `assets/fuentes/`. No sustituir sin registrar revisión.

En miniatura con viewBox 1280×720: titular inicial 88 px, máximo dos líneas, interlineado aproximado 0.95; etiquetas 20–22 px. Escala de espacios 8, 16, 24, 32, 48, 64 px. Los SVG maestros de 3840×2160 escalan todo 3×. Si el texto se desborda, acortarlo primero; revisar a 320 y 160 px. Etiquetas pequeñas son apoyo, no la promesa que debe leerse en móvil.

Rótulos 1920×1080: etiqueta 36 px y explicación 38 px; titular de tarjeta 96–130 px según extensión. Evitar rótulos simultáneos y datos innecesarios.

## Fotografía y composición

Fotos propias de Arturo y Liz, lugares, comida y detalles. Luz natural, color moderado, reacciones auténticas. Elegir una escena dominante y espacio negativo; evitar múltiples recortes compitiendo. En v0.3 se utilizan escenas fotográficas ficticias generadas con IA, identificadas como mockups. No representan un hotel, panadería, hogar ni perro reales; se sustituyen por fotos propias antes de uso documental.

YT01: estancia/lugar con historia. YT02: comida y recomendación personal. YT03: vlog/lifestyle en pareja. La foto ocupa el encuadre; el texto se coloca sobre espacio negativo con sombra gradual para lectura. Se usa una placa pequeña clara para el logo original cuando la imagen lo requiere. Limitar a una promesa clara, título corto y marca discreta. El título del video completa el mensaje sin repetir todo el texto de la imagen.

## Formatos y recortes

Ver `formatos-y-fuentes.md`. El banner 2560×1440 mantiene marca y frase dentro de una zona central conservadora de 1540×420. Portada vertical 1080×1920: guía interna de trabajo, nunca garantía de interfaces cambiantes. Previsualizar recortes reales antes de subir. Rótulo horizontal tiene fondo transparente salvo su panel.

## Edición y exportación

El archivo histórico `archivo/v03-aplicaciones/plantillas/` contiene SVG con grupos separados, fotografías y fuentes embebidas. El editor en `archivo/v03-aplicaciones/index.html` permite cambiar textos, reemplazar fotos y descargar SVG o PNG. Se produce localmente, sin Canva, por petición de Arturo. Cambiar el mockup por foto propia, verificar texto y eliminar guías antes de exportar. El catálogo de aplicaciones históricas está en `archivo/v03-aplicaciones/catalogo.json`; los PNG vigentes se consultan en `exportaciones/v05-png/index.html`.

Maestros: SVG. Preview: PNG, sin guías. Exportación ligera de miniatura 1280×720; maestro 3840×2160. Para móvil conservar archivo por debajo de 2 MB según documentación consultada. Banner menor de 6 MB. Avatar 1080×1080, revisar a 98×98 y en círculo.

## Motion propuesto

Rótulo de entrada breve, aparición de 150–250 ms y permanencia suficiente para lectura; transición sencilla o corte. Es una propuesta, no motion pack implementado. No añadir intro larga antes del gancho. Mantener ambiente y voz como centro.

## Versionado

Guardar original, archivo editable y exportación por separado; registrar ID de episodio, fuentes de fotos, licencia y estado. Las conversiones Canva anteriores se conservan como historial descartado, sin uso recomendado. Revisar fidelidad del logo, tamaños y separación de elementos en cualquier herramienta futura. No marcar «aprobado» por completar una exportación.

## Capa social propuesta · v0.4

Conservar el logo original y la paleta. Usar monograma en avatar y composición completa donde su tagline sea legible. Pruebas internas de perfil a 32 y 48 px, más 98 px por referencia de YouTube.

Cormorant queda para expresión editorial. Propuesta: Plus Jakarta Bold 700–800 para ganchos y Semibold para subtítulos. En 1280×720, punto de partida 80–112 px para título, 2–5 palabras y prueba a 160/320 px; decisiones de diseño revisables, no requisitos ni fórmula de rendimiento.

Vertical de trabajo 1080×1920: ganchos 72–112 px; subtítulos 48–64 px con máximo dos líneas. Guía interna: 8% izquierda, 16% derecha, 18% arriba, 34% abajo. Estos márgenes son orientativos y no una zona oficial universal. Los recortes 4:5, 3:4 y 1:1 sirven para probar portadas y no prescriben la vista actual de una cuenta.

Priorizar un acento protagonista y pares de alto contraste. Terracota/arena 2.56:1 se usa como decoración; turquesa/arena 3.09:1 sólo alcanza la referencia para texto grande. No confiar en sombras leves sobre fotografía.

Fuentes, límites y decisiones de investigación están en `investigacion-redes.json` y la sección Investigación del HTML. TikTok Ads se usa con su alcance publicitario explícito; acceso directo Meta/Instagram limitado. No se extrapolan estadísticas de anuncios a alcance orgánico. No hay garantía de crecimiento; las propuestas se validan con lectura, recorte y datos propios.


## Firma propia propuesta · v0.5

Dirección creativa: la A de Arturo y la L de Liz, dos miradas que firman su experiencia. Se mantienen intactos logo, colores y familias tipográficas. La portada del HTML muestra el origen del nombre y un punto de partida desde Morelia; no convierte esa ciudad en límite geográfico.

Gesto auxiliar: dos trazos rectos, paralelos, terracota arriba y turquesa abajo. Base 32 × 4 px por trazo, separación 4 px, escala proporcional y rotación 0°. No sustituye el logo ni se usa como nuevo avatar. La firma es opcional en tamaños pequeños. Sin degradados ni una colección de adornos turísticos.

Notas con autor: propuesta de Arturo con borde terracota, Liz con borde turquesa. Texto y nombres en café sobre arena. El código no asigna personalidades ni gustos. Completar con observaciones reales; en video, mostrar una nota a la vez. La doble firma permite ambos acentos como código funcional, manteniendo una jerarquía clara.

Voz: partir de lugares, planes y detalles concretos que ellos hayan declarado. Los ejemplos “Vamos por pan”, “Nos vamos a Vallarta”, “Nos mudamos” y “Y viene el perro” son exploraciones tipográficas; no testimonios, experiencias realizadas ni títulos aprobados. No inventar nombre/apariencia del perro. Privacidad en lifestyle: excluir direcciones, documentos y accesos.

El HTML incluye cuatro exploraciones para verificar que la firma siga reconocible al cambiar tema. Las invariantes y variables están en `tokens/brand_tokens.json`, clave `signature`. Ninguna exploración requiere fotografía ficticia. Las aplicaciones fotográficas futuras usarán material propio.

Referencia: [YouTube · personalidad y coherencia de marca](https://support.google.com/youtube/answer/12950272), consultada el 11 de octubre de 2026. La combinación de dos trazos, las notas de autor y la dirección tipográfica son decisiones creativas propias, no requisitos de YouTube. Estado: BORRADOR.


## Entregables PNG y animación por partes

Los elementos del sistema v0.5 se exportan por categoría en `exportaciones/v05-png/`. El catálogo distingue recursos, exploraciones de contexto y láminas de referencia. Los originales siguen en `originales/`; las revisiones anteriores en `archivo/`.

El logo se descompone en PNG de sus píxeles visibles en `assets/logos/piezas/`, con coordenadas y método registrados. Se conserva el original intacto; la transparencia y el límite del pie A/L son propuestas de extracción, sin recrear letras ni partes ocultas. La animación HyperFrames de `motion/logo-al-destino/` mueve A, L, sol, ola, divisor, nueve letras del nombre y tagline individualmente. Entregables: APNG con extensión `.png` y secuencia PNG RGBA, 1920 × 1080, 30 fps, 3.2 s, sin audio. La versión de revelación en bloque está descartada. Todo sigue BORRADOR.


## Fondo arena para el logo · preferencia de Arturo

Arturo expresó que le gustó mucho la animación y pide sustituir el blanco de las aplicaciones del logo por arena claro. Se adopta el arena existente #E3DEC9, sin añadir otro color ni recolorear el dibujo. La guía HTML, placas de firma, avatar, monograma y PNG de aplicación usan la extracción transparente sobre arena. El archivo original con fondo claro se conserva intacto y se identifica como referencia heredada. La animación transparente conserva su movimiento y sus fotogramas. Los entregables continúan BORRADOR.


## Entrada esencial

`design-system.html` resume el sistema en seis bloques e incluye la animación existente, con controles Repetir y Ver estático. Mantiene arena como fondo del logo y las descargas del sistema. `guia-detallada.html` conserva simuladores, exploraciones y fuentes completas. El manual y tokens permanecen como referencia técnica; el exportador PNG utiliza la guía detallada.

## Avatar circular animado · BORRADOR

Composición HyperFrames en `motion/logo-circular/index.html`. Cuatro piezas PNG originales animadas por separado sobre círculo beige arena #E3DEC9, con exterior transparente. 1080 × 1080, 3.2 segundos y 30 fps. APNG y secuencia PNG descargables desde la guía; versión estática para movimiento reducido. No sustituye el logo horizontal ni altera su animación.
