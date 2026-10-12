# AL DESTINO · animación por elementos · BORRADOR

Cada parte del logo tiene una capa PNG y una entrada propia. A desde izquierda, L desde arriba, sol ascendente, ola horizontal, divisor vertical, nueve letras del nombre secuenciales y tagline final. Se utiliza el raster original, sin reemplazar el lettering. La extracción del pie compartido A/L y los bordes sigue siendo una propuesta revisable.

- `index.html`: composición HyperFrames editable; registro de timeline `al-destino-logo`.
- `assets/piezas/`: capas PNG usadas por el render.
- `renders/AL-DESTINO-logo-animado.png`: APNG RGBA, 1920 × 1080, 30 fps, 96 fotogramas, 3.2 segundos, repetición continua y sin audio.
- `renders/secuencia-png/`: los mismos 96 fotogramas RGBA, renderizados por HyperFrames.
- `renders/logo-poster.png`: pose final sobre arena para comprobar legibilidad.
- `snapshots/por-elementos/`: poses y mapa de keyframes comprobados.
- `archivo/`: revelación en bloque descartada; no es la animación vigente.

Las zonas ocultas por la ola no se reconstruyen. Los PNG mantienen la geometría visible y las coordenadas del original. El APNG necesita un visor que reproduzca PNG animado; la secuencia conserva los fotogramas para otros editores. Editar en el Studio local con `npx --yes hyperframes@0.8.145 preview --background --port 3017`.
