# Benchmark: Misias pero Viajeras, Viajando con Vero, La Vida de Viaje y PlanetaJuan

Fecha de observación: **6 de octubre de 2026**, America/Mexico_City. Investigación de cuatro identidades distintas, con YouTube e Instagram vinculados desde sus fuentes propias. Viajando con Vero reemplaza la identificación no verificada «Viajando con Vero y Alex»: el canal verificado pertenece a Verónica Weffer. Misias y La Vida de Viaje son referencias **históricas** en YouTube; no deben contarse como canales activos de 2026.

## Método y límites

Se consultaron buscador web, páginas de los creadores y HTML público de las pestañas Videos de YouTube, sin sesión ni métricas privadas. Para cada canal se capturaron sus ocho primeras entradas de la pestaña Videos. De la página pública individual se extrajeron título, autor, descripción, fecha de publicación y contador de reproducciones desde `ytInitialPlayerResponse`; la duración de la tarjeta se conserva tal como se mostró. No se usaron APIs privadas, proyecciones de ingresos de agregadores ni supuestos sobre CTR/retención. El JSON adjunto conserva descripciones y URLs de miniatura para auditar el análisis.

Las vistas son una **fotografía acumulada al consultar**, cambian continuamente y los videos tienen edades distintas. No prueban que un título, miniatura o destino cause más reproducciones. Esta muestra privilegia actualidad de publicación y no es aleatoria ni permite afirmar la frecuencia anual. La frecuencia se calcula con fechas exactas entre primera y última entrada: `(n−1) × 7 / días entre publicaciones`. «ND» significa no determinado. La pestaña Videos excluye Shorts y transmisiones de otras pestañas; una pieza de un minuto aquí no implica que sea Short. No se vio el metraje completo: las observaciones de estructura se basan en descripciones, capítulos y secuencia de temas; no se inventan hooks visuales, montaje, audio o retención. La auditoría visual usa capturas Browser y, para dos canales, hojas de contacto de las miniaturas públicas originales. La muestra de Instagram usa URLs y fechas del grid Browser, verificadas con los metadatos públicos de cada publicación seleccionada. No se infiere la imagen a partir de su texto alternativo automático.

## Comparación útil para un lanzamiento

| Canal | Situación verificada en YouTube | Identidad / promesa visible | Cadencia de la muestra | Duración de la muestra | Uso comercial visible |
|---|---|---|---|---|---|
| Misias pero viajeras | Cierre declarado 30-may-2025 | Viajar con utilidad económica; amigas peruanas | Siete videos viajeros 10-nov a 29-dic-2024: 0,86/semana; cierre separado | Viajes entre 10:02 y 30:12 | eSIM, seguro, tienda, redes personales; cierre dirige a canales individuales |
| Viajando con Vero | Activo, último 4-oct-2026 | Destinos + familia + experiencias emocionales | Ocho videos 10-sep a 4-oct-2026: 2,04/semana | 16:24–30:50; mediana por segundos 22:40 | En esta muestra el CTA visible se centra en comentar y acompañar la historia; otras piezas históricas cruzan a IG |
| La Vida de Viaje | Último video encontrado 12-jul-2024; anterior 29-sep-2021 | Movimiento lento, naturaleza, bici/kayak/casa rodante | Frecuencia actual ND; serie de julio 2021 combina episodios y trailers | Episodios 4:11–15:01; clips/trailers 0:56–1:45 | Blog, comunidad, embajadores; web ofrece libros y newsletter |
| PlanetaJuan | Activo, último 4-oct-2026 | Curiosidad cultural, expectativas vs realidad, encuentros locales | Ocho videos 2-sep a 4-oct-2026: 1,53/semana | 21:59–1:01:21; mediana 32:01,5 por segundos | Libros, eSIM, VPN, escuela de idiomas, membresía, IG |

Las dos referencias históricas enriquecen las opciones creativas, pero su tamaño y catálogo no equivalen a actividad actual. Un benchmark que no distingue esto podría recomendar una carga de producción que sus propios referentes dejaron de sostener.

## 1. Misias pero viajeras — utilidad práctica como marca

