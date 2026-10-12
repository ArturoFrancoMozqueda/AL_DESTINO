# Benchmark 03: aventura, exploración y utilidad para viajar

**Corte: 6 de octubre de 2026, México.** Investigación primaria de Clavero, Ramilla de Aventura y Molaviajar. Se consultaron los canales, páginas de vídeo y metadatos públicos de Instagram sin sesión. Se inspeccionaron visualmente nueve miniaturas, tres por creador. No se vieron completos los 24 vídeos: los análisis de narración se apoyan en títulos, descripciones y capítulos y se marcan como inferencias cuando corresponde.

**Método auditable.** La pestaña Videos se confirmó en orden “Más recientes” en `ytInitialData`. Se seleccionaron sus ocho primeras fichas; cada página watch permitió verificar título, fecha de publicación, vistas y duración desde `ytInitialPlayerResponse`. Hay HTML/JSON fuente en `investigacion/evidencia/`, además del script `extract_aventura.py` y la lámina `miniaturas_aventura.jpg`. Las vistas cambian y representan el contador público de esta captura, no el rendimiento a una misma edad. Se usa la duración del reproductor; las tarjetas a veces redondean un segundo. Suscriptores y total de publicaciones son cifras públicas redondeadas. No se calculan CTR, retención, impresiones, ingresos ni conversiones; esos datos no están disponibles públicamente.

## 1. Clavero: expedición condensada y una pregunta fuerte

