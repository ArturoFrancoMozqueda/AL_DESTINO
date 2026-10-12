import pathlib
p=pathlib.Path('investigacion/02_parejas_nomadas.md');s=p.read_text()
s=s.replace('La auditoría visual y la muestra de Instagram se documentan por separado cuando Browser entrega evidencia.','La auditoría visual usa capturas Browser y, para dos canales, hojas de contacto de las miniaturas públicas originales. La muestra de Instagram usa URLs y fechas del grid Browser, verificadas con los metadatos públicos de cada publicación seleccionada. No se infiere la imagen a partir de su texto alternativo automático.')
s=s.replace('Miniaturas: ND hasta revisión visual. Instagram: cuenta verificada por enlaces cruzados; muestra de posts y frecuencia ND si Browser no aporta fechas.','Miniaturas e Instagram: verificados en las secciones de evidencia visual y multiplataforma al final. El grid incluye piezas antiguas en primeras posiciones; no representa por sí solo un orden cronológico completo.')
s=s.replace('Instagram: fuentes indexadas secundarias muestran captions con CTA a video completo de safari y al canal para Zanzíbar, así como marca de swimwear y hotel; **no cuentan como muestra primaria validada**, por lo que se excluyen de frecuencia y métricas hasta evidencia Browser. Miniaturas: pendientes de evidencia visual.','Instagram: tres publicaciones primarias seleccionadas confirman remisión a YouTube y presencia de marca de swimwear; se detallan al final. Las miniaturas se inspeccionaron en la captura Browser compartida y se describen en evidencia visual.')
s=s.replace('Miniaturas e Instagram: pendientes de evidencia visual y fechas. No confundir La Vida de Viaje con La Vida **en un** Viaje ni con La Vida de M: son identidades distintas.','Instagram confirma retorno editorial en mayo 2026, aunque YouTube permanece sin nuevas publicaciones en la muestra. El grid mezcla piezas de 2021, 2022 y 2026: no permite calcular frecuencia actual. Miniaturas inspeccionadas en captura Browser. No confundir La Vida de Viaje con La Vida **en un** Viaje ni con La Vida de M: son identidades distintas.')
s=s.replace('Miniaturas e Instagram: pendiente de evidence Browser para describir imágenes y muestra de publicaciones.','Miniaturas e Instagram verificados con tres piezas primarias seleccionadas por plataforma; detalle en las secciones siguientes.')
extra='''## Evidencia visual: 12 miniaturas inspeccionadas

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

'''
s=s.replace('## Qué medir en nuestro canal sin confundir benchmark con causalidad',extra+'## Qué medir en nuestro canal sin confundir benchmark con causalidad')
s=s.replace('- `extract_public_channels.py`: extracción reproducible limitada a datos públicos de la primera página de la pestaña Videos.','- `extract_public_channels.py`: extracción reproducible limitada a datos públicos de la primera página de la pestaña Videos.\n- `02_instagram_posts.json`: 12 publicaciones primarias, fechas del grid y metadatos/captions públicos.\n- `00_instagram_grids.json` y `evidencia/ig_*.txt`: evidencia de grid recolectada por Browser.\n- `evidencia/miniaturas_*`: imágenes inspeccionadas para los cuatro casos.')
p.write_text(s)
print(len(s.split()),'words')