Fuentes de identidad: [YouTube oficial](https://www.youtube.com/@misiasperoviajeras/videos), [Instagram enlazado en sus descripciones](https://www.instagram.com/misiasperoviajeras/). La descripción de «Un mensaje importante» declara que el proyecto llega a su fin y deriva a [Fátima](https://youtube.com/@Fatima_Sotoma) y [Daniela](https://www.youtube.com/@danielaritacabrera). Este dato primario confirma el cierre anunciado en prensa. Las creadoras no se presentan como pareja sentimental; son una dupla de amigas.

### Muestra primaria

| Fecha de publicación | Video / enlace primario | Duración visible | Vistas observadas |
|---|---|---:|---:|
| 2025-05-30 | [Un mensaje importante ❤️‍🩹](https://www.youtube.com/watch?v=P9OQBl8NkEU) | 28:27 | 587 426 |
| 2024-12-29 | [Lo MEJOR de El Salvador 🇸🇻 · 10 actividades imperdibles 📝🌋🏄🏽‍♀️](https://www.youtube.com/watch?v=avYS1tpkZbc) | 26:20 | 179 366 |
| 2024-12-15 | [⏰ Primeras 24 horas en EL SALVADOR 🇸🇻 · Comida, qué hacer Y LA SEGURIDAD 📝](https://www.youtube.com/watch?v=na25oNB_LTg) | 29:11 | 284 396 |
| 2024-12-11 | [🇻🇪 Las 2 caras de LOS ROQUES: el MAGNATE ✨ vs el real 👊](https://www.youtube.com/watch?v=3dGh081aCOA) | 17:24 | 130 945 |
| 2024-12-01 | [¡FULL DAY EN MORROCOY 🇻🇪! Playas turquesas por US$20 🤑](https://www.youtube.com/watch?v=KEhZnDXlrxc) | 18:23 | 130 762 |
| 2024-11-25 | [HOTEL XCARET ARTE 2025 🇲🇽 · Mi hotel favorito del MUNDO 🔝 ¿Por qué lo es? 🤔](https://www.youtube.com/watch?v=K9Mv-fnHp7c) | 29:44 | 515 603 |
| 2024-11-17 | [VIAJÉ A OAXACA POR ESTO 🇲🇽](https://www.youtube.com/watch?v=VK7JIMP4NNE) | 30:12 | 102 593 |
| 2024-11-10 | [¡5 platos que SÍ O SÍ debes probar en tu viaje a México! 🇲🇽 · Peruana AMA comida mexicana 😋🌶️](https://www.youtube.com/watch?v=FDl4Au7ChhU) | 10:02 | 67 203 |

### Observaciones de contenido y empaque textual

La muestra combina guías de entrada («primeras 24 horas»), lista concreta («10 actividades»), comparación («magnate vs real»), precio explícito («US$20»), evaluación de hospedaje («mi hotel favorito») y gastronomía numerada («5 platos»). México, Venezuela y El Salvador generan siete entregas viajeras antes de la despedida. Hay una promesa verificable en el título que puede resolverse dentro del episodio, más allá de «nuestro viaje a X».

Los capítulos de El Salvador permiten revisar estructura sin simular visionado: llegada 0:46, costos de traslados 1:18, migraciones 2:56, aeropuerto a ciudad 4:27, alojamiento 5:34, mercado 6:20, comida 8:55, recorrido urbano, impresiones 22:45 y cierre 28:27. El segundo episodio reorganiza la experiencia como diez actividades, con puntos útiles entre 0:39 y 23:50 y enlaces de mapas. Es una misma zona convertida en dos intenciones de consumo: vivir la llegada y planear qué hacer.

Las descripciones distinguen **temporada de viaje** (noviembre 2024 en El Salvador) de fecha de publicación (diciembre 2024). Eso evita confundir la actualidad de un precio o condición de destino. Incluyen descuentos Holafly/IATI, suscripción, Instagram conjunto, perfiles personales y tienda propia. Se observa diversificación de enlaces comerciales; sus ingresos y conversiones son ND. Las menciones a puntos de venta pertenecen al texto histórico de esos videos, no prueban que los locales o tienda operen hoy.

### Frecuencia y desempeño con límites

Separando la despedida, siete videos viajeros abarcan 49 días (10-nov a 29-dic-2024): seis intervalos, 0,857 publicaciones por semana, mediana de intervalo 7,5 días; intervalos individuales de 4 a 14 días. El cierre llega 152 días después del último viaje de la muestra. No se recomienda promediar ambos periodos para presentar una frecuencia actual.

En esa muestra Xcaret reúne 515 603 vistas; primeras 24 horas en El Salvador, 284 396; la lista de actividades, 179 366. La diferencia sugiere temas para estudiar, no demuestra que hoteles o logística ganen siempre. Cada video acumula distinta antigüedad, interés del destino y distribución. Las vistas de la despedida se excluyen de comparación de temas viajeros.

### Hipótesis aplicables, por probar

Un nuevo canal puede distinguirse si transforma el presupuesto en un elemento recurrente: enseñar ticket/importe, contexto de temporada, decisión de ahorro y resultado. Un itinerario de dos episodios («llegar» y «hacer») puede abaratar investigación y grabación, siempre que cada entrega resuelva una pregunta nueva. Para una dupla, acordar responsabilidades, pausas y forma de continuar individualmente es una decisión de producción útil ante el cierre observado; no permite atribuir causas personales no publicadas.

Miniaturas e Instagram: verificados en las secciones de evidencia visual y multiplataforma al final. El grid incluye piezas antiguas en primeras posiciones; no representa por sí solo un orden cronológico completo.

## 2. Viajando con Vero — continuidad de personaje y contraste emocional

Fuentes: [YouTube oficial](https://www.youtube.com/@ViajandoconVero/videos), [Instagram](https://www.instagram.com/veronicaweffer/). El perfil de YouTube identifica a Verónica Weffer; videos anteriores enlazan ese Instagram con su nombre. No se encontró evidencia primaria de un proyecto «Vero y Alex».

### Muestra primaria

| Fecha de publicación | Video / enlace primario | Duración visible | Vistas observadas |
|---|---|---:|---:|
| 2026-10-04 | [DÍA DE PLAYA CON MIS HERMANAS EN VENEZUELA 🇻🇪☀️ 2026](https://www.youtube.com/watch?v=9PTISpiUuBc) | 19:02 | 422 266 |
| 2026-10-01 | [¿CUÁNTO CUESTA REALMENTE VIVIR EN VENEZUELA? 🇻🇪 😳](https://www.youtube.com/watch?v=sF67SexLMdA) | 27:55 | 351 354 |
| 2026-09-27 | [¿RENUNCIARÉ A MI SUEÑO? Por primera vez tengo miedo](https://www.youtube.com/watch?v=sqQsuD3VYVw) | 30:50 | 523 642 |
| 2026-09-24 | [ENTRÉ a la CASA de una TRIBU MASÁI 😳 · Lo que vi ADENTRO me IMPACTÓ](https://www.youtube.com/watch?v=T5AzvI9-hps) | 16:25 | 325 754 |
| 2026-09-20 | [ENTRÉ al SAFARI más SALVAJE de ÁFRICA 😱 · Masái Mara](https://www.youtube.com/watch?v=YRhKlxN1pAY) | 18:27 | 627 970 |
| 2026-09-17 | [ASÍ es la VIDA NOCTURNA en ÁFRICA 😳 · Lo que pasa en NAIROBI de noche 🇰🇪](https://www.youtube.com/watch?v=2p_RFRT6WpU) | 16:24 | 523 437 |
| 2026-09-13 | [ME ENAMORÉ EN ESTA ISLA DE ÁFRICA 😍 · ZANZÍBAR](https://www.youtube.com/watch?v=h543bByz13E) | 26:19 | 492 143 |
| 2026-09-10 | [EL PEOR VIAJE DE MI VIDA 😰 JAMÁS SENTÍ TANTO MIEDO](https://www.youtube.com/watch?v=5NI-tNIm6uY) | 28:07 | 1 849 097 |

### Observaciones de contenido y empaque textual

La secuencia presenta África desde varias entradas: viaje difícil, Zanzíbar, vida nocturna en Nairobi, safari y visita a una casa masái. Después pasa a una reflexión sobre su sueño, costo de vida en Venezuela y reencuentro familiar en Isla Larga. La continuidad del personaje permite pasar de descubrimiento cultural a vida cotidiana sin cambiar de identidad. No significa que esos públicos sean idénticos; se necesitaría Analytics para medirlo.

Los títulos usan primera persona y verbos concretos («entré», «me enamoré»), superlativo («peor», «más salvaje»), pregunta útil («cuánto cuesta»), incertidumbre («renunciaré») y relaciones («mis hermanas»). El conflicto y la recompensa cambian entre episodios de una misma gira. No describimos la imagen de portada desde estos textos.

La descripción del video de reflexión conecta ocho años de viaje y 117 países con una nueva meta de 150, y pide al público opinar sobre continuar viajando. Son declaraciones de la creadora, no validaciones independientes de cada país. El video de costo de vida anuncia supermercado, gasolina, transporte, servicios, restaurante, gimnasio y vivienda, además de testimonios callejeros; la pregunta de cierre solicita una opinión económica. El de Isla Larga sitúa la acción en Puerto Cabello y en una salida con hermanas y padres. Así el episodio familiar conserva anclas de destino y turismo, no depende sólo de intimidad.

### Frecuencia y desempeño con límites

Las ocho publicaciones observadas alternan jueves y domingo. Siete intervalos: 3, 4, 3, 4, 3, 4, 3 días. Periodo de 24 días y 2,04 publicaciones/semana. Es una cadencia demostrada en esta ventana; no se extrapola automáticamente a todo 2026 ni a Instagram. Las duraciones varían de 16:24 a 30:50, mediana 22:40 usando segundos del reproductor. Algunas etiquetas de tarjeta redondean un segundo más; se conservaron tal como aparecen.

«El peor viaje...» (10-sep) suma 1 849 097 vistas y es también el más antiguo de los ocho; el safari (20-sep) suma 627 970. El último familiar (4-oct) suma 422 266 en aproximadamente dos días; no hay medición histórica suficiente para compararlo a igual edad con los anteriores. No debe usarse la división vistas/días como una tasa de crecimiento actual ni inferirse CTR.

### Hipótesis aplicables, por probar

La gira puede organizarse como una temporada con una pregunta distinta por entrega: experiencia, rutina local, costo, cultura y consecuencias personales. Un canal nuevo necesita entregar contexto en cada episodio para quien llega desde recomendaciones y no vio los anteriores. La alternancia emocional/utilitaria es una hipótesis atractiva si el mismo personaje sigue siendo reconocible. La cadencia de dos videos por semana requiere un colchón de grabación y edición; copiarla sin ese margen sería una propuesta de producción, no una conclusión de estos datos.

Instagram: tres publicaciones primarias seleccionadas confirman remisión a YouTube y presencia de marca de swimwear; se detallan al final. Las miniaturas se inspeccionaron en la captura Browser compartida y se describen en evidencia visual.

## 3. La Vida de Viaje — referencia de nicho y sistema transmedia histórico

Fuentes: [quiénes somos, sitio propio](https://lavidadeviaje.com/quienes-somos/), [YouTube enlazado](https://www.youtube.com/lavidadeviaje/videos), [Instagram enlazado](https://www.instagram.com/lavidadeviaje/). El proyecto identifica a Andrés Calla y Jime Sánchez y define movimiento lento en naturaleza; menciona bicicleta, kayak, caminatas y casa rodante. El contraste con vlogs generalistas es útil para decidir especialización.

### Muestra primaria de la pestaña Videos

| Fecha de publicación | Video / enlace primario | Duración visible | Vistas observadas |
|---|---|---:|---:|
| 2024-07-12 | [📍 Cabo Blanco, Santa Cruz. Argentina 🇦🇷](https://www.youtube.com/watch?v=lXCqB8TLFss) | 1:45 | 634 |
| 2021-09-29 | [GLAMPING EN CÓRDOBA: DOMOS INMERSOS EN EL MONTE SERRANO](https://www.youtube.com/watch?v=nC5mkyAqudY) | 1:01 | 4 252 |
| 2021-07-18 | [Al Pie del NEVADO, CACHI. Salta 🚵 #cicloturismo](https://www.youtube.com/watch?v=3bOdylF2wzA) | 12:08 | 2 353 |
| 2021-07-15 | [(TRAILER) Al Pie del NEVADO, CACHI. Salta 🚵 #cicloturismo](https://www.youtube.com/watch?v=6IfSHEErGP4) | 0:56 | 371 |
| 2021-07-10 | [EL ALGARROBAL, CACHI. Salta 🚵  #cicloturismo](https://www.youtube.com/watch?v=RDo7bKB-eCY) | 4:11 | 1 749 |
| 2021-07-07 | [(TRAILER) EL ALGARROBAL, CACHI. Salta 🚵  #cicloturismo](https://www.youtube.com/watch?v=K2t7ZkH9oRU) | 1:00 | 600 |
| 2021-07-03 | [VUELTA al RIO PINTO 🚵  #cicloturismo](https://www.youtube.com/watch?v=yfP-ZS49Eng) | 15:01 | 2 950 |
| 2021-07-01 | [(TRAILER) VUELTA al RIO PINTO 🚵  #cicloturismo](https://www.youtube.com/watch?v=Rt-WtQhOiJs) | 1:00 | 543 |

### Observaciones de contenido y empaque textual

La muestra de julio 2021 encadena Rio Pinto, El Algarrobal y Al Pie del Nevado en pares trailer/episodio. El trailer antecede al episodio 2, 3 y 3 días, respectivamente. No se asume que funcionara como Short: YouTube los muestra aquí como Videos, con duraciones de aproximadamente un minuto. Los episodios usan lugar concreto y la etiqueta cicloturismo. Es un empaque basado en ruta/actividad que facilita identidad de nicho, con menos promesa emocional explícita que Vero o PlanetaJuan.

Las descripciones dirigen a la comunidad del blog y declaran embajadores Venzo/Spot Latam. El clip de glamping pide leer el artículo completo en el blog; la web concentra guías, historias, destinos, libros, contacto para marcas y newsletter. El canal puede funcionar como una pieza de un ecosistema editorial. No se conoce el tráfico ni la conversión entre piezas.

El [catálogo de películas propio](https://lavidadeviaje.com/peliculas/) además documenta cuatro obras: [Manifiesto](https://www.youtube.com/watch?v=06l2rF5Mkok), 2020, 10 minutos; [Alsur: Tierra del Fuego en bicicleta](https://www.youtube.com/watch?v=FTitVUsknNk), 2019, 22 minutos; [12 Días, bikerafting río Santa Cruz](https://www.youtube.com/watch?v=saXl41bN8ms), 2018, 36 minutos; [1247, Carretera Austral](https://www.youtube.com/watch?v=hq-_oosSj4I), 2017, 40 minutos. Años/duraciones proceden del catálogo del creador y son aproximados; no se verificaron fechas exactas ni vistas de esos cuatro. Las descripciones de obra ofrecen un viaje, una búsqueda y una transformación, no sólo una lista turística. Las selecciones en Banff se atribuyen a la web del autor, sin verificación independiente del festival.

### Frecuencia y desempeño con límites

El último video encontrado es de julio 2024 y el anterior de septiembre 2021. Esto indica inactividad de esta pestaña en 2026. Un cálculo mecánico de los ocho últimos mezclaría una campaña de 2021 con enormes pausas y sería engañoso como cadencia operativa. **Frecuencia actual: ND; no activo en la muestra.**

Durante la serie 1–18 julio 2021 hay seis piezas en 17 días, tres episodios y tres trailers. Si se describe esa campaña histórica, aparecen cinco intervalos de 2, 4, 3, 5 y 3 días; no es la frecuencia actual. Los episodios acumulan entre 1 749 y 2 950 vistas y los trailers entre 371 y 600. El mayor tamaño de las películas o el prestigio de festival no permite concluir rendimiento comercial del canal.

### Hipótesis aplicables, por probar

Un canal nuevo de viajes puede escoger una experiencia distintiva —bicicleta, caminatas, transporte público, campamentos— y repetir la actividad con destinos diferentes. Eso crea un motivo para volver más concreto que «viajamos». Un trailer debe entregar valor por sí mismo y dar una razón para abrir el episodio; la mera existencia de pares no demuestra que el puente haya convertido. Un blog/guía descargable es útil si responde preguntas que no caben en el relato, pero necesita inversión propia y medición.

Instagram confirma retorno editorial en mayo 2026, aunque YouTube permanece sin nuevas publicaciones en la muestra. El grid mezcla piezas de 2021, 2022 y 2026: no permite calcular frecuencia actual. Miniaturas inspeccionadas en captura Browser. No confundir La Vida de Viaje con La Vida **en un** Viaje ni con La Vida de M: son identidades distintas.

## 4. PlanetaJuan — viaje serializado y producto editorial propio

Fuentes: [YouTube oficial](https://www.youtube.com/@planetajuan/videos), [Instagram enlazado desde descripciones](https://www.instagram.com/planetajuan/), [Linktree del creador](https://linktr.ee/planetajuan). Se incorpora como cuarto caso para añadir una referencia activa frente a los dos proyectos históricos. Es creador individual y no un canal de pareja.

### Muestra primaria

| Fecha de publicación | Video / enlace primario | Duración visible | Vistas observadas |
|---|---|---:|---:|
| 2026-10-04 | [Me quieren buscar mujer en UZBEKISTÁN 🇺🇿](https://www.youtube.com/watch?v=rPtr1AD6cnM) | 32:36 | 314 923 |
| 2026-09-30 | [Uzbekistán NO ES como yo creía... 🇺🇿](https://www.youtube.com/watch?v=FU9oP1jJn50) | 35:19 | 480 510 |
| 2026-09-27 | [Las ciudades PERDIDAS de la Ruta de la Seda](https://www.youtube.com/watch?v=mUQ9AtUTHzE) | 27:37 | 525 294 |
| 2026-09-20 | [Jamás imaginé que UZBEKISTÁN fuera así 🇺🇿](https://www.youtube.com/watch?v=tQwBy0ZMNVA) | 31:58 | 810 353 |
| 2026-09-16 | [Escapando de TURKMENISTÁN por la Frontera 🇹🇲](https://www.youtube.com/watch?v=MGrWEcN_eKM) | 32:01 | 946 741 |
| 2026-09-13 | [La Turkmenistán que NO quieren que veas 🇹🇲](https://www.youtube.com/watch?v=WkX8ykZNlKo) | 32:03 | 1 425 614 |
| 2026-09-06 | [Entré al país MÁS RARO Y ABSURDO del planeta 🇹🇲](https://www.youtube.com/watch?v=2FlBpZFhYC0) | 1:01:21 | 2 374 883 |
| 2026-09-02 | [Top 5 países que JAMÁS VOLVERÉ 🤫](https://www.youtube.com/watch?v=QojLaU9A8Ag) | 21:59 | 3 269 148 |

### Observaciones de contenido y empaque textual

Seis de los ocho títulos cubren una gira de Turkmenistán y Uzbekistán, más un ranking de países y una pieza histórica sobre Ruta de la Seda. El paso «entré → otra cara → frontera → descubrimiento del país siguiente» convierte una ruta geográfica en varios conflictos editoriales. Las promesas son de curiosidad («raro y absurdo»), acceso («no quieren que veas»), transición («escapando por la frontera»), sorpresa («no es como creía») e interacción social («me quieren buscar mujer»).

Hay mayúsculas selectivas, banderas y emojis; en esta muestra no aparece una numeración de episodios en el título. La secuencia puede consumirse como temporada pero cada video contiene una promesa independiente. En comparación con Misias, pesa más qué descubrirá el espectador que cómo planear su propio itinerario. Esta es una clasificación de títulos, no un conteo de todos los minutos de contenido.

Las ocho descripciones presentan un bloque comercial repetido con libro, Holafly, Surfshark, escuela de inglés/francés, membresía del canal y cuentas sociales. Su [Linktree](https://linktr.ee/planetajuan) ofrece los libros Migrantes e Inadaptados, audiolibro y varios distribuidores. Es evidencia de un ecosistema editorial y educativo con afiliación; las ventas, comisiones y participación de cada fuente son ND. La mención de membresía es una oferta visible y no permite inferir número de miembros pagadores.

### Frecuencia y desempeño con límites

Ocho publicaciones abarcan 32 días, del 2-sep al 4-oct-2026: intervalos 4, 7, 3, 4, 7, 3, 4 días en orden cronológico; mediana 4 días; 1,53 publicaciones por semana. Predominan domingo y miércoles, pero hay semanas con una sola entrega; no se presenta como dos por semana constante. La mediana de duración es 32:01,5 a partir de segundos; una entrega supera una hora y otra ronda 22 minutos, por lo que hay flexibilidad según promesa.

El ranking «Top 5 países...» suma 3 269 148 vistas, seguido del primer video de Turkmenistán con 2 374 883. Ambos son los más antiguos de los ocho. En Uzbekistán las entradas más recientes suman de 314 923 a 810 353; comparar directamente no demostraría menor interés del país. Para evaluar paquetes, se necesitaría seguir las vistas al mismo día 2/7/28 de cada publicación.

### Hipótesis aplicables, por probar

Una ruta puede descomponerse antes de viajar en episodios con conflictos diferentes; no hay que esperar a la edición para inventar el título. Un nuevo creador puede usar contraste expectativa/realidad y diálogo local sin depender de lugares de acceso complicado o de viajes caros. Si se ofrece un producto propio, conviene que comparta la misma promesa central del canal; este caso muestra convivencia de libro, idioma y migración/viaje, pero no prueba cuál funciona mejor.

Miniaturas e Instagram verificados con tres piezas primarias seleccionadas por plataforma; detalle en las secciones siguientes.

## Evidencia visual: 12 miniaturas inspeccionadas

Observaciones de imágenes vistas directamente, tres por canal. Se describen composición, texto y relación con el título; CTR, resultado de pruebas A/B, diseño original vs revisiones y composición fotográfica exacta son ND. Las imágenes pueden contener montajes gráficos; verlos no permite declarar una escena falsa ni saber con qué herramientas se produjo.

### Misias pero viajeras

Evidencia: `evidencia/miniaturas_misias_contacto.png`, elaborada con las URLs públicas originales guardadas en el JSON. En la despedida, las dos creadoras aparecen juntas en primer plano, fondo interior desaturado y dos bloques grandes de texto rosa/verde que anuncian una conversación. El título es sobrio y la portada transmite vínculo/comunidad.

La guía de El Salvador combina rostro sorprendido en primer plano, bandera, volcán, playa y arquitectura con un titular blanco superior y nombre del país. La pieza de primeras 24 horas coloca a la presentadora con cámara, plaza urbana de fondo, texto amarillo superior y nombre del país azul muy grande. Ambas portadas priorizan expresión y destino con colores intensos; la primera promete variedad mediante collage, la segunda encuentro/presencia en el sitio. No se midió legibilidad a tamaños móviles ni rendimiento diferencial.

**Hipótesis:** para una guía de destino, usar uno o dos elementos que prueben variedad puede ayudar; demasiados elementos podrían competir con la cara/texto. Es una decisión que necesita test de miniaturas del canal nuevo, no un supuesto de eficacia.

### Viajando con Vero

Evidencia: `evidencia/miniaturas_vero.png`, captura Browser. La primera fila se inspeccionó con claridad. La pieza familiar muestra selfie de la presentadora y sus dos hermanas en agua turquesa, sin texto grande. La de costo de vida sitúa a presentadora e interlocutor, billetes visibles, bandera venezolana y texto blanco muy grande que contrapone dos cantidades ($500 y $10.000). La reflexión coloca rostro serio, maleta/pasaporte y aeropuerto/avión al atardecer, con una pregunta breve en blanco/amarillo sobre el final de etapa.

Son tres soluciones visuales distintas para tres promesas: vínculo + lugar, evidencia económica + contraste, incertidumbre personal + símbolo de viaje. La ausencia de texto en la portada familiar también evita imponer una plantilla única a cada episodio. La segunda fila visible incluye una visita situacional masái y un montaje de fauna en safari con expresión sorprendida; se usó sólo como contexto, sin ampliar el conteo de tres piezas revisadas en detalle.

**Hipótesis:** vincular el motivo visual a la pregunta editorial es más útil que mantener siempre la misma cantidad de texto. Una portada de costos puede contrastar dos cifras; una de relación/familia puede apoyarse en el gesto y lugar.

### La Vida de Viaje

Evidencia: `evidencia/miniaturas_lavidadeviaje.png`, captura Browser. Cabo Blanco usa vista aérea costera, tonos apagados y nombre del lugar centrado en letras blancas espaciadas. Glamping muestra un domo blanco dentro de vegetación, sin titular superpuesto visible. Al Pie del Nevado usa paisaje montañoso amplio y título blanco centrado, con localización adicional menor.

El paisaje ocupa el espacio que otros canales dan a la cara; lugar y atmósfera son la evidencia. El blanco centrado y la tipografía espaciada dan una continuidad visual a dos piezas. En esta muestra no domina un rostro con emoción amplificada. Eso es una alternativa creativa comprobada, pero las pocas vistas no prueban que el estilo cause bajo rendimiento: también difieren actividad, tamaño del canal, nicho y distribución.

**Hipótesis:** una identidad de naturaleza puede hacer que el lugar sea protagonista si el canal busca un público de observación y slow travel. Para sumar una pregunta narrativa se puede probar situación/persona dentro del paisaje, conservando espacio visual.

### PlanetaJuan

Evidencia: `evidencia/miniaturas_planetajuan_contacto.png`, miniaturas públicas originales. Las tres primeras piezas **no tienen grandes titulares superpuestos visibles**. En la más reciente, un hombre mayor muestra una tela o prenda mientras el presentador observa, en una escena cotidiana de exterior/interior de barrio. En la segunda, el creador aparece con casco y gafas sosteniendo un muñeco de bebé, con arquitectura monumental de fondo. En la tercera, rostro en primer plano y gorro voluminoso de piel/felpa, sobre arquitectura y torres del destino.

Las imágenes proponen interacción, rareza visual y caracterización personal; los títulos aportan la pregunta o el contexto. Un mismo fondo arquitectónico puede diferenciarse por una situación humana concreta. La miniatura no repite palabra por palabra el título. No se afirma que el gorro sea de un material específico ni que la escena tenga una explicación que no vimos en metraje.

**Hipótesis:** fotografía de una situación que necesita explicación + título claro puede crear curiosidad sin colocar texto adicional. Para un canal nuevo sería necesario mostrar suficiente contexto para que la rareza no parezca arbitraria.

## Instagram: 12 publicaciones primarias y su función

URLs/fechas recogidas en Browser por el equipo y captions contrastados con `og:description` público de cada enlace. El JSON `02_instagram_posts.json` conserva la evidencia. No se vio el metraje completo de estos Reels ni todas las diapositivas; un `/p/` con etiqueta «Photo» se reporta como publicación fotográfica de feed y no permite asegurar si es imagen única o carrusel. `reel` identifica formato Reel. El contenido del caption se **parafrasea** para distinguir mensaje de estilo visual. Métricas de alcance, guardados, clics y conversión son ND.

| Creador | Fecha | Publicación primaria | Formato verificable | Mensaje / función del caption |
|---|---|---|---|---|
| Misias | 2025-05-30 | [Anuncio de cierre](https://www.instagram.com/misiasperoviajeras/p/DKSvhYKOizj/) | Feed fotográfico | Explica el final del proyecto conjunto y continuidad individual; comunicación de comunidad |
| Misias | 2025-05-30 | [Convocatoria a YouTube](https://www.instagram.com/misiasperoviajeras/reel/DKSKiJeIDyE/) | Reel | Convoca al canal a las 4 pm Perú para un anuncio; puente de Instagram a estreno/conversación larga |
| Misias | 2024-12-31 | [Cierre de año](https://www.instagram.com/misiasperoviajeras/reel/DEQY9VVOOnO/) | Reel | Agradece viajes y comunidad de 2024; mantiene lenguaje de ahorro y expectativa de 2025 |
| Vero | 2026-10-04 | [Día familiar](https://www.instagram.com/veronicaweffer/p/DeFvhUeiUO4/) | Feed fotográfico | Evoca vínculo familiar, remite al video completo en YouTube y etiqueta su swimwear |
| Vero | 2026-09-25 | [Sentido de viajar](https://www.instagram.com/veronicaweffer/p/Ddt8jJzkb_y/) | Feed fotográfico | Reflexiona sobre cultura y formas de vida; marca personal y propósito, sin CTA a YouTube en el caption revisado |
| Vero | 2026-09-20 | [Safari África](https://www.instagram.com/veronicaweffer/reel/Ddh1yI7JemJ/) | Reel | Pregunta si el público haría un safari y manda a tocar el enlace del Reel para el video completo |
| La Vida | 2026-05-05 | [Retorno](https://www.instagram.com/lavidadeviaje/p/DX-Kan_kWNX/) | Feed fotográfico | Declara regreso a contar viajes, tras pausa de pantallas; pasa a observar la naturaleza como propósito |
| La Vida | 2026-05-14 | [Vida simple](https://www.instagram.com/lavidadeviaje/reel/DYVfVnFtJ1h/) | Reel | Mensaje breve sobre sencillez y naturaleza con geolocalización por hashtags, sin CTA explícito en el caption |
| La Vida | 2022-10-11 | [Laguna Blanca](https://www.instagram.com/lavidadeviaje/p/Cjlq4FNJ2Vm/) | Feed fotográfico | Ubicación concreta y mención turística nacional; pieza de catálogo de destinos |
| PlanetaJuan | 2026-09-27 | [Encontró a Nemo](https://www.instagram.com/planetajuan/p/Ddz0mhdGYCj/) | Feed fotográfico | Guiño humorístico breve; caption no dirige a YouTube |
| PlanetaJuan | 2026-09-23 | [Turkmenistán](https://www.instagram.com/planetajuan/p/Ddpmt6ODVLR/) | Feed fotográfico | Sitio curioso y humor; pregunta si vieron el video, referencia a contenido largo sin enlace textual en el caption |
| PlanetaJuan | 2026-09-17 | [Australia](https://www.instagram.com/planetajuan/reel/DdZ0eJzyi37/) | Reel | Emoción personal en pocas palabras; el Reel habla de otro destino que la gira de YouTube de esa semana |

### Frecuencia observable y cautelas del grid

- **Vero:** el grid Browser muestra 12 entradas fechadas 1-sep a 4-oct-2026, siete fotográficas de feed y cinco Reels; en orden cronológico descendente en la captura. La densidad observada por intervalos es 2,33 entradas/semana en esos 33 días. No equivale a un censo de Stories ni a la cadencia anual, y puede omitir entradas no cargadas. El safari tiene publicación de Instagram y YouTube el mismo 20-sep, y el día familiar también coincide el 4-oct: coordinación de lanzamiento comprobada en dos pares, sin atribuir conversiones.
- **PlanetaJuan:** seis entradas propias del grid tienen fecha 2–27-sep-2026 (cinco fotográficas y un Reel); densidad de esa muestra por intervalos 1,40/semana. El grid completo entregado incluye una pieza cuyo autor visible es Netflix Colombia: no se atribuye como producción exclusiva de Juan ni se inventa relación comercial. El Reel de Australia en una semana de videos de Asia Central muestra que ambas plataformas no siempre siguen la misma cronología de destinos.
- **Misias:** las primeras posiciones incluyen un Reel de enero 2024 antes de piezas de mayo 2025. No se calcula cadencia con el orden visual: puede haber fijados y la condición exacta no se verificó. La comunicación del cierre sí está validada por dos publicaciones del mismo día y la página YouTube.
- **La Vida:** el grid mezcla mayo 2026 con julio 2021 y agosto 2022 antes de volver a mayo 2026. Frecuencia actual ND. Dos piezas en mayo demuestran retorno en Instagram, sin probar una cadencia posterior ni vuelta a YouTube.

### Lecturas útiles para el canal nuevo, formuladas como hipótesis

Instagram puede cumplir funciones distintas por pieza: sacar una escena con pregunta y CTA preciso; compartir una imagen familiar con referencia al episodio; mantener propósito/personaje con reflexión; o comunicar un cambio del proyecto. Copiar sólo paisajes pierde el puente editorial que sí vemos en Vero y Misias. Una prueba de lanzamiento podría alternar estas funciones y registrar qué publicaciones generan tráfico medible, guardados o conversación; no se conocen esos resultados en los referentes.

Un Reel con destino diferente al YouTube de esa semana puede mantener variedad o reflejar retraso editorial; no se elige una explicación sin evidencia. Para nuestro canal conviene decidir conscientemente si Instagram acompaña el mismo episodio o documenta el viaje más actual y explicarlo cuando sea necesario.

## YouTube Shorts: muestra separada de los videos de la pestaña Videos

Revisión adicional del 6-oct-2026: HTML público de la pestaña Shorts, primeras tres tarjetas donde existe esa pestaña, con fecha y contador de la página pública individual. No se mezclan con la cadencia de Videos calculada arriba. Un clip corto en Videos tampoco se reclasifica automáticamente como Short. No se visionó el metraje de estos clips; la clasificación de temas procede del título.

| Canal | Fecha | Short primario | Duración | Vistas al consultar |
|---|---|---|---:|---:|
| Misias pero viajeras | 2024-12-31 | [#Adiós 2024, hola #2025 🥺](https://www.youtube.com/shorts/y5bwqpHKkLA) | 19 s | 41 105 |
| Misias pero viajeras | 2024-12-30 | [Renovando #contrato de #viajes 😝✈️](https://www.youtube.com/shorts/1PIhVY3bBXY) | 8 s | 27 796 |
| Misias pero viajeras | 2024-12-23 | [#Navidad siendo #latino 😝🎄](https://www.youtube.com/shorts/Z0DClMLOmWM) | 13 s | 20 301 |
| Viajando con Vero | 2026-09-27 | [¡No podrás parar de jugar Tasty Travels! Descárgalo para tus ratos libres 😍](https://www.youtube.com/shorts/yicAvf4ofvY) | 38 s | 23 558 |
| Viajando con Vero | 2026-03-02 | [GANA DINERO MIENTRAS VIAJAS](https://www.youtube.com/shorts/yL1HfxhXoIs) | 81 s | 419 870 |
| Viajando con Vero | 2025-10-18 | [ASÍ REACCIONAN A MIS BIKINIS EN PLAYAS DE INDIA 🇮🇳  #india #playasdeindia](https://www.youtube.com/shorts/9OrBOzU6Jjc) | 37 s | 795 354 |

- **Misias:** pestaña Shorts presente; los tres primeros observados se publicaron 23, 30 y 31-dic-2024. Son piezas de temporada, humor/vínculo y cierre de año, de 8–19 segundos. Se comprueba el mismo tema y fecha de cierre de año en Instagram, pero no identidad exacta del metraje porque no se reprodujeron ambos. No hay publicaciones recientes en esta muestra; frecuencia actual ND. No sumar estos tres al cálculo de los siete episodios viajeros de noviembre/diciembre.
- **Vero:** pestaña Shorts presente; los primeros tres aparecen separados por grandes periodos: 18-oct-2025, 2-mar-2026 y 27-sep-2026. El más reciente promueve descargar un juego, el segundo vincula ingresos con viaje y el tercero plantea reacción cultural a bikinis. Sólo el título del primero permite calificarlo de promoción; pago, patrocinador o condiciones comerciales son ND. La pieza de 81 segundos se identifica como Short por la pestaña y URL, no por un límite supuesto de 60 segundos. La cadencia de aproximadamente dos videos semanales observada en septiembre/octubre es de **Videos**; no constituye frecuencia de Shorts. Aquí no hay evidencia de una cadencia de Shorts continua; frecuencia actual ND con tres piezas tan separadas.
- **La Vida de Viaje:** la navegación pública no muestra pestaña Shorts. Consultar `/shorts` devuelve contenido con Principal seleccionado y sin tarjetas Shorts. Es ausencia de una pestaña pública en esta revisión; no se afirma que nunca haya publicado un Short ni que no pueda tener piezas retiradas/no públicas.
- **PlanetaJuan:** tampoco aparece pestaña Shorts en la navegación pública y la ruta solicitada regresa al contenido Principal. La muestra activa de ocho videos de la investigación corresponde a Videos. La ausencia pública de Shorts ofrece una referencia de estrategia centrada en esa pestaña, sin probar motivos editoriales.

**Hipótesis para lanzar:** los casos muestran que un canal activo de viajes no necesita necesariamente una cadencia alta de Shorts para sostener videos largos. No demuestra que los Shorts ayuden o perjudiquen al crecimiento; para el canal nuevo conviene probarlos como piezas independientes con promesa clara y medir audiencia/puente a largo, antes de duplicar todo Reel automáticamente. Evidencia reproducible: `02_shorts.json`.

## Qué medir en nuestro canal sin confundir benchmark con causalidad

Propuestas para validar tras el lanzamiento, no métricas observadas de los competidores:

1. Comparar títulos de utilidad (costo/ruta), experiencia (reto/imprevisto) y descubrimiento cultural a edades iguales: 48 horas, 7 y 28 días.
2. Medir CTR por fuente, retención a 30 segundos, porcentaje medio visto y espectadores recurrentes dentro de YouTube Studio. No hay acceso a estas métricas privadas de los referentes.
3. Probar una cadencia sostenible, por ejemplo un video semanal durante ocho semanas; las dos publicaciones semanales de un referente activo no constituyen una obligación.
4. Etiquetar cada pieza de Instagram por función —dato guardable, escena de historia, pregunta/comunidad, avance del episodio— y registrar clics cuando la herramienta lo permita, evitando atribuir toda reproducción de YouTube a Reels.
5. Documentar fecha de viaje, presupuesto y supuestos de precio dentro de cada episodio/descripcion, siguiendo la precisión observada en Misias.
6. Separar trailers/clips, episodios y despedidas en cualquier promedio. Publicar un último video no convierte un archivo histórico en competidor activo.

## Archivos de evidencia

- `02_parejas_nomadas_datos.json`: 32 videos, URLs primarias, fechas, duración, vistas, descripciones y URLs públicas de miniaturas.
- `extract_public_channels.py`: extracción reproducible limitada a datos públicos de la primera página de la pestaña Videos.
- `02_instagram_posts.json`: 12 publicaciones primarias, fechas del grid y metadatos/captions públicos.
- `02_shorts.json`: navegación Shorts de cuatro canales, seis clips públicos con fecha, vistas y duración.
- `00_instagram_grids.json` y `evidencia/ig_*.txt`: evidencia de grid recolectada por Browser.
- `evidencia/miniaturas_*`: imágenes inspeccionadas para los cuatro casos.
- Los perfiles y cada video se enlazan en las tablas; son fuentes primarias. El buscador puede mostrar cifras obsoletas y por eso no se usó para los contadores de estas tablas.
