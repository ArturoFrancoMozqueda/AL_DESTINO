# Verificación de edición horizontal v1.0 · Registro histórico

Este registro documenta la prueba del 16 de noviembre de 2026. Se conserva fuera de la skill activa; no debe cargarse para preparar cada montaje.


Contraste realizado el 16 de noviembre de 2026 con el piloto existente `ad-0001`. Es una comprobación directa del autor de la actualización, sin evaluación independiente ni nuevo montaje. Los IDs reales y rutas privadas permanecen locales.

| Comprobación efectuada | Resultado y consecuencia para el procedimiento |
|---|---|
| Conexión, catálogo y carga real en Clipo | El proyecto guardado de Pátzcuaro abrió con 22 clips, 135.9 s y cero medios ausentes. La copia personal de la skill todavía era v0.1: debe sincronizarse con la fuente vigente. |
| Integridad temporal del proyecto leído | Los 22 clips tienen assets y límites válidos; textos y overlays quedan dentro de duración. Esto acredita esos cálculos, no continuidad narrativa ni privacidad de todos los fotogramas. |
| Solapamiento de subtítulos | Dos entradas del piloto comparten 0.12 s alrededor de 01:45.57. La comprobación no permite declararlo terminado; exige corregir o justificar esa composición. Se deja localizado sin modificar el montaje en esta tarea. |
| Búsqueda y captura a 01:13 | El cabezal se actualizó antes que la imagen; la primera captura mostró otro plano. Tras consultar estado y volver a capturar apareció Liz dando el bocado esperado. Se incorpora la comprobación de imagen realmente decodificada. |
| Plan histórico frente al contrato actual | Tiene 15 medios y 22 selecciones, pero carece de `source_coverage`, `story_beats`, `technical_checks` y `exclusions` del contrato posterior. Se conserva como antecedente; no demuestra cobertura completa ni se rellena retroactivamente. |
| Catálogo tipográfico actual | Cormorant Garamond y Manrope disponibles; Plus Jakarta Sans no figura en el catálogo leído. Una adaptación técnica debe documentarse y no cambia la marca. |
| Recuperación del artefacto final previo | Trabajo de exportación persistido `completed`, artefacto 1920 × 1080, 135.914667 s, 138795151 bytes; SHA-256 `8ce0d23dcf562bee6e535aa3b72bbf83c6e6b2412acc5596ece278f2e54d6a9b`. Recuperado a archivo temporal con verificación del MCP. Es el render previo del piloto, no una exportación nueva. |
| Inspección local de ese archivo | FFprobe confirmó H.264/AAC, 1920 × 1080, duración y tamaño; SHA-256 local coincide con el recibo. Se decodificaron e inspeccionaron imágenes de 01:13 (bocado de Liz) y 02:13 (firma final). Son muestras; no certifican todo el acabado ni el sonido. |
| Audio y estudio de referentes | Sigue sin escucha crítica en esta sesión. Una consulta gratuita de vidIQ volvió a devolver `Unknown tool`. La revisión visual permanece parcial y el piloto mantiene su pendiente de escucha. |

La versión operativa de estas instrucciones permite producir, revisar y cerrar encargos con condiciones explícitas. La prueba del piloto detecta pendientes que el flujo debe conservar hasta resolverlos; no aprueba ese video ni certifica todas las capacidades del editor.

Comprobación documental: `scripts/validar.py` sin fallos. El validador de skill-creator no inicia porque falta PyYAML en los Python disponibles; no se instalaron herramientas para esa comprobación documental. La validación del repositorio sí comprueba frontmatter básico, nombre, descripción, ausencia de scaffold y enlaces locales. El resultado exacto de la ejecución final se informa en la entrega.
