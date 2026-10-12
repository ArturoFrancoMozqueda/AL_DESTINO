# Marca · mapa de archivos · BORRADOR

La entrada vigente es [design-system.html](design-system.html). El [manual](manual.md) y los [tokens JSON](tokens/brand_tokens.json) describen la misma versión v0.5.

| Material | Ubicación y uso |
|---|---|
| Fuentes de identidad | `assets/fuentes/` y `assets/logos/`; conservar las licencias y el original |
| PNG separados | [Catálogo](exportaciones/v05-png/index.html): logos, firma, paleta, tipografía, composición, historias, notas, redes y láminas |
| Animación por piezas | [PNG animado](motion/logo-al-destino/renders/AL-DESTINO-logo-animado.png) y [composición editable](motion/logo-al-destino/index.html) |
| Secuencia animada | `motion/logo-al-destino/renders/secuencia-png/`: fotogramas RGBA numerados |
| Investigación de redes | [Registro de fuentes](investigacion-redes.json) y [formatos](formatos-y-fuentes.md) |
| Control visual | `previews/`: capturas de escritorio y móvil del sistema vigente |
| Fuentes heredadas | `originales/`: no modificar ni interpretar “aprobado” como decisión actual |
| Revisiones anteriores | [Archivo histórico](archivo/LEEME.md); no usar automáticamente como identidad vigente |

Las piezas del logo son PNG extraídos de los píxeles visibles del raster original. No constituyen un vector maestro. Se conservan aparte el original con fondo claro y la propuesta con transparencia. El límite entre A/L en el pie compartido y la compensación del matte son decisiones de extracción documentadas en `assets/logos/piezas/catalogo.json`; no se han reconstruido partes ocultas por la ola.

El PNG animado es un APNG con extensión `.png`. La secuencia PNG permite reutilizar la animación como fotogramas sin depender de un reproductor APNG. Todo entregable sigue BORRADOR.

La entrada principal es una guía esencial concisa, con animación reproducible en la propia página. `guia-detallada.html` conserva las pruebas de contraste, tipografía, recortes y exploraciones completas.

## Entrega organizada · 12 de octubre de 2026

[Kit completo descargable](exportaciones/AL-DESTINO-kit-marca.zip) y [catálogo de todos los PNG](exportaciones/index.html).

- `assets/logos/`: original conservado y piezas transparentes fuente.
- `exportaciones/v05-png/logos/`: logo horizontal, monograma y avatar circular PNG.
- `motion/logo-al-destino/`: composición horizontal y sus renders.
- `motion/logo-circular/`: composición circular y sus renders.
- `exportaciones/`: ZIP completo, ZIP de los 72 elementos y ZIP independiente por animación.
- `tokens/`: JSON y CSS vigentes.
- `archivo/` y `originales/`: historial y fuentes, separados de recursos vigentes.

El ZIP completo organiza `01-logos`, `02-animaciones/horizontal`, `02-animaciones/circular`, `03-elementos-png` y `04-tokens`; incluye manifiesto SHA-256. Para reconstruirlo tras cambiar recursos: `python3 scripts/empaquetar-marca.py`. Todo sigue BORRADOR.