**Identidad primaria.** [YouTube @Clavero](https://www.youtube.com/@Clavero/videos), canal UCQmGdB07nnkyvXbjkigkKtA, 2.8 millones de suscriptores y 231 vídeos declarados. El JSON-LD del canal enlaza `sameAs` a [Instagram @hiclavero](https://www.instagram.com/hiclavero/) y su canal secundario HiClavero. Instagram identifica a Pau Clavero y muestra aproximadamente 807 mil seguidores y 229 posts. Estos vínculos distinguen al autor de cuentas de fans como `hi.clavero`.

### Muestra de ocho vídeos

| Vídeo (fuente primaria) | Publicación | Vistas al corte | Duración |
|---|---:|---:|---:|
| [Exploré la Casa Más PARANORMAL de Estados Unidos](https://www.youtube.com/watch?v=QYfXqSxW20s) | 2024-12-28 | 4,197,475 | 0:37:16 |
| [Así Crucé Indonesia con solo 5 Euros (+1200km)](https://www.youtube.com/watch?v=-114h33L9AE) | 2024-06-18 | 2,047,535 | 0:24:43 |
| [La Oscura Realidad de Corea del Sur](https://www.youtube.com/watch?v=iFCZcHjJ8Cs) | 2024-04-25 | 5,030,666 | 0:24:55 |
| [Así es el Barrio Flotante más Peligroso del Mundo](https://www.youtube.com/watch?v=tM77WlEGhgI) | 2024-02-01 | 4,117,311 | 0:19:16 |
| [24 Horas Conduciendo en Línea Recta ¿Dónde Acabaré?](https://www.youtube.com/watch?v=RSkgP7AHjyk) | 2023-11-04 | 6,534,469 | 0:20:45 |
| [Así es la Ciudad Vertedero de Egipto](https://www.youtube.com/watch?v=iWCdhQ-eFXQ) | 2023-08-22 | 1,956,135 | 0:17:53 |
| [La Ciudad Tóxica de Estados Unidos que Todos Ignoran](https://www.youtube.com/watch?v=4SCOKD4MYf0) | 2023-07-13 | 3,889,364 | 0:17:38 |
| [Así Viven en los Túneles de Las Vegas, La Ciudad Oculta](https://www.youtube.com/watch?v=GCJDd4QrNDU) | 2023-06-10 | 5,137,837 | 0:23:04 |

**Cadencia observada.** Entre las ocho publicaciones los intervalos son 193, 54, 84, 89, 74, 40 y 33 días: mediana 74, media 81. La última publicación pública visible en Videos es del 28 de diciembre de 2024, 647 días antes del corte. Esta frecuencia corresponde al canal principal y a vídeos públicos largos: no demuestra que el creador dejara de publicar en su canal secundario, Reels o Shorts. Clavero es un referente de packaging, pero una cadencia pasada de un gran canal no es una receta de lanzamiento.

**Duración.** Mediana 21:54.5; rango 17:38–37:16. Siete de ocho piezas duran aproximadamente entre 18 y 25 minutos; la mansión es la excepción larga. Esto permite estudiar un arco de aventura relativamente compacto, sin asumir que esos minutos sean óptimos para otro canal.

**Contenido y promesa observados.** Cinco títulos presentan una realidad excepcional o escondida: Corea, Makoko, ciudad vertedero, Salton Sea y túneles de Las Vegas. Dos construyen una misión cuantificable: Indonesia por cinco euros y conducir 24 horas. Otro utiliza exploración paranormal. La descripción de Indonesia anticipa dificultades y una llegada a un supuesto paraíso; la de conducir integra combustible y peajes. Las descripciones de Egipto y Las Vegas contrastan turismo o superficie con otra forma de vivir. Son señales de una aventura con conflicto y contexto, aunque no se comprobó cómo se resuelve cada arco en pantalla.

**Títulos.** Patrones transferibles: `Así [acción] con solo [recurso limitado] (+[escala])`, `24 horas [regla del reto] ¿[resultado pendiente]?`, `Así viven en [espacio inesperado]`, `La [realidad] de [lugar conocido]`. Las cantidades permiten entender la regla sin conocer al autor. “Oscura”, “tóxica” y “peligroso” aumentan la tensión: un canal nuevo debería utilizarlos sólo cuando la evidencia del vídeo los justifique y no convertir pobreza o comunidades en un decorado sensacionalista.

**Miniaturas inspeccionadas (3).**

- [Mansión Winchester](https://www.youtube.com/watch?v=QYfXqSxW20s): casa victoriana nocturna a izquierda, luna, rostro grande a derecha y medidor en la mano. Sin frase larga; objeto y atmósfera explican la promesa paranormal.
- [Indonesia](https://www.youtube.com/watch?v=-114h33L9AE): protagonista haciendo autostop, carretera y señales verdes con destinos/distancias. La dirección de la ruta y el gesto cuentan la misión antes de leer el título.
- [Corea](https://www.youtube.com/watch?v=iFCZcHjJ8Cs): rostro a izquierda, calle nocturna roja y cintas amarillas de peligro. Contraste cromático e información ambiental; sin bloque explicativo de texto.

En esta muestra las tres usan rostro identificable, escenario específico y un elemento de prueba; el título proporciona el concepto. La imagen no repite una frase completa del título. Es una observación de tres diseños, no una regla universal del canal ni una medición del CTR.

**Modelo de negocio observado en descripciones.** Hay enlaces de campañas con Revolut, un portátil HP OMEN y la tienda de café Beanywood. Esto evidencia diversificación comercial, pero no cuánto gana el canal. La promoción bancaria aparece actualizada en varios vídeos antiguos; fecha de publicación y vigencia de la oferta no deben confundirse.

**Hipótesis para un nuevo canal.** Tomar la regla narrativa, no el coste de producción: una expedición accesible en México con destino, limitación de dinero/tiempo y resultado que haya que descubrir. Abrir con la regla y el problema; documentar obstáculos reales; aportar prueba de gasto y una llegada. Es un diseño propuesto, no una afirmación de que todos sus vídeos empleen esta secuencia.

### Instagram

Feed abierto por el navegador público del equipo y metadatos de posts corroborados por HTML canónico. El grid mostró contenido de 2022–2026 intercalado: no constituye una secuencia cronológica fiable, por lo que **frecuencia ND**. Se verificaron tres piezas de 2026 y una adicional de 2025:

| Pieza primaria | Fecha | Caption / formato observado | Likes / comentarios |
|---|---|---|---:|
| [Reel de campaña en viaje](https://www.instagram.com/hiclavero/reel/Dd6mQOLICVf/) | 2026-09-30 | Declara publicidad de Google Pixel; habla de capturar ideas durante el viaje. El alt del grid identifica montaña y texto; no se reprodujo completo. | 16K / 81 |
| [Recuerdo de serie en Estados Unidos](https://www.instagram.com/p/DbEFww8CAoe/) | 2026-07-21 | Foto/post de recap y agradecimiento por apoyo; menciona una serie mensual en Estados Unidos. No prueba que fuese publicada en el canal principal. | 125K / 1,019 |
| [China y nuevas gorras](https://www.instagram.com/p/DXKI2zaCKXl/) | 2026-04-15 | Dump de viaje a China asociado a producto propio de Beanywood. | 70K / 408 |
| [Recap de mes y camisetas](https://www.instagram.com/p/DMvNKLBsNoC/) | 2025-07-30 | Resumen personal y agradecimiento por camisetas agotadas, según declara el autor. | 100K / 827 |

**Hallazgo:** Instagram conserva actividad reciente aunque Videos del canal principal no muestre largos recientes. Los captions combinan recuerdo de la experiencia, relación con la comunidad y producto/campaña. La función comercial se observa directamente, pero no se atribuye alcance, ventas o cuota de contenido promocionado sobre toda la cuenta. Los contadores K son redondeados por Instagram.

## 2. Ramilla de Aventura: el trayecto es la historia

**Identidad primaria.** [YouTube @ramilladeaventura](https://www.youtube.com/@ramilladeaventura/videos), UCyPaCXX5RPYa0Q-eE_gGDug, 742 mil suscriptores y 355 vídeos. El canal se presenta mediante destinos curiosos, remotos y extremos. Sus descripciones enlazan [@ramilladeaventura](https://www.instagram.com/ramilladeaventura/). La descripción del vídeo del Pamir anuncia expresamente un nuevo Instagram: [@soyramilladeaventura](https://www.instagram.com/soyramilladeaventura/). El nuevo perfil dice que es respaldo del anterior y muestra 8,320 seguidores y nueve posts en la captura. El antiguo no entregó una biografía verificable mediante HTML público. No mezclar sus conteos ni interpretar un cambio de cuenta como crecimiento/caída del creador.

### Muestra de ocho vídeos

| Vídeo (fuente primaria) | Publicación | Vistas al corte | Duración |
|---|---:|---:|---:|
| [Recorrimos la LEGENDARIA Carretera del Pamir](https://www.youtube.com/watch?v=Z4f-NCCXhEw) | 2026-09-21 | 481,634 | 2:36:29 |
| [Probé el Último Tren Soviético de Europa](https://www.youtube.com/watch?v=Nz8e8RwMAKo) | 2026-07-27 | 342,793 | 0:49:05 |
| [Fui a mi 100º País!](https://www.youtube.com/watch?v=DtQqi9CKWsk) | 2026-07-16 | 202,006 | 1:40:43 |
| [Fui a Taiwan: ¿Es Realmente un País?](https://www.youtube.com/watch?v=aNiw3-ToJ5Q) | 2026-06-24 | 382,018 | 1:08:44 |
| [Hice el Viaje en Bus Más Largo del Mundo](https://www.youtube.com/watch?v=1i6hWxpm3a8) | 2026-06-01 | 1,123,066 | 1:19:40 |
| [Cómo Visité las 7 Maravillas del Mundo en 7 Días](https://www.youtube.com/watch?v=fRkL7cI4tzQ) | 2026-05-24 | 394,869 | 1:59:24 |
| [Probé el Vuelo de Primera Clase Más Lujoso del Mundo](https://www.youtube.com/watch?v=vKxX0BWHQuM) | 2026-05-17 | 1,000,673 | 0:50:16 |
| [Visité la Afición Más Ruidosa del Mundo](https://www.youtube.com/watch?v=iVRmgRyRLXY) | 2026-05-12 | 143,075 | 0:40:44 |

**Cadencia observada.** Ocho vídeos entre 12 de mayo y 21 de septiembre de 2026, 132 días entre primero y último. Intervalos consecutivos: 56, 11, 22, 23, 8, 7 y 5 días; mediana 11, media 18.86. En mayo hay un bloque de cuatro publicaciones en doce días; después aparecen pausas largas. No equivale a una entrega fija semanal. La última publicación tiene 15 días de antigüedad. Esta muestra se debe entender como una temporada de piezas extensas con cadencia variable.

**Duración.** Mediana 74:12, mínimo 40:44, máximo 2:36:29. Cinco de ocho superan una hora. A diferencia de Clavero, aquí se observa una apuesta por episodios largos que incorporan el viaje y su contexto; no hay evidencia pública de que mayor duración cause más alcance.

**Pilares observados.** Transporte extraordinario (bus, tren soviético, primera clase); expediciones y reglas de reto (Pamir, siete maravillas en siete días); geopolítica de destino (Taiwán); biografía viajera (país 100); cultura de eventos (afición de fútbol). El núcleo que une títulos heterogéneos es “viví personalmente una experiencia difícil de acceder”.

**Narración comprobable en capítulos.** [País 100](https://www.youtube.com/watch?v=DtQqi9CKWsk) comienza con el hito, pasa al viaje a Arabia Saudí, explica cuántos países hay, prueba trenes, explora Jeddah, repasa el recorrido personal, cambios del país, preguntas frecuentes, fútbol y valoraciones. Se alternan experiencia y explicación. La descripción del bus fija el recorrido Río de Janeiro–Lima, 6,300 kilómetros y casi una semana. La del Pamir nombra el eje Tayikistán–Kirguistán y fronteras vecinas. Esas coordenadas aportan escala y un itinerario reconocible.

**Reutilización observada.** El resumen de las siete maravillas enlaza una lista de reproducción de la serie por días: [serie](https://www.youtube.com/playlist?list=PLh_3mQhWDFpIYeuQJ1kMjlsp0Du9GGdpW). Existe así una unidad de viaje explotada como entregas y como pieza completa; esto es evidencia de arquitectura de catálogo, sin afirmar que las piezas tengan idéntico montaje.

**Títulos.** Predominan verbo de experiencia en primera persona + singularidad: `Probé el último...`, `Hice el viaje ... más largo`, `Visité la afición ... más ruidosa`. Cinco de ocho incorporan último, legendaria, maravillas o un superlativo; el reto 7/7 incorpora regla memorable y el país 100 depende más de la relación con el autor. Para un canal sin audiencia propia, una consecuencia clara para el espectador o una dificultad entendible probablemente sea más transferible que un aniversario personal: hipótesis de adquisición.

**Miniaturas inspeccionadas (3).**

- [Pamir](https://www.youtube.com/watch?v=Z4f-NCCXhEw): autor junto al vehículo y carretera montañosa, carteles azules de países/fronteras, polvo y sensación de desnivel. Elementos ambientales explican escala sin frase extensa.
- [Tren soviético](https://www.youtube.com/watch?v=Nz8e8RwMAKo): rostro/mochila a izquierda, locomotora roja a derecha y texto breve “14 horas”. La imagen entrega la duración del trayecto mientras el título entrega su singularidad histórica.
- [País 100](https://www.youtube.com/watch?v=DtQqi9CKWsk): selfie con libreta marcada 94–100, casillas de países completados y destino número 100 difuminado. Convierte el hito en progresión visible y reserva la revelación del destino.

Las tres tienen un protagonista cercano y un artefacto que acredita viaje (cartel, tren, libreta). Son imágenes compuestas/seleccionadas; no se afirma que cada elemento sea una fotografía documental sin edición.

**Señales de resultados.** En la muestra, bus y primera clase rondan o superan el millón de vistas; la afición ronda 143 mil. Los temas, edad y difusión difieren. La diferencia sugiere candidatos para investigar —transporte accesible como curiosidad versus un evento especializado—, pero no prueba una causa. El Pamir ya ronda 482 mil con 15 días y no debe compararse sin corrección de antigüedad a publicaciones de mayo.

**Monetización observada.** Descripciones con membresías, códigos/enlaces Holafly y campañas de Trade Republic/BYD. Las marcas y ofertas se describen como evidencia comercial histórica, no recomendaciones financieras o de compra.

**Hipótesis transferible.** Convertir un desplazamiento asequible en la misión principal: “crucé [región] sólo con [transporte/regla]”. Una serie puede llevar miniepisodios por tramo, una conclusión completa y clips verticales de incidentes que se entiendan solos. Empezar con piezas más cortas hasta comprobar recursos editoriales y respuesta del público; las duraciones del referente no son una obligación.

### Instagram

Feed abierto por navegador público y corroborado con páginas canónicas. Se identificaron cuatro Reels propios consecutivos del perfil de respaldo:

| Pieza primaria | Fecha | Tema declarado en caption | Likes / comentarios |
|---|---|---|---:|
| [Día 3 en Kilimanjaro](https://www.instagram.com/soyramilladeaventura/reel/DeJhV0cRa6m/) | 2026-10-06 | Tercera entrega del ascenso; alt de camping y exterior | 687 / 15 |
| [Día 2 en Kilimanjaro](https://www.instagram.com/soyramilladeaventura/reel/DeHuNYuRtJ8/) | 2026-10-05 | Segunda entrega del ascenso | 1,067 / 19 |
| [Día 1 en Kilimanjaro](https://www.instagram.com/soyramilladeaventura/reel/DeDwNsaIpVr/) | 2026-10-03 | Primera entrega del ascenso | 1,212 / 18 |
| [Helicóptero sobre Kilimanjaro](https://www.instagram.com/soyramilladeaventura/reel/Dd9qEK1NN5G/) | 2026-10-01 | Experiencia previa asociada al mismo destino | 2,055 / 33 |

**Cadencia de este bloque:** cuatro Reels entre el 1 y 6 de octubre, gaps 2, 2 y 1 día; mediana dos días. Es un bloque de viaje activo en una cuenta nueva/de respaldo, no una frecuencia anual. El Reel del 6 de octubre tiene menos de un día: sus likes no se comparan directamente con el del día 1. El grid también incluye publicaciones de @elgranrally de septiembre como colaboraciones; se distinguieron de los posts propios. El patrón de “día 1/2/3” demuestra progresión episódica y un lugar concreto. Se comprobó caption y alt, no reproducción íntegra, edición ni audio. Stories no auditadas.

## 3. Molaviajar: ayudar a organizar el viaje y acompañarlo

**Identidad primaria.** [YouTube @molaviajar](https://www.youtube.com/@molaviajar/videos), UCz071p8TGbjk-spxWPT9CLw, 404 mil suscriptores y 721 vídeos. El canal enlaza directamente [Instagram @molaviajar](https://www.instagram.com/molaviajar/) y [sitio oficial](https://www.molaviajar.com/); Instagram identifica a Adri y Gosi, aproximadamente 274 mil seguidores y 2,131 posts. Su web integra vídeos, mapas y guías. No se trata exclusivamente de vlog personal: es un sistema de ayuda para planear viajes.

### Muestra de ocho vídeos

| Vídeo (fuente primaria) | Publicación | Vistas al corte | Duración |
|---|---:|---:|---:|
| [El hotel MÁS BARATO y MEJOR ubicado de Nueva York 🇺🇸 (sí existe). Guía New York MolaViajar](https://www.youtube.com/watch?v=4Z3DzorPMUM) | 2026-03-11 | 17,889 | 0:05:28 |
| [Vlog 3 Nueva York: Tienes que acabar el día así 😍 INCREÍBLE. Guía New York MolaViajar](https://www.youtube.com/watch?v=pI9DukCMNbc) | 2026-03-04 | 6,131 | 0:07:30 |
| [Vlog2: Rincones de NUEVA YORK poco conocidos. Guía Molaviajar](https://www.youtube.com/watch?v=zHg3PIErM3c) | 2026-02-25 | 6,782 | 0:07:20 |
| [Vlog: Llegada a NUEVA YORK, Aeropuerto, Taxi, Hotel y Central Park!! Guía Molaviajar](https://www.youtube.com/watch?v=pyXC2BmRvMc) | 2026-02-18 | 9,083 | 0:07:30 |
| [Subo a 5 Observatorios de Nueva York ¿Cual es el mejor? y como entrar a precio reducido. MolaViajar](https://www.youtube.com/watch?v=E1LefXt8EnY) | 2026-02-11 | 11,341 | 0:11:32 |
| [Regalamos 2 VIAJES a Nueva York🗽y Sorpresa🎁!!!](https://www.youtube.com/watch?v=T8rWvsQuEt8) | 2025-04-06 | 6,244 | 0:01:56 |
| [Propina en Estados Unidos. ¿Cómo funciona? Explicación detallada y cuidado con esto. Guía Nueva York](https://www.youtube.com/watch?v=Bu9VTAYO7MQ) | 2025-03-06 | 10,885 | 0:02:27 |
| [Ruta 14 horas en Nueva York con pase GO CITY y ahorrar 400$ en 1 día. Reto INCREIBLE de MolaViajar.](https://www.youtube.com/watch?v=mK6p4jFSNys) | 2025-02-27 | 38,267 | 0:25:11 |

**Cadencia observada.** Cinco vídeos consecutivos publicados cada siete días, del 11 de febrero al 11 de marzo de 2026. El antecedente público en la muestra es el 6 de abril de 2025: un intervalo de 311 días. La mediana de los siete gaps es siete días, pero la media es 53.86 por las pausas; comunicar sólo la mediana “semanal” sería engañoso. No hay nuevas publicaciones largas visibles después del 11 de marzo (209 días al corte) en la respuesta del canal ordenada por recientes. Esto no descarta actividad por Shorts, Instagram o el blog.

**Duración.** Mediana 7:25; rango 1:56–25:11. Los tres vlogs recientes duran 7:20–7:30; tutorial y review suelen tener una pregunta concreta. Se diferencia de los documentales largos: una necesidad del viajero puede resolverse en pocos minutos y formar parte de una biblioteca.

**Formatos observados.** Review de hotel; serie de detrás de cámaras (Vlog 1/2/3); comparación de cinco observatorios; reto para amortizar pase; tutorial de propina; promoción/sorteo. Las descripciones de los vlogs declaran que son más caseros y muestran lo que hay tras las cámaras, manteniendo consejos. El resultado editorial es una mezcla deliberada de cercanía y utilidad, respaldada por lo que el autor afirma, no una valoración técnica del montaje.

**Títulos.** Utilidad + lugar + restricción: hotel económico y bien situado; cuál mirador elegir; cómo funciona la propina; ahorrar un importe en un día. Los títulos vlogs numerados aportan continuidad pero algunos esconden la situación detrás de “INCREÍBLE” y un número; para un creador desconocido conviene que el beneficio o dilema aparezca primero. “Nueva York” se repite y “Guía New York MolaViajar” actúa como sello de serie, con títulos extensos.

**Miniaturas inspeccionadas (3).**

- [Hotel](https://www.youtube.com/watch?v=4Z3DzorPMUM): selfie dentro de la habitación; bloques grandes amarillos, rojos y blancos, skyline pequeño y flechas. Promesas visibles de ahorro y ubicación, con el gesto del autor como reacción.
- [Vlog 3](https://www.youtube.com/watch?v=pI9DukCMNbc): composición del protagonista con skyline y luces, centro dominado por “VLOG 3”, subtítulo “ACABA EL DÍA ASÍ EN NEW YORK”. Prima la continuidad del catálogo y la experiencia de la tarde.
- [Vlog 2](https://www.youtube.com/watch?v=zHg3PIErM3c): protagonista, edificios de Manhattan y escena con personaje Superman, “VLOG 2” muy grande y “NO EMPIEZO ANIMADO EL DÍA”. Anticipa estado emocional y recorrido, con muchos elementos simultáneos.

El diseño es más textual y denso que las seis miniaturas vistas de los otros dos. Hipótesis práctica: usar una pregunta económica y una prueba visible, pero reducir texto y objetos para el tamaño móvil. No hay CTR para decidir cuál diseño funciona mejor.

**Señales de resultados en contexto.** Los tres vlogs de febrero/marzo registran aproximadamente 6.1k–9.1k vistas; hotel, aproximadamente 17.9k. El reto Go City de 2025 supera 38k. La utilidad explícita podría alcanzar a quien todavía no conoce al autor, pero las diferencias de antigüedad impiden tratarlo como demostración causal. Esto motiva un experimento con títulos claros, no una condena al formato vlog.

**Integración comercial observada.** Descripciones con hoteles afiliados, pases, seguros, eSIM, tarjetas, libros y un PDF de alojamientos. El sitio enlaza vídeos con itinerarios y guías impresas; la compra se inserta en una tarea de planificación. La llamada a escribir dudas por WhatsApp/email evidencia servicio y comunidad. No se estiman conversiones ni ventas.

### Instagram: cuatro piezas primarias con fecha

La página propia [Nueva York en 7 días](https://www.molaviajar.com/nueva-york-en-7-dias/) enlaza por tema varias piezas Instagram y acredita que son parte de su catálogo. Las páginas públicas de los posts ofrecen caption, fecha y contadores por HTML, aunque el navegador de búsqueda restringió la reproducción. Se analizó el texto; no se afirma haber visto completo su montaje ni su audio.

| Post/Reel y URL | Fecha | Tema/papel observado | Likes / comentarios públicos |
|---|---|---|---:|
| [Ferry y skyline sin gente](https://www.instagram.com/molaviajar/reel/DXbrp33oIM2/) | 2026-04-22 | Microconsejo de dónde colocarse; pregunta por experiencia de seguidores | 4,080 / 75 |
| [Brooklyn Heights](https://www.instagram.com/molaviajar/reel/DMsBAXvo6eB/) | 2025-07-29 | Recomendación de paseo + referencia a caja de rutas en tienda/Amazon | 1,836 / 79 |
| [Tiempo para cruzar puente de Brooklyn](https://www.instagram.com/molaviajar/reel/DJjUPdJolzP/) | 2025-05-12 | Pregunta concreta y escala de 1.8 km; invita a comparar tiempos | 5,298 / 110 |
| [Aplicación al entrar a Estados Unidos](https://www.instagram.com/p/DTu8x0uCDbs/) | 2026-01-20 | Experiencia práctica y aclaración en caption; tutorial enlazado desde vlog largo | 9,599 / 519 |

**Frecuencia Instagram ND.** Es una muestra intencional de utilidad, de fechas no consecutivas; calcular frecuencia entre ellas sería incorrecto. **Conexión plataformas observada:** el vlog de llegada de febrero enlaza el tutorial Instagram de enero; la web organiza Reels por zona y actividad. Es evidencia de circulación bidireccional y de contenido vertical con una pregunta que se entiende sola.

## Comparación para la estrategia del nuevo canal

| Dimensión | Clavero | Ramilla | Molaviajar | Decisión experimental para lanzamiento |
|---|---|---|---|---|
| Puerta de entrada | Realidad oculta o reto | Experiencia extrema de viaje/transporte | Problema práctico al viajar | Elegir una promesa principal por vídeo |
| Escala de pieza en muestra | Mediana ~22 min | Mediana ~74 min | Mediana ~7.5 min | Planear 12–20 min de historia + clips útiles; ajustar tras datos propios |
| Motor de curiosidad | Qué hay detrás / dónde acabaré | Cómo es / cómo llego / cuánto aguanto | Qué elegir / cuánto cuesta / cómo hacerlo | Un dilema medible en un destino cercano |
| Miniaturas (3/canal) | Rostro + ambiente + objeto | Rostro + ruta/vehículo/progreso | Texto fuerte + rostro + contexto | Un sujeto, una prueba y 0–4 palabras como hipótesis inicial |
| Catálogo | Reportajes autocontenidos | Misiones y series + resumen | Biblioteca de guías y serie cotidiana | Combinar episodios autónomos con playlists por ruta |
| Recursos complementarios | Enlaces y producto propio | Membresía y sponsors | PDF, mapas, guías, consultas, afiliación | Publicar presupuesto/itinerario útil y enlaces transparentes |

**Experimentos propuestos, sin promesa de crecimiento.** (1) Viaje cercano con dinero o tiempo limitado: comparar dos encuadres de título —regla del reto versus problema de presupuesto— usando herramientas del propio canal. (2) Un vídeo orientado a decisiones y otro a aventura del mismo destino, manteniendo calidad y fechas comparables; revisar impresiones, CTR, retención de primeros 30 segundos y fuentes de tráfico en Studio propio, si hay volumen suficiente. (3) Tres clips verticales por experiencia: una dificultad, un coste y un consejo; cada uno debe aportar valor autónomo y enlazar a una pieza relacionada. (4) Revisar 28 días después con vistas a igual edad, suscripciones por mil vistas y coste/horas de producción. Los ejemplos muestran patrones de oferta y packaging; no justifican universalizar números de grandes creadores.

**Límites materiales.** Selección de ocho vídeos recientes por canal, no censo de histórico. Los ocho recientes de Clavero abarcan 2023–2024 y los de Molaviajar mezclan dos bloques temporales, consecuencia real del catálogo observado. Tres miniaturas por canal. Se corroboraron 12 piezas Instagram (cuatro por creador), con captions/fechas y las muestras de grid del navegador del equipo. No se vieron completos los vídeos ni los Reels. Instagram puede pedir login, no lista todos los posts en HTML y cambia disponibilidad; Stories no se auditaron. Fechas de publicación son del reproductor, no fechas de rodaje. Vistas son de esta captura y no pronóstico. Las conclusiones sobre causas de rendimiento están deliberadamente formuladas como hipótesis.


## Comprobación adicional: YouTube Shorts separado de vídeos largos

Se consultó la pestaña pública Shorts el 6 de octubre de 2026. Se extrajeron las tres primeras fichas visibles por canal con pestaña disponible; fecha y vistas exactas se corroboraron en metadata del reproductor. Evidencia en `03_shorts.json` y HTML de las pestañas. No se reprodujeron completos los clips ni se inspeccionaron sus portadas.

**Clavero:** [ruta consultada](https://www.youtube.com/@clavero/shorts) devuelve Principal seleccionado y navegación sin pestaña Shorts. No hay muestra pública verificable del formato en este canal principal; esto no describe el secundario HiClavero.

| Canal | Short | Fecha | Vistas públicas | Duración |
|---|---|---|---:|---:|
| Ramilla | [Pusimos a prueba a la afición de Uruguay 🇺🇾 con Gemini](https://www.youtube.com/shorts/dlfGGHbix28) | 2026-07-01 | 15,338 | 63 s |
| Ramilla | [Siguiendo a LA SELECCIÓN desde la otra punta del mundo](https://www.youtube.com/shorts/CDAj3fGmbPg) | 2026-06-19 | 16,301 | 37 s |
| Ramilla | [el vuelo más lujoso del mundo!](https://www.youtube.com/shorts/i0Ma9ZDeBy8) | 2026-05-29 | 24,638 | 36 s |
| Molaviajar | [Tiendas temáticas que no te puedes perder en NY 🗽](https://www.youtube.com/shorts/Z5jIDcPaong) | 2026-09-30 | 5,411 | 61 s |
| Molaviajar | [Fans de Alicia en el País de las Maravillas 👧🐇🎩](https://www.youtube.com/shorts/tLJWokO-E_c) | 2026-09-27 | 9,622 | 27 s |
| Molaviajar | [Nuevo puzzle de 1.000 piezas del mapa del mundo 🧩](https://www.youtube.com/shorts/45yM12u0i4k) | 2026-09-23 | 2,740 | 75 s |

**Frecuencia por formato.** Las tres fichas de Molaviajar tienen intervalos de cuatro y tres días (23–30 septiembre), mediana 3.5 días en este bloque: su actividad vertical reciente continúa pese a la pausa de vídeos largos desde marzo. Ramilla muestra publicaciones de 29 de mayo, 19 de junio y 1 de julio, intervalos de 21 y 12 días, mediana 16.5 en esta pequeña muestra; no prueba cadencia anual ni elimina actividad más reciente en Instagram. Los conteos y hábitos de Shorts y largos se deben mantener separados.

**Contenido observado por títulos.** Molaviajar combina descubrimiento de tiendas y personajes con promoción de producto propio (puzzle); Ramilla combina fútbol y una experiencia de primera clase, tema que también tiene un vídeo largo de mayo. Esto muestra continuidad temática entre formatos, sin afirmar que sea un recorte idéntico ni que convierta espectadores a largos.
