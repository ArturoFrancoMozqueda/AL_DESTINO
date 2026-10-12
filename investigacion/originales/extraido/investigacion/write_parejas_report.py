import json,pathlib,statistics,datetime
D=json.load(open('investigacion/02_parejas_nomadas_datos.json'))
def table(name):
 r=['| Fecha de publicación | Video / enlace primario | Duración visible | Vistas observadas |','|---|---|---:|---:|']
 for v in D[name]['videos']:
  r.append('| '+v['datePublished'][:10]+' | ['+v['title'].replace('|','·')+']('+v['url']+') | '+v['duration']+' | '+f"{int(v['viewsExact']):,}".replace(',',' ')+' |')
 return '\n'.join(r)
intro='''# Benchmark: Misias pero Viajeras, Viajando con Vero, La Vida de Viaje y PlanetaJuan

Fecha de observación: **6 de octubre de 2026**, America/Mexico_City. Investigación de cuatro identidades distintas, con YouTube e Instagram vinculados desde sus fuentes propias. Viajando con Vero reemplaza la identificación no verificada «Viajando con Vero y Alex»: el canal verificado pertenece a Verónica Weffer. Misias y La Vida de Viaje son referencias **históricas** en YouTube; no deben contarse como canales activos de 2026.

## Método y límites

Se consultaron buscador web, páginas de los creadores y HTML público de las pestañas Videos de YouTube, sin sesión ni métricas privadas. Para cada canal se capturaron sus ocho primeras entradas de la pestaña Videos. De la página pública individual se extrajeron título, autor, descripción, fecha de publicación y contador de reproducciones desde `ytInitialPlayerResponse`; la duración de la tarjeta se conserva tal como se mostró. No se usaron APIs privadas, proyecciones de ingresos de agregadores ni supuestos sobre CTR/retención. El JSON adjunto conserva descripciones y URLs de miniatura para auditar el análisis.

Las vistas son una **fotografía acumulada al consultar**, cambian continuamente y los videos tienen edades distintas. No prueban que un título, miniatura o destino cause más reproducciones. Esta muestra privilegia actualidad de publicación y no es aleatoria ni permite afirmar la frecuencia anual. La frecuencia se calcula con fechas exactas entre primera y última entrada: `(n−1) × 7 / días entre publicaciones`. «ND» significa no determinado. La pestaña Videos excluye Shorts y transmisiones de otras pestañas; una pieza de un minuto aquí no implica que sea Short. No se vio el metraje completo: las observaciones de estructura se basan en descripciones, capítulos y secuencia de temas; no se inventan hooks visuales, montaje, audio o retención. La auditoría visual y la muestra de Instagram se documentan por separado cuando Browser entrega evidencia.

## Comparación útil para un lanzamiento

| Canal | Situación verificada en YouTube | Identidad / promesa visible | Cadencia de la muestra | Duración de la muestra | Uso comercial visible |
|---|---|---|---|---|---|
| Misias pero viajeras | Cierre declarado 30-may-2025 | Viajar con utilidad económica; amigas peruanas | Siete videos viajeros 10-nov a 29-dic-2024: 0,86/semana; cierre separado | Viajes entre 10:02 y 30:12 | eSIM, seguro, tienda, redes personales; cierre dirige a canales individuales |
| Viajando con Vero | Activo, último 4-oct-2026 | Destinos + familia + experiencias emocionales | Ocho videos 10-sep a 4-oct-2026: 2,04/semana | 16:24–30:50; mediana por segundos 22:40 | En esta muestra el CTA visible se centra en comentar y acompañar la historia; otras piezas históricas cruzan a IG |
| La Vida de Viaje | Último video encontrado 12-jul-2024; anterior 29-sep-2021 | Movimiento lento, naturaleza, bici/kayak/casa rodante | Frecuencia actual ND; serie de julio 2021 combina episodios y trailers | Episodios 4:11–15:01; clips/trailers 0:56–1:45 | Blog, comunidad, embajadores; web ofrece libros y newsletter |
| PlanetaJuan | Activo, último 4-oct-2026 | Curiosidad cultural, expectativas vs realidad, encuentros locales | Ocho videos 2-sep a 4-oct-2026: 1,53/semana | 21:59–1:01:21; mediana 32:01,5 por segundos | Libros, eSIM, VPN, escuela de idiomas, membresía, IG |

Las dos referencias históricas enriquecen las opciones creativas, pero su tamaño y catálogo no equivalen a actividad actual. Un benchmark que no distingue esto podría recomendar una carga de producción que sus propios referentes dejaron de sostener.
'''
misias='''## 1. Misias pero viajeras — utilidad práctica como marca

Fuentes de identidad: [YouTube oficial](https://www.youtube.com/@misiasperoviajeras/videos), [Instagram enlazado en sus descripciones](https://www.instagram.com/misiasperoviajeras/). La descripción de «Un mensaje importante» declara que el proyecto llega a su fin y deriva a [Fátima](https://youtube.com/@Fatima_Sotoma) y [Daniela](https://www.youtube.com/@danielaritacabrera). Este dato primario confirma el cierre anunciado en prensa. Las creadoras no se presentan como pareja sentimental; son una dupla de amigas.

### Muestra primaria

'''+table('Misias pero viajeras')+'''

### Observaciones de contenido y empaque textual

La muestra combina guías de entrada («primeras 24 horas»), lista concreta («10 actividades»), comparación («magnate vs real»), precio explícito («US$20»), evaluación de hospedaje («mi hotel favorito») y gastronomía numerada («5 platos»). México, Venezuela y El Salvador generan siete entregas viajeras antes de la despedida. Hay una promesa verificable en el título que puede resolverse dentro del episodio, más allá de «nuestro viaje a X».

Los capítulos de El Salvador permiten revisar estructura sin simular visionado: llegada 0:46, costos de traslados 1:18, migraciones 2:56, aeropuerto a ciudad 4:27, alojamiento 5:34, mercado 6:20, comida 8:55, recorrido urbano, impresiones 22:45 y cierre 28:27. El segundo episodio reorganiza la experiencia como diez actividades, con puntos útiles entre 0:39 y 23:50 y enlaces de mapas. Es una misma zona convertida en dos intenciones de consumo: vivir la llegada y planear qué hacer.

Las descripciones distinguen **temporada de viaje** (noviembre 2024 en El Salvador) de fecha de publicación (diciembre 2024). Eso evita confundir la actualidad de un precio o condición de destino. Incluyen descuentos Holafly/IATI, suscripción, Instagram conjunto, perfiles personales y tienda propia. Se observa diversificación de enlaces comerciales; sus ingresos y conversiones son ND. Las menciones a puntos de venta pertenecen al texto histórico de esos videos, no prueban que los locales o tienda operen hoy.

### Frecuencia y desempeño con límites

Separando la despedida, siete videos viajeros abarcan 49 días (10-nov a 29-dic-2024): seis intervalos, 0,857 publicaciones por semana, mediana de intervalo 7,5 días; intervalos individuales de 4 a 14 días. El cierre llega 152 días después del último viaje de la muestra. No se recomienda promediar ambos periodos para presentar una frecuencia actual.

En esa muestra Xcaret reúne 515 603 vistas; primeras 24 horas en El Salvador, 284 396; la lista de actividades, 179 366. La diferencia sugiere temas para estudiar, no demuestra que hoteles o logística ganen siempre. Cada video acumula distinta antigüedad, interés del destino y distribución. Las vistas de la despedida se excluyen de comparación de temas viajeros.

### Hipótesis aplicables, por probar

Un nuevo canal puede distinguirse si transforma el presupuesto en un elemento recurrente: enseñar ticket/importe, contexto de temporada, decisión de ahorro y resultado. Un itinerario de dos episodios («llegar» y «hacer») puede abaratar investigación y grabación, siempre que cada entrega resuelva una pregunta nueva. Para una dupla, acordar responsabilidades, pausas y forma de continuar individualmente es una decisión de producción útil ante el cierre observado; no permite atribuir causas personales no publicadas.

Miniaturas: ND hasta revisión visual. Instagram: cuenta verificada por enlaces cruzados; muestra de posts y frecuencia ND si Browser no aporta fechas.
'''
vero='''## 2. Viajando con Vero — continuidad de personaje y contraste emocional

Fuentes: [YouTube oficial](https://www.youtube.com/@ViajandoconVero/videos), [Instagram](https://www.instagram.com/veronicaweffer/). El perfil de YouTube identifica a Verónica Weffer; videos anteriores enlazan ese Instagram con su nombre. No se encontró evidencia primaria de un proyecto «Vero y Alex».

### Muestra primaria

'''+table('Viajando con Vero')+'''

### Observaciones de contenido y empaque textual

La secuencia presenta África desde varias entradas: viaje difícil, Zanzíbar, vida nocturna en Nairobi, safari y visita a una casa masái. Después pasa a una reflexión sobre su sueño, costo de vida en Venezuela y reencuentro familiar en Isla Larga. La continuidad del personaje permite pasar de descubrimiento cultural a vida cotidiana sin cambiar de identidad. No significa que esos públicos sean idénticos; se necesitaría Analytics para medirlo.

Los títulos usan primera persona y verbos concretos («entré», «me enamoré»), superlativo («peor», «más salvaje»), pregunta útil («cuánto cuesta»), incertidumbre («renunciaré») y relaciones («mis hermanas»). El conflicto y la recompensa cambian entre episodios de una misma gira. No describimos la imagen de portada desde estos textos.

La descripción del video de reflexión conecta ocho años de viaje y 117 países con una nueva meta de 150, y pide al público opinar sobre continuar viajando. Son declaraciones de la creadora, no validaciones independientes de cada país. El video de costo de vida anuncia supermercado, gasolina, transporte, servicios, restaurante, gimnasio y vivienda, además de testimonios callejeros; la pregunta de cierre solicita una opinión económica. El de Isla Larga sitúa la acción en Puerto Cabello y en una salida con hermanas y padres. Así el episodio familiar conserva anclas de destino y turismo, no depende sólo de intimidad.

### Frecuencia y desempeño con límites

Las ocho publicaciones observadas alternan jueves y domingo. Siete intervalos: 3, 4, 3, 4, 3, 4, 3 días. Periodo de 24 días y 2,04 publicaciones/semana. Es una cadencia demostrada en esta ventana; no se extrapola automáticamente a todo 2026 ni a Instagram. Las duraciones varían de 16:24 a 30:50, mediana 22:40 usando segundos del reproductor. Algunas etiquetas de tarjeta redondean un segundo más; se conservaron tal como aparecen.

«El peor viaje...» (10-sep) suma 1 849 097 vistas y es también el más antiguo de los ocho; el safari (20-sep) suma 627 970. El último familiar (4-oct) suma 422 266 en aproximadamente dos días; no hay medición histórica suficiente para compararlo a igual edad con los anteriores. No debe usarse la división vistas/días como una tasa de crecimiento actual ni inferirse CTR.

### Hipótesis aplicables, por probar

La gira puede organizarse como una temporada con una pregunta distinta por entrega: experiencia, rutina local, costo, cultura y consecuencias personales. Un canal nuevo necesita entregar contexto en cada episodio para quien llega desde recomendaciones y no vio los anteriores. La alternancia emocional/utilitaria es una hipótesis atractiva si el mismo personaje sigue siendo reconocible. La cadencia de dos videos por semana requiere un colchón de grabación y edición; copiarla sin ese margen sería una propuesta de producción, no una conclusión de estos datos.

Instagram: fuentes indexadas secundarias muestran captions con CTA a video completo de safari y al canal para Zanzíbar, así como marca de swimwear y hotel; **no cuentan como muestra primaria validada**, por lo que se excluyen de frecuencia y métricas hasta evidencia Browser. Miniaturas: pendientes de evidencia visual.
'''
lvdv='''## 3. La Vida de Viaje — referencia de nicho y sistema transmedia histórico

Fuentes: [quiénes somos, sitio propio](https://lavidadeviaje.com/quienes-somos/), [YouTube enlazado](https://www.youtube.com/lavidadeviaje/videos), [Instagram enlazado](https://www.instagram.com/lavidadeviaje/). El proyecto identifica a Andrés Calla y Jime Sánchez y define movimiento lento en naturaleza; menciona bicicleta, kayak, caminatas y casa rodante. El contraste con vlogs generalistas es útil para decidir especialización.

### Muestra primaria de la pestaña Videos

'''+table('La Vida de Viaje')+'''

### Observaciones de contenido y empaque textual

La muestra de julio 2021 encadena Rio Pinto, El Algarrobal y Al Pie del Nevado en pares trailer/episodio. El trailer antecede al episodio 2, 3 y 3 días, respectivamente. No se asume que funcionara como Short: YouTube los muestra aquí como Videos, con duraciones de aproximadamente un minuto. Los episodios usan lugar concreto y la etiqueta cicloturismo. Es un empaque basado en ruta/actividad que facilita identidad de nicho, con menos promesa emocional explícita que Vero o PlanetaJuan.

Las descripciones dirigen a la comunidad del blog y declaran embajadores Venzo/Spot Latam. El clip de glamping pide leer el artículo completo en el blog; la web concentra guías, historias, destinos, libros, contacto para marcas y newsletter. El canal puede funcionar como una pieza de un ecosistema editorial. No se conoce el tráfico ni la conversión entre piezas.

El [catálogo de películas propio](https://lavidadeviaje.com/peliculas/) además documenta cuatro obras: [Manifiesto](https://www.youtube.com/watch?v=06l2rF5Mkok), 2020, 10 minutos; [Alsur: Tierra del Fuego en bicicleta](https://www.youtube.com/watch?v=FTitVUsknNk), 2019, 22 minutos; [12 Días, bikerafting río Santa Cruz](https://www.youtube.com/watch?v=saXl41bN8ms), 2018, 36 minutos; [1247, Carretera Austral](https://www.youtube.com/watch?v=hq-_oosSj4I), 2017, 40 minutos. Años/duraciones proceden del catálogo del creador y son aproximados; no se verificaron fechas exactas ni vistas de esos cuatro. Las descripciones de obra ofrecen un viaje, una búsqueda y una transformación, no sólo una lista turística. Las selecciones en Banff se atribuyen a la web del autor, sin verificación independiente del festival.

### Frecuencia y desempeño con límites

El último video encontrado es de julio 2024 y el anterior de septiembre 2021. Esto indica inactividad de esta pestaña en 2026. Un cálculo mecánico de los ocho últimos mezclaría una campaña de 2021 con enormes pausas y sería engañoso como cadencia operativa. **Frecuencia actual: ND; no activo en la muestra.**

Durante la serie 1–18 julio 2021 hay seis piezas en 17 días, tres episodios y tres trailers. Si se describe esa campaña histórica, aparecen cinco intervalos de 2, 4, 3, 5 y 3 días; no es la frecuencia actual. Los episodios acumulan entre 1 749 y 2 950 vistas y los trailers entre 371 y 600. El mayor tamaño de las películas o el prestigio de festival no permite concluir rendimiento comercial del canal.

### Hipótesis aplicables, por probar

Un canal nuevo de viajes puede escoger una experiencia distintiva —bicicleta, caminatas, transporte público, campamentos— y repetir la actividad con destinos diferentes. Eso crea un motivo para volver más concreto que «viajamos». Un trailer debe entregar valor por sí mismo y dar una razón para abrir el episodio; la mera existencia de pares no demuestra que el puente haya convertido. Un blog/guía descargable es útil si responde preguntas que no caben en el relato, pero necesita inversión propia y medición.

Miniaturas e Instagram: pendientes de evidencia visual y fechas. No confundir La Vida de Viaje con La Vida **en un** Viaje ni con La Vida de M: son identidades distintas.
'''
juan='''## 4. PlanetaJuan — viaje serializado y producto editorial propio

Fuentes: [YouTube oficial](https://www.youtube.com/@planetajuan/videos), [Instagram enlazado desde descripciones](https://www.instagram.com/planetajuan/), [Linktree del creador](https://linktr.ee/planetajuan). Se incorpora como cuarto caso para añadir una referencia activa frente a los dos proyectos históricos. Es creador individual y no un canal de pareja.

### Muestra primaria

'''+table('PlanetaJuan')+'''

### Observaciones de contenido y empaque textual

Seis de los ocho títulos cubren una gira de Turkmenistán y Uzbekistán, más un ranking de países y una pieza histórica sobre Ruta de la Seda. El paso «entré → otra cara → frontera → descubrimiento del país siguiente» convierte una ruta geográfica en varios conflictos editoriales. Las promesas son de curiosidad («raro y absurdo»), acceso («no quieren que veas»), transición («escapando por la frontera»), sorpresa («no es como creía») e interacción social («me quieren buscar mujer»).

Hay mayúsculas selectivas, banderas y emojis; en esta muestra no aparece una numeración de episodios en el título. La secuencia puede consumirse como temporada pero cada video contiene una promesa independiente. En comparación con Misias, pesa más qué descubrirá el espectador que cómo planear su propio itinerario. Esta es una clasificación de títulos, no un conteo de todos los minutos de contenido.

Las ocho descripciones presentan un bloque comercial repetido con libro, Holafly, Surfshark, escuela de inglés/francés, membresía del canal y cuentas sociales. Su [Linktree](https://linktr.ee/planetajuan) ofrece los libros Migrantes e Inadaptados, audiolibro y varios distribuidores. Es evidencia de un ecosistema editorial y educativo con afiliación; las ventas, comisiones y participación de cada fuente son ND. La mención de membresía es una oferta visible y no permite inferir número de miembros pagadores.

### Frecuencia y desempeño con límites

Ocho publicaciones abarcan 32 días, del 2-sep al 4-oct-2026: intervalos 4, 7, 3, 4, 7, 3, 4 días en orden cronológico; mediana 4 días; 1,53 publicaciones por semana. Predominan domingo y miércoles, pero hay semanas con una sola entrega; no se presenta como dos por semana constante. La mediana de duración es 32:01,5 a partir de segundos; una entrega supera una hora y otra ronda 22 minutos, por lo que hay flexibilidad según promesa.

El ranking «Top 5 países...» suma 3 269 148 vistas, seguido del primer video de Turkmenistán con 2 374 883. Ambos son los más antiguos de los ocho. En Uzbekistán las entradas más recientes suman de 314 923 a 810 353; comparar directamente no demostraría menor interés del país. Para evaluar paquetes, se necesitaría seguir las vistas al mismo día 2/7/28 de cada publicación.

### Hipótesis aplicables, por probar

Una ruta puede descomponerse antes de viajar en episodios con conflictos diferentes; no hay que esperar a la edición para inventar el título. Un nuevo creador puede usar contraste expectativa/realidad y diálogo local sin depender de lugares de acceso complicado o de viajes caros. Si se ofrece un producto propio, conviene que comparta la misma promesa central del canal; este caso muestra convivencia de libro, idioma y migración/viaje, pero no prueba cuál funciona mejor.

Miniaturas e Instagram: pendiente de evidence Browser para describir imágenes y muestra de publicaciones.
'''
closing='''## Qué medir en nuestro canal sin confundir benchmark con causalidad

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
- Los perfiles y cada video se enlazan en las tablas; son fuentes primarias. El buscador puede mostrar cifras obsoletas y por eso no se usó para los contadores de estas tablas.
'''
pathlib.Path('investigacion/02_parejas_nomadas.md').write_text(intro+'\n'+misias+'\n'+vero+'\n'+lvdv+'\n'+juan+'\n'+closing)
print('written',len((intro+misias+vero+lvdv+juan+closing).split()),'words')
