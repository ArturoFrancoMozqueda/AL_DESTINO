# Tres referentes consolidados: Alan, Luisito y Lethal

Corte de investigación: 6 de octubre de 2026, zona America/Mexico_City. Se estudiaron los ocho videos largos más recientes de cada canal, sus metadatos públicos, nueve miniaturas inspeccionadas visualmente y doce entradas de Instagram por perfil. Las fechas de YouTube se convirtieron desde `publishDate` a CDMX. Las vistas son capturas puntuales, no cifras futuras ni garantía de alcance para un canal nuevo.

Fuentes principales: HTML público de `/videos` y `watch` de YouTube; perfiles y publicaciones públicas de Instagram; grillas del navegador capturadas por el agente principal. Se conservaron los registros JSON en `evidencia_grandes/` para revisar cálculos. Se usaron buscadores y agregadores para descubrir enlaces, pero los cuadros finales se reconstruyeron con metadatos primarios. No se vieron completos los 24 videos: las conclusiones sobre estructura parten de títulos, descripciones y capítulos; las observaciones de diseño sí parten de imágenes inspeccionadas.

## Lectura comparativa

| Referente | Propuesta observable | Largos publicados 8 ago–6 oct (60 días) | Mediana entre las últimas 8 publicaciones | Mediana de duración |
|---|---|---:|---:|---:|
| Alan por el mundo | Series por destino y decisiones prácticas | 5 | 17.1 días | 17.4 min |
| Luisito Comunica | Curiosidad, experiencias y personalidad | 7 | 8.0 días | 24.4 min |
| Lethal Crysis | Documental de personas, acceso y exploración | 2 | 24.0 días | 38.5 min |

Estas cadencias describen esta muestra: Alan acumula cuatro largos desde el 13 de septiembre al 4 de octubre, mientras Lethal tiene pausas de casi 50 días. No se puede convertir una biografía que anuncia días de publicación en una frecuencia real sin revisar fechas. El muestreo excluye Shorts porque proviene de la pestaña `/videos` y los ocho registros `watch` tienen `isShortsEligible=false`.

El aprendizaje transferible es la claridad de la promesa. Alan ayuda a decidir; Luisito convierte una duda cotidiana en experiencia; Lethal promete acceso a una historia humana. Para un canal nuevo conviene definir primero cuál de esas necesidades resolverá, porque requiere recursos y ritmos distintos. Esta última frase es una recomendación, no un resultado causal de las vistas.

## Alan por el mundo

