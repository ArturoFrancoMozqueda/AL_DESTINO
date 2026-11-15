# Gráficos, transiciones y movimiento · v0.1 · BORRADOR

Fuente visual: `marca/manual.md` y tokens v0.6. Recursos nuevos en `marca/video/v01/`; exportaciones en `marca/exportaciones/video-v01/`. El catálogo enlaza iconos, fuentes SVG de componentes y especificaciones de movimiento. No reemplaza logos ni animaciones vigentes.

Preferencia expresa de Arturo, 14 de noviembre de 2026: profesional y elegante, tomando el [video elegido como referencia](referencia-video.md). Propuesta de aplicación: placas limpias, jerarquía tipográfica, espacio, acentos medidos y movimiento preciso. La serif puede distinguir la presentación; Plus Jakarta Sans sigue llevando los datos. La forma, tamaño y timing de cada muestra siguen BORRADOR.

## Familia gráfica propuesta

Iconos de línea, extremos redondos, rejilla 32 × 32, trazo 1.8. Las flechas tienen una curvatura suave propia; no simulan un mapa preciso. PNG transparentes en café oscuro, arena y turquesa; SVG fuente con `currentColor`. Emplear café/arena o arena/petróleo para datos pequeños. Terracota/turquesa como detalles, comprobando contraste sobre la toma. No depender de rojo/verde para expresar una opinión.

Un gráfico debe localizar, explicar, atribuir o comparar. Mostrar el mínimo necesario. Mantener un dato protagonista por placa. Evitar rótulo + subtítulos + valoración + precio simultáneos; desplazar o escalonar según el audio. Los iconos acompañan texto cuando su significado sea ambiguo.

## Componentes iniciales

| ID | Campos editables deseados | Uso y condición |
|---|---|---|
| `lugar` | nombre, ciudad/categoría, icono | Primera referencia clara al sitio o cambio de lugar. No repetir en cada corte. |
| `precio` | importe, moneda, unidad, fecha y condiciones | Junto a la mención o demostración. No mostrar importe sin qué incluye ni fuente/fecha. |
| `consejo` | título breve, dato, icono | Consejo práctico comprobado; no opinión inventada. |
| `opinion` | autor, criterio, comentario, pulgar opcional | Atribuir a quien lo dijo. Pulgar arriba/abajo = opinión contextual, no nota objetiva ni consenso. |
| `presentacion` | Arturo, Liz, descripción opcional | Primer contexto/conversación; no ocupa la apertura entera. |
| `cierre` | pregunta o mensaje, cuenta opcional | Cierre de la historia; cuenta/URL sólo confirmada. Reutilizar el logo existente si aporta. |

Los SVG de componentes son muestras con capas identificadas y textos de ejemplo editables en su fuente. Los PNG son referencias visuales aplanadas; Clipo debe colocar texto, fondo e icono por separado cuando sus herramientas lo permitan. Mapas/rutas, QR y rótulos de plataforma se diseñarán cuando tengamos el contenido concreto. `redes` es un icono genérico de cámara; no es el logo oficial de Instagram.

## Posición y lectura

Maestro de trabajo propuesto: 1920 × 1080 para el largo. Margen interior inicial 96 px; componente preferente abajo a izquierda, salvo caras, acción o subtítulos. Datos de lectura desde 36 px de la marca; dato protagonista 60–72 px según longitud. Las etiquetas secundarias de los mockups ensayan 28 px: si no se leen en el encuadre real, ampliar o acortar, sin perder datos necesarios. Estos puntos de partida se prueban a escala de teléfono; no son zonas oficiales de todas las plataformas. En vertical, hacer otra composición conforme a los márgenes de trabajo del token, no reducir la horizontal entera.

Duración visible: suficiente para leer a voz natural y volver a mirar la escena. Probar 3–5 s para un rótulo breve y 5–7 s para un precio con condiciones; acortar contenido antes de encoger texto. Entrada/salida son adicionales a la pausa de lectura. Los presets del JSON usan tiempo relativo al comienzo de cada pieza; el plan del episodio fija su tiempo absoluto.

## Movimiento propuesto

| ID | Construcción | Uso |
|---|---|---|
| `aparecer` | Opacidad 0→1 en 180 ms; salida de 140 ms. | Datos secundarios sin llamar demasiado la atención. |
| `deslizar` | Traslado local X de −24→0 px y opacidad 0→1 en 240 ms; salida de 160 ms. | Lugar, consejo, presentación. Mantener texto estable durante la lectura. |
| `enfatizar` | Escala 0.96→1 y opacidad 0→1 en 220 ms, sin rebote ni loop. | Precio o una valoración puntual; no animar cada cifra de la escena. |
| `trazar` | Longitud visible de trazo 0→1 en 360 ms; pausa; fade de 140 ms. | Flecha que señala algo visible. Requiere máscara/revelado real. Si no existe, usar aparición del icono completo y declarar la adaptación. |

Easing creativo deseado de entrada: ease-out; salida: ease-in. La equivalencia depende del editor. No afirmar una curva exacta cuando el MCP sólo expone un easing genérico. Las piezas dentro de un rótulo pueden entrar como conjunto; separación de capas se conserva para futuros ajustes. No animar continuamente elementos de lectura. Presets en `motion.json` son especificaciones, sin render ni validación todavía en Clipo.

## Transiciones entre tomas

| Recurso | Propuesta de uso | Punto de partida |
|---|---|---|
| Corte directo | Cambio de encuadre/acción/idea dentro de la experiencia. | Sin efecto. Elegir el fotograma por continuidad. |
| Puente de audio J/L | Conversación sobre tomas de apoyo o anticipo de la siguiente escena. | Ajustar por frase y ambiente, sin duración fija. |
| Fundido | Elipsis o pausa de paisaje cuando el contraste temporal tenga sentido. | 8–12 fotogramas a 30 fps; ajustar a la toma. |
| Corte por correspondencia | Una forma, gesto o dirección enlaza dos planos existentes. | Alinear la acción. No necesita una transición gráfica. |
| A negro | Cierre de bloque o elipsis explícita. | Breve y deliberado; evitar entre todos los sitios. |

Whips, flashes, glitches y zooms fuertes quedan para propuestas específicas cuando la escena los justifique; no hay obligación de usarlos ni se consideran prohibidos. La alternancia entre planos y la comprensión de la experiencia llevan el ritmo principal.

## Cómo revisar esta versión

Primero juzgar forma de iconos, jerarquía, cantidad de información y voz de los rótulos en la mesa visual. Después probar lectura sobre una toma propia. Finalmente ajustar velocidad/curva con una muestra de movimiento en Clipo. Registrar si el cambio es una preferencia declarada, una hipótesis o un resultado observado. El tablero tipográfico no demuestra integración ni fidelidad de una animación ejecutada.
