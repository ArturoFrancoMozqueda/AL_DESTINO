> Arturo rechazó estas conversiones y pidió producir aquí. No usar como bases recomendadas. La revisión actual está en [Aplicaciones v0.3](../v03-aplicaciones/index.html). Los enlaces se conservan como historial; no se borraron diseños de la cuenta.

# Canva · HISTORIAL DESCARTADO

Las ocho bases se crearon con el conector Canva a partir de previews del kit. Son diseños guardados de trabajo, no publicaciones ni Brand Templates con campos de autofill. Se mantienen los enlaces/IDs en `canva-designs.json`.

| Pieza | Diseño editable | Maestro local |
|---|---|---|
| YT02-comida | [Abrir Canva](https://www.canva.com/d/A8NW5ulu5E3IAn0) | [SVG](plantillas/YT02-comida.svg) |
| YT01-lugares-hoteles | [Abrir Canva](https://www.canva.com/d/JaeXvhYPzwWiidr) | [SVG](plantillas/YT01-lugares-hoteles.svg) |
| YT03-vlog-lifestyle | [Abrir Canva](https://www.canva.com/d/RmTmRD28QYaE__y) | [SVG](plantillas/YT03-vlog-lifestyle.svg) |
| YT-banner | [Abrir Canva](https://www.canva.com/d/NCvxlfGoAVRJMB6) | [SVG](plantillas/YT-banner.svg) |
| avatar | [Abrir Canva](https://www.canva.com/d/bSljFw9kL5YxvSJ) | [SVG](plantillas/avatar.svg) |
| vertical-portada | [Abrir Canva](https://www.canva.com/d/eaDUm4h_D3pRPVZ) | [SVG](plantillas/vertical-portada.svg) |
| video-rotulo-lugar | [Abrir Canva](https://www.canva.com/d/cgWBH8BYOJc2f0w) | [SVG](plantillas/video-rotulo-lugar.svg) |
| video-tarjeta-consejo | [Abrir Canva](https://www.canva.com/d/MbXvz5Yf2v32wpx) | [SVG](plantillas/video-tarjeta-consejo.svg) |

## Flujo de edición

1. Duplicar la base elegida para el episodio. Mantener la base como referencia.
2. Sustituir el paisaje abstracto por una fotografía propia y ajustar el encuadre.
3. Cambiar textos; aplicar Cormorant Garamond Semibold y Plus Jakarta Sans cuando Canva no haya conservado la fuente. Las licencias y archivos oficiales están en `assets/fuentes/`.
4. Cotejar logo contra el SVG local. Si la conversión lo convirtió en texto u objetos deformados, eliminarlos y subir `assets/monograma-borrador.png` o `assets/logo-horizontal-borrador.png`; no escribir «AL» para imitarlo. El original PNG heredado está en `originales/extraido/AL_DESTINO_Design_System_v0.1/02_Logos_PNG/`.
5. Revisar composición y tamaño. Los diseños de miniatura convertidos son 1280×720; el maestro SVG es 3840×2160. Escalar cuando el flujo lo permita o usar la copia ligera dentro de límites de archivo.
6. Quitar placeholders/guías, revisar a tamaño pequeño y guardar proyecto + exportación + fuente de fotos.

## Verificación y limitaciones

Inspeccioné la conversión de YT02: cinco regiones de texto y seis rellenos de imagen editables, página 1280×720. La conversión interpretó parte del monograma como texto «al» y alteró algunos detalles. Esa limitación exige cotejo de las otras piezas; no se afirma fidelidad de marca ni transparencia de las conversiones. YT02 procede de la primera prueba, anterior al ajuste del placeholder en el SVG.

Para rótulos, comprobar transparencia antes de superponer en video; si Canva no la conserva o requiere una función no disponible en la cuenta, usar el PNG transparente local o el SVG. La vista previa local permite editar textos y descargar SVG sin Canva, pero no mueve fotografías de forma interactiva.

No se guardaron ediciones mediante transacciones después de inspeccionar: las bases originales convertidas permanecen como borradores. Este kit no crea ni modifica un Brand Kit de la cuenta.