Identidad verificada: [YouTube @alanxelmundo](https://www.youtube.com/@alanxelmundo/videos), [Instagram @alanxelmundo](https://www.instagram.com/alanxelmundo/), [sitio oficial](https://alanxelmundo.com/). Instagram muestra aproximadamente 2M seguidores y 4,388 publicaciones en la captura pública; ambos son contexto de escala. La biografía indica actualmente Corea, mientras los videos recientes son Egipto: la fecha del viaje y la fecha de estreno son diferentes.

### Muestra de ocho videos largos

| Video | Fecha CDMX | Vistas públicas capturadas | Duración |
|---|---|---:|---:|
| [Conocí las pirámides de Egipto 4K — Alan por el mundo Egipto #9](https://www.youtube.com/watch?v=uTuWgiHT4Zs) | 2026-10-04 | 171,035 | 44:18 |
| [¿Vale la pena visitar Alejandría? 4K — Alan por el mundo Egipto #8](https://www.youtube.com/watch?v=vKwMLTnqN7w) | 2026-09-25 | 371,299 | 16:00 |
| [El templo "secreto" de Egipto, DENDERA — Alan por le mundo Egipto #7 4K](https://www.youtube.com/watch?v=VXHx8_F8Y70) | 2026-09-18 | 285,618 | 20:50 |
| [Cómo elegir un crucero por el Nilo — Alan por el mundo EGIPTO #6](https://www.youtube.com/watch?v=uzTTe4yklQc) | 2026-09-13 | 189,692 | 12:56 |
| [No sabías que esto estaba en México! 4K Alan por el mundo](https://www.youtube.com/watch?v=WzTLFitPSds) | 2026-08-24 | 407,883 | 18:47 |
| [Todo lo que debes saber de ABU SIMBEL 4K — Alan por el mundo Egipto #5](https://www.youtube.com/watch?v=cF-vYE5DZtw) | 2026-07-31 | 253,811 | 12:02 |
| [Así se vive en Fan Fest en Nuevo León 4K — Alan por el mundo](https://www.youtube.com/watch?v=o_G67M9N0ak) | 2026-06-17 | 222,147 | 12:02 |
| [Esta construcción cambió Egipto para siempre — Asuán Alan x el mundo #Egipto 4](https://www.youtube.com/watch?v=6sZw9JHrdqk) | 2026-05-31 | 297,237 | 19:20 |

### Qué se observa

- Seis de los ocho largos pertenecen a Egipto (#4 a #9), con número de episodio, destino y firma del creador. El resto muestra una experiencia mexicana y un evento en Nuevo León. La continuidad existe sin que el título dependa sólo de “día X”.
- Los títulos alternan utilidad (“Cómo elegir...”, “Todo lo que debes saber...”), evaluación (“¿Vale la pena...?”) y descubrimiento (“No sabías...”, “templo secreto”). Cada video tiene una pregunta o una razón autónoma para entrar.
- Las descripciones de Egipto declaran viaje en marzo/abril de 2026, grabación mayoritariamente con teléfono Samsung y enlaces a guía, presupuestos y eSIM. Se observa un producto editorial que sirve antes de viajar y permite prolongar el consumo en la web. No se infiere el precio de su equipo ni presupuesto de producción.
- En la descripción de Dendera, la introducción habla de elegir un crucero, igual que el episodio previo. Es una inconsistencia visible de metadatos; no prueba un problema del contenido del video. Para un canal nuevo, revisar descripción, enlaces y CTA por episodio evita ese error de reutilización.
- Cinco largos en los últimos 60 días equivalen a 0.58 por semana dentro de esa ventana; cuatro en los últimos 30 días. Los siete intervalos de la muestra van de 5.1 a 44 días. Existe actividad reciente más concentrada que su mediana de todo el conjunto.

### Miniaturas: observación directa, n=3

Se inspeccionaron pirámides, Alejandría y Dendera. Las tres usan una escena reconocible del destino y texto blanco grande centrado en dos líneas o una; las tres llevan una marca pequeña en una esquina inferior. Sólo Dendera muestra al presentador. Pirámides usa la perspectiva del corredor interior; Alejandría usa el puerto; Dendera usa columnas y profundidad. Las imágenes de pirámides y Alejandría están suficientemente oscurecidas para separar el texto. El texto visual responde qué se verá, mientras el título puede aportar decisión o sorpresa. No se midió CTR ni se afirmó que sea la causa de las vistas.

### Instagram: tres publicaciones verificadas

| Publicación | Fecha | Formato/ruta | Contenido de la leyenda | Interacción pública capturada |
|---|---|---|---|---:|
| [Pirámides](https://www.instagram.com/alanxelmundo/reel/DeFjLiFBua9/) | 4 oct 2026 | Reel | Anuncia el nuevo video de pirámides | 6,194 likes; 53 comentarios |
| [Kenia y Tanzania](https://www.instagram.com/alanxelmundo/p/Dd6nRYyjoh4/) | 30 sep 2026 | Publicación fotográfica | Recuerdos de ambos países | 17K likes; 142 comentarios |
| [Kenia y Tanzania en horizontal](https://www.instagram.com/alanxelmundo/p/DdwoXj8DuBt/) | 26 sep 2026 | Publicación fotográfica | Selección horizontal del viaje | 8,926 likes; 100 comentarios |

La grilla observada contiene 12 piezas entre 16 de septiembre y 4 de octubre: cinco rutas `/reel/` y siete `/p/`; 12/19 días × 7 = **4.4 piezas por semana dentro de esta muestra**. Son tipos de ruta/metadatos, no una inspección de todas las diapositivas ni de todos los clips. No se incluyeron Stories. La coincidencia del Reel de pirámides con el estreno de YouTube el 4 de octubre respalda un uso de Instagram para anunciar el largo; las fotos aportan memoria y destinos distintos al estreno.

### Oportunidad para un nuevo canal — inferencia

Crear series cortas por destino con una decisión por capítulo: cómo llegar, qué sí vale la pena y presupuesto real. Usar el mismo viaje para construir videos útiles y fotos/reels con funciones diferentes. La propuesta puede hacerse localmente; no requiere comenzar con una expedición internacional. La parte práctica debería indicar fecha del viaje y fuente actual de horarios/precios, porque hay desfase entre grabación y publicación.

## Luisito Comunica

Identidad verificada: [YouTube @luisitocomunica](https://www.youtube.com/@luisitocomunica/videos), [Instagram @luisitocomunica](https://www.instagram.com/luisitocomunica/). El perfil público muestra aproximadamente 33M seguidores y 3,031 publicaciones. El volumen y trayectoria lo vuelven referencia de empaquetado, no una base realista de vistas para un canal inicial.

### Muestra de ocho videos largos

| Video | Fecha CDMX | Vistas públicas capturadas | Duración |
|---|---|---:|---:|
| [No sabía que esto pasa en España — VLOG 🇪🇸](https://www.youtube.com/watch?v=ArTj5p3lTkc) | 2026-10-02 | 5,778,419 | 39:52 |
| [Así es la cantina más antigua de todo México (+150 años) — ¡Sobrevivió a todo!](https://www.youtube.com/watch?v=I1CXqUxhBj4) | 2026-09-23 | 5,069,336 | 33:03 |
| [Compré un hotel de 2 estrellas — ¿Qué tan malo es?](https://www.youtube.com/watch?v=4_gdo4yT_bg) | 2026-09-16 | 8,923,063 | 24:13 |
| [¿Vale la pena formarse HORAS por esta Coca-Cola “secreta”? — NUEVA YORK](https://www.youtube.com/watch?v=SipLo0atXTw) | 2026-09-03 | 14,549,814 | 21:13 |
| [Probando el UBER de helicópteros para millonarios — ¿Vale la pena? 🚁](https://www.youtube.com/watch?v=ErYcoE5frXc) | 2026-08-26 | 8,719,741 | 17:06 |
| [Así es CABO VERDE: el país más aislado de África — ¡Hermoso! 🇨🇻](https://www.youtube.com/watch?v=4DBy1-BdcsE) | 2026-08-18 | 9,046,566 | 45:59 |
| [Probando comida callejera en CABO VERDE — ¡Valió la pena el viaje! 🇨🇻](https://www.youtube.com/watch?v=L7eshVo3kpc) | 2026-08-11 | 9,892,694 | 24:01 |
| [Entrar a este país es MUY difícil y costoso — CABO VERDE 🇨🇻](https://www.youtube.com/watch?v=95sZykZh0Wg) | 2026-08-05 | 7,452,031 | 24:35 |

### Qué se observa

- Hay tres capítulos complementarios sobre Cabo Verde: acceso y trámites, gastronomía y recorrido del país. Los otros cinco tratan España, una cantina mexicana, hotelería, curiosidades de Nueva York y transporte en helicóptero. Un destino abastece varias promesas sin repetir exactamente el mismo formato.
- Siete de los ocho títulos contienen una pregunta evaluativa, sorpresa, dificultad o una característica extrema. La fórmula frecuente es experiencia concreta + duda: “¿Vale la pena?”, “¿Qué tan malo es?”, “difícil y costoso”. La promesa suele entenderse sin conocer previamente al creador.
- El video de Nueva York tiene capítulos para estación secreta, propiedad diminuta y diner histórico, pero el título concentra la curiosidad en la Coca-Cola. Esto muestra selección de una historia principal para vender un recorrido más amplio.
- Los capítulos visibles de helicópteros ordenan explicación de la app, funcionamiento, costos, embarque, vuelo y valoración. Es un ejemplo verificable de secuencia pregunta → prueba → evidencia práctica; no equivale a haber medido retención.
- Las descripciones de España, hotel, Coca-Cola y helicópteros anuncian publicidad de Holafly. El negocio de hotelería también forma parte del contenido. Se observa integración comercial explícita, sin poder calcular ingresos ni tarifa de patrocinio.
- Siete largos en 60 días equivalen a 0.82 por semana; tres en los últimos 30 días. Los siete intervalos de los últimos ocho van de 6.3 a 12.9 días, con mediana 8.0. En esta ventana mantiene una periodicidad cercana a un largo cada ocho días.

### Miniaturas: observación directa, n=3

España, cantina y hotel muestran al creador grande en primer plano, con un lugar reconocible detrás. La de España usa escena urbana y gesto abierto, sin gran texto añadido. La de cantina agrega un letrero “1869” y trata el fondo casi en escala de grises mientras el rostro/copa destacan. La de hotel combina edificio y dos estrellas amarillas cerca del dedo. En los tres casos el rostro ocupa un área relevante y el contexto prueba el tema. El sistema combina sujeto reconocible con una evidencia visual pequeña; no usa el mismo bloque de texto en todos los videos.

### Instagram: tres publicaciones verificadas

| Publicación | Fecha | Formato/ruta | Contenido de la leyenda | Interacción pública capturada |
|---|---|---|---|---:|
| [Con Jordi Sabaté](https://www.instagram.com/luisitocomunica/p/DdcJrphjMlz/) | 18 sep 2026 | Publicación fotográfica | Encuentro en persona y reconocimiento a su labor sobre ELA | 201K likes; 300 comentarios |
| [The Wild Project](https://www.instagram.com/luisitocomunica/p/DdZ0Y74DFGD/) | 17 sep 2026 | Publicación fotográfica | Anticipa la aparición en el podcast | 371K likes; 1,931 comentarios |
| [Grabación con otro creador](https://www.instagram.com/luisitocomunica/p/DdXHLefnO2l/) | 16 sep 2026 | Publicación fotográfica | Anticipa videos de colaboración | 559K likes; 2,662 comentarios |

La grilla contiene tres publicaciones fijadas de 2024, que se excluyen de cualquier cálculo de frecuencia. Las nueve entradas posteriores abarcan 2 de agosto–24 de septiembre de 2026: cuatro `/p/` y cinco `/reel/`, incluyendo dos colaboraciones cuyo autor/ruta pertenece a Ibai y Ary Tenorio. La tasa observada de presencia en el feed es 9/54 × 7 = **1.17 piezas por semana en esa muestra**; excluyendo colaboraciones son siete piezas propias en la ventana, 0.91/semana. No son tasas de producción ni actividad de Stories. No se debe dividir la antigüedad de las fijadas entre doce y llamar a eso frecuencia actual.

### Oportunidad para un nuevo canal — inferencia

Convertir pequeñas dudas en pruebas observables: un trayecto, una comida, una tarifa o un alojamiento. Mantener una persona reconocible y una prueba visual del tema en la miniatura. Se puede probar el esquema con turismo cercano y costos modestos. Evitar copiar superlativos sin evidencia: describir qué se comprobó y qué fue opinión. Usar Instagram también para relaciones, anticipación y momentos personales, con una propuesta que siga siendo entendible cuando el espectador no conoce al presentador.

## Lethal Crysis

Identidad verificada: [YouTube @lethalcrysis](https://www.youtube.com/@lethalcrysis/videos), [Instagram @lethalcrysis_](https://www.instagram.com/lethalcrysis_/). **Instagram lleva guion bajo final.** La biografía pública se presenta como documentalista y viajero de aventura, enlaza expediciones y fundación; aproximadamente 1M seguidores y 298 publicaciones. Es un referente de documental de viaje y acceso humano, más distante del vlog turístico cotidiano.

### Muestra de ocho videos largos

| Video | Fecha CDMX | Vistas públicas capturadas | Duración |
|---|---|---:|---:|
| [Ruta de la LIBERTAD: El paso MÁS DRAMÁTICO de la Guerra Civil Española](https://www.youtube.com/watch?v=GB2LbcyccME) | 2026-09-20 | 865,270 | 77:24 |
| [NOS ESTAFAN EN AMAZONAS](https://www.youtube.com/watch?v=d9gZZ91tUrY) | 2026-09-09 | 2,251,552 | 39:18 |
| [CASOS IMPOSIBLES en el CAMIÓN QUIRÓFANO de Diego G. Rivas](https://www.youtube.com/watch?v=wu-yX2lYWas) | 2026-07-21 | 578,888 | 37:10 |
| [El ritual donde muere tu EGO: Mi iniciación secreta en la selva de Gabón](https://www.youtube.com/watch?v=GZwSC2Eu5lc) | 2026-06-24 | 500,850 | 38:16 |
| [TOKYO DRIFT EN LA VIDA REAL — Carreras Ilegales](https://www.youtube.com/watch?v=KOEq1XQ6Uko) | 2026-05-31 | 2,203,186 | 32:59 |
| [72h en un BARCO DE GUERRA Español](https://www.youtube.com/watch?v=vIk68KYIUog) | 2026-05-10 | 1,172,672 | 38:46 |
| [MIGINGO: la isla MÁS SUPERPOBLADA del mundo](https://www.youtube.com/watch?v=Lx5ge3ExvQI) | 2026-04-30 | 1,866,976 | 30:13 |
| [¿Hay GENOCIDIO CRISTIANO en África?](https://www.youtube.com/watch?v=07LzDUgDiFw) | 2026-04-05 | 897,422 | 64:48 |

### Qué se observa

- Los temas de la muestra cubren memoria histórica, turismo indígena, cirugía en Liberia, ritual en Gabón, carreras en Tokio, vida naval, hacinamiento insular y conflicto en Nigeria. El lugar sirve de entrada a una comunidad, oficio, evento o problema.
- En títulos domina el acceso a situaciones extraordinarias: “72h”, “camión quirófano”, “en la vida real”, “mi iniciación”, junto con palabras de tensión o extremos. El episodio de Bielsa promete un paso dramático de la historia; el del Amazonas condensa un conflicto vivido.
- Las descripciones de Liberia y barco explican instituciones, protagonistas y acceso. El documental de Nigeria declara colaboración con un periodista; no se trata sólo de recorrer sitios. Las afirmaciones históricas o políticas de esos videos no fueron auditadas aquí y no se adoptan como hechos externos al canal.
- “Tokyo Drift” contiene una promoción de Revolut visible en su descripción. La publicación de Instagram de Nissan identifica publicidad y una serie de cuatro reportajes por España. Se comprueba la presencia de marcas, sin extrapolar presupuestos o ganancias.
- Dos largos en 60 días equivalen a 0.23 por semana; los mismos dos aparecen en los últimos 30 días. La mediana de siete intervalos es 24 días y la pausa máxima casi 50. La duración mediana es 38.5 min; dos videos de la muestra exceden una hora. Esto sugiere un modelo de estrenos más espaciados y extensos, pero no establece la plantilla ni costo de producción.

### Miniaturas: observación directa, n=3

Bielsa, Amazonas y camión quirófano no tienen bloques grandes de texto añadido. Cada una muestra personas junto a un entorno que explica la historia: personajes con vestuario y montañas, grupo en selva, médicos junto al camión. La de Amazonas usa primer plano con personas detrás; la de médicos privilegia la escala del vehículo; la histórica muestra un grupo y una localización montañosa. Texto físico en el vehículo es parte de la escena. El patrón de esta pequeña muestra es contexto humano y evidencia de acceso, no una promesa textual completa dentro de la imagen.

### Instagram: tres publicaciones verificadas

| Publicación | Fecha | Formato/ruta | Contenido de la leyenda | Interacción pública capturada |
|---|---|---|---|---:|
| [Recepción del documental](https://www.instagram.com/lethalcrysis_/p/DdoPGAPiCw2/) | 23 sep 2026 | Publicación fotográfica | Agradece recepción de Bielsa y acredita colaboración y equipo | 47K likes; 480 comentarios |
| [Lanzamiento de Bielsa](https://www.instagram.com/lethalcrysis_/reel/Ddg_KFqoM_o/) | 20 sep 2026 | Reel | Presenta la historia del exilio y la ruta | 9,500 likes; 238 comentarios |
| [The X-Trails](https://www.instagram.com/lethalcrysis_/p/Dc_p8l0CJuj/) | 7 sep 2026 | Publicación fotográfica | Publicidad declarada de Nissan y cuatro reportajes de España | 11K likes; 32 comentarios |

La grilla muestra 12 entradas entre 20 de mayo y 23 de septiembre: siete `/reel/` y cinco `/p/`, con una colaboración cuya ruta es del creador Melerus. 12/127 × 7 = **0.66 piezas/semana dentro de la muestra**; once propias en ese mismo tramo, 0.61. El Reel de Bielsa coincide con el estreno del largo; tres días después aparece una publicación de respuesta y agradecimiento. Se observa una secuencia estreno → conversación y reconocimiento del equipo.

### Oportunidad para un nuevo canal — inferencia

Adoptar el enfoque humano en una escala factible: acompañar un oficio, una comunidad o una ruta local con un protagonista. La singularidad de acceso puede reemplazar viajar lejos. Necesita investigación, permisos adecuados y capacidad de explicar contexto; no conviene adoptar duración de 40–80 min hasta validar que la historia sostiene esa extensión. Probar un mini documental de 12–18 min sería un experimento de producción, no una duración “óptima” demostrada por esta muestra.

## Hallazgos que sí pueden convertirse en pruebas

1. **Una necesidad por episodio.** Probar tres promesas sobre el mismo viaje: resolver una decisión, experimentar algo curioso y conocer a una persona. Comparar alcance a igual edad de publicación dentro del propio canal; las vistas absolutas de estos referentes no deciden el ganador.
2. **Tres sistemas visuales posibles.** Destino + texto útil (Alan), rostro + evidencia (Luisito), personas + acceso (Lethal). Crear bocetos propios usando imágenes realmente obtenidas durante el viaje. La elección debe corresponder al interés del video, no a una moda asumida.
3. **Separar rodaje y publicación.** La descripción de Egipto prueba que un viaje se puede publicar meses después. Registrar fechas, mantener datos útiles actualizados y guardar piezas cortas para cada estreno.
4. **Instagram necesita una función.** En las nueve publicaciones verificadas aparece anuncio del largo, recuerdos fotográficos, colaboraciones, acceso a personas, agradecimiento y publicidad declarada. No se demuestra conversión desde Instagram a YouTube; esa medición requeriría datos propios.
5. **Cadencia viable.** El muestreo muestra tres ritmos distintos. Un canal nuevo puede elegir uno según capacidad real y medir consistencia, costos y reservas de contenido. La muestra no prueba que publicar más sea siempre mejor.

## Shorts: presencia y muestra independiente

Se verificó la pestaña pública Shorts de los tres canales el 6 de octubre de 2026. En cada una se observaron 48 tarjetas iniciales, que **no equivalen al total del canal**. Se seleccionaron las primeras tres del orden por defecto y se consultó su metadato público `watch` para fecha, duración y vistas exactas. Los nueve registros tienen `isShortsEligible=true`. Esta muestra confirma presencia de Shorts; no constituye un barrido del historial ni se incorpora a las frecuencias de videos largos.

| Canal | Short | Fecha CDMX | Vistas capturadas | Duración |
|---|---|---|---:|---:|
| Alan por el mundo | [Perfecta excursión desde Londres. #alanxelmundo #axmegipto #turismo #hamptoncourt](https://www.youtube.com/shorts/ed3KX8DoE54) | 2026-09-27 | 15,596 | 2:13 |
| Alan por el mundo | [tomando fotos en #panama #alanxelmundo #travel #turismo](https://www.youtube.com/shorts/272kgAGYR6k) | 2026-09-23 | 23,808 | 1:10 |
| Alan por el mundo | [el turismo de gorilas en #Ruanda un caso de éxito digno de replicar. #axm #axmruanda](https://www.youtube.com/shorts/CQzS5Ts2kaI) | 2026-09-22 | 7,032 | 1:16 |
| Luisito Comunica | [Una pequeña broma en japonés 🇯🇵🍉🤪](https://www.youtube.com/shorts/sB7_12URgFU) | 2026-04-11 | 1,076,285 | 0:53 |
| Luisito Comunica | [El escándalo de los monjes budistas que está sacudiendo a Tailandia 🇹🇭](https://www.youtube.com/shorts/NVGFlt_yMTk) | 2025-07-19 | 734,712 | 1:48 |
| Luisito Comunica | [Los nuevos Crocs de Luisillo El Gordillo 🤩👌🏽🔥](https://www.youtube.com/shorts/nkL0v0Pm4SQ) | 2025-07-16 | 686,073 | 2:46 |
| Lethal Crysis | [Así es una MINA EN ÁFRICA](https://www.youtube.com/shorts/BnWJ4GqORRQ) | 2026-06-29 | 19,374 | 1:20 |
| Lethal Crysis | [¿A qué sabe la CARNE y LECHE DE CAMELLO?](https://www.youtube.com/shorts/uuOw1dCdyb4) | 2026-06-27 | 30,959 | 1:02 |
| Lethal Crysis | [La Isla más Densamente Poblada del Mundo](https://www.youtube.com/shorts/TgPtrDUrCMU) | 2026-06-24 | 16,782 | 2:06 |

Fuentes de las grillas: [Alan](https://www.youtube.com/@alanxelmundo/shorts), [Luisito](https://www.youtube.com/@luisitocomunica/shorts) y [Lethal](https://www.youtube.com/@lethalcrysis/shorts). Los enlaces de cada clip permiten revisar el metadato; [01_shorts.json](01_shorts.json) conserva registros y hora de consulta.

**Observación:** los primeros tres de Alan muestran excursión, fotografía y turismo de gorilas con fechas de septiembre; los de Luisito abarcan humor en Japón, un tema de Tailandia y una colaboración de producto, con fechas de abril de 2026 y julio de 2025; los de Lethal presentan mina, comida de camello y densidad insular, todos de junio de 2026. Presencia de Shorts no implica que el canal mantenga una actividad corta reciente.

**Inferencia para el canal nuevo:** un Short puede cubrir una sola curiosidad, decisión o momento humano. Conviene medir su desempeño por separado del largo y verificar si genera visitas al canal con datos propios. Las cifras aquí no prueban que los Shorts conviertan a espectadores de videos largos ni que la menor actividad corta perjudique su alcance. No se calculó frecuencia de Shorts con sólo tres piezas; tampoco se inspeccionaron completos los nueve clips.

## Evidencia y límites

- [Hoja de nueve miniaturas inspeccionadas](evidencia_grandes/miniaturas_9_referentes.jpg), con identificadores de video; imágenes obtenidas de las URLs que YouTube presenta en la grilla del canal.
- Por canal: `{handle}_channel.json` conserva 30 piezas de la grilla; `{handle}_watch.json` conserva los ocho registros primarios y hora de consulta. `resumen_metricas.json` conserva cálculos. [Publicaciones de Instagram](evidencia_grandes/instagram_posts.json) conserva los nueve metadatos consultados; [grillas del navegador](00_instagram_grandes_grids.json) conserva URLs y texto de accesibilidad de las 36 entradas. Las descripciones automáticas “May be an image...” no se trataron como inspección visual.
- YouTube puede mostrar variaciones de título por superficie. El 6 de octubre el mismo video de pirámides tenía “Visité el interior...” en `/videos` y “Conocí las pirámides...” en el metadato del reproductor. No se infiere que sea un experimento A/B, ni edición definitiva.
- Algunos agregadores mostraban fechas del día siguiente por zona horaria, cifras viejas, “última publicación” contradictoria o mezclaban Shorts con largos. Se descartaron de los cálculos finales. En particular, la fecha local de Alejandría es 25 de septiembre, Dendera 18 de septiembre y Abu Simbel 31 de julio, aunque índices secundarios señalaban el día siguiente.
- La frecuencia de Instagram es una muestra de las 12 entradas visibles, no un barrido completo de fechas fijo. Su rate incluye colaboraciones sólo donde se indica. Fotografías pueden ser carruseles; no se inspeccionaron todas sus diapositivas. Las cuentas no proporcionaron métricas de vistas de Reels fiables en el HTML público utilizado.
- No se tienen CTR, impresiones, retención, fuentes de tráfico, guardados, conversiones, ingresos, presupuesto, composición demográfica ni tasas de patrocinio. No se estimaron. No se atribuyó desempeño a la miniatura sin prueba causal y no se compararon videos de edades diferentes como si fueran equivalentes.
