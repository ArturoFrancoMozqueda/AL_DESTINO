# Firma por piezas · BORRADOR

Variante de 4 s, 1920 × 1080, 30 fps, sin audio. Se reutilizan las 15 piezas raster originales; el apoyo de contraste está detrás de su alfa, sin placa ni recolor del frente. La ola, el sol y el lettering tienen entradas coordinadas, pausa de lectura y salida a transparencia.

Entregables en `renders/`: APNG, WebM con alfa, poster y 120 PNG RGBA. El APNG reproduce una vez; el WebM dura 4 s. No son el episodio reexportado y su importación/decodificación en Clipo sigue pendiente. La comparación privada sobre fotogramas del viaje vive con ad-0001.

También se entrega monograma animado de 528 × 320 para firma en esquina: mismo movimiento recortado, sin divisor ni nombre. `renders/monograma-png/` conserva sus 120 PNG. El recorte sobre el maestro 1920 × 1080 es x=280, y=384, ancho=528, alto=320. Se comprobó que el movimiento queda dentro de esos límites. Para reproducirlo, crear esa carpeta y exportar la secuencia con `ffmpeg -framerate 30 -start_number 1 -i renders/secuencia-png/frame_%06d.png -vf crop=528:320:280:384 -pix_fmt rgba -start_number 1 renders/monograma-png/frame_%06d.png`; convertirla después con los mismos comandos de APNG/WebM y los nombres del catálogo.

## Reproducción

Desde la raíz del repo, `node scripts/generar-logo-premium.cjs` reconstruye la fuente, las copias verificadas de las piezas y el sidecar de movimiento. La generación no renderiza. Después, desde esta carpeta:

```powershell
npx --yes hyperframes@0.9.58 check . --snapshots
npx --yes hyperframes@0.9.58 render --format png-sequence --output renders/secuencia-png --fps 30 --quality delivery --workers 2
ffmpeg -framerate 30 -i renders/secuencia-png/frame_%06d.png -plays 1 -f apng -y renders/AL-DESTINO-firma-premium.png
ffmpeg -framerate 30 -i renders/secuencia-png/frame_%06d.png -c:v libvpx-vp9 -pix_fmt yuva420p -lossless 1 -auto-alt-ref 0 -row-mt 1 -threads 4 -an -y renders/AL-DESTINO-firma-premium.webm
```

El catálogo del render es un recibo de comprobaciones fechadas, no una garantía automática de una nueva exportación. Tras cambiar la fuente, volver a renderizar y verificar duración, alfa, fotogramas, poster, hashes y muestras compuestas antes de actualizar ese recibo y `marca/recursos.json`.

Se consultó la primitiva `logo-outro` del catálogo local. Su asamblea por piezas sirvió de contraste; la fuente final adapta el movimiento a nuestro raster existente, sin copiar el logo de muestra, glow amplio ni pastilla de URL. La primitiva de consulta permanece en la caché ignorada del proyecto anterior.

HyperFrames se actualizó de 0.8.145 a 0.9.58 y ambas composiciones pasaron `check`. La captura usó hardware GPU y modo screenshot, con 120 fotogramas en unos 14 s. El aviso de primer frame vacío es deliberado: es un overlay que entra desde transparencia; se entrega poster aparte. El sidecar verifica entradas, orden y permanencia en cuadro. No se verificó audio porque este recurso no lo contiene.
