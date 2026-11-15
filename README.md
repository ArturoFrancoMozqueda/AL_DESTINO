# AL DESTINO · Arturo y Liz

Repositorio para investigar, crear, editar y revisar contenido. **BORRADOR · marca v0.6 · kit de edición v0.1.** Una fuente vigente no equivale a aprobación final.

## Entradas principales

- **Ver la marca completa:** [design system](marca/design-system.html), con logos, ambas animaciones y acceso al módulo de video.
- **Trabajar con el agente:** [AGENTS.md](AGENTS.md) y [mapa del proyecto](proyecto.json).
- **Elegir recursos:** [índice común](marca/recursos.json), con fuentes, exportaciones y límites de uso; [mesa de video](marca/video/v01/index.html).
- **Producir un episodio:** [flujo](produccion/flujo.md) y [catálogo de episodios](produccion/episodios/catalogo.json).

## Qué usar para cada tarea

| Tarea | Ruta |
|---|---|
| Ideas, guiones, copies, títulos, miniaturas y adaptación social | [Skill de contenido](.agents/skills/al-destino-contenido/SKILL.md) |
| Planes locales y restaurantes | [Skill local](.agents/skills/al-destino-local/SKILL.md) |
| Alojamientos Airbnb | [Skill Airbnb](.agents/skills/al-destino-airbnb/SKILL.md) |
| Hoteles de playa | [Skill hoteles](.agents/skills/al-destino-hoteles-playa/SKILL.md) |
| Historia, hooks, montaje, audio, color, gráficos y motion | [Skill de edición](.agents/skills/al-destino-edicion/SKILL.md) |
| Identidad y reglas gráficas | [Manual](marca/manual.md), [tokens](marca/tokens/brand_tokens.json), [mapa de marca](marca/LEEME.md) |
| Evaluar esfuerzo y resultados propios | [Plantilla de resultados](resultados/plantilla-episodio.json) |

Arturo desarrolla Clipo y su MCP. El paquete editorial define qué montar y qué recursos aplicar; la conexión se comprueba al ejecutar una tarea. La disponibilidad de un gráfico o APNG no garantiza que un editor lo reproduzca correctamente.

## Organización

| Carpeta | Contenido |
|---|---|
| `contexto/` | Perfil, visión, preferencias e historial de decisiones |
| `investigacion/` | Metodología, fuentes y consultas guardadas |
| `planificacion/` | Oportunidades, ideas y carteras; sin calendario aprobado |
| `produccion/` | Plantillas, episodios y planes de montaje |
| `marca/` | Guía visual pública, recursos compartidos, aplicaciones y fuentes |
| `.agents/skills/` | Skills específicas que reutilizan las fuentes anteriores |
| `resultados/` | Métricas propias y aprendizaje; sin resultados inventados |
| `scripts/` y `validacion/` | Generación reproducible y evidencia de comprobaciones |

`marca/archivo/`, ZIPs y carpetas `originales/` conservan antecedentes. No se usan por defecto para crear piezas nuevas. La ruta histórica `v05-png` se mantiene compatible, aunque su catálogo contiene la revisión de marca 0.6.

`marca/` se publica mediante el workflow de Pages existente al hacer push a `main`. Mantener allí sólo recursos públicos de marca. Las grabaciones, rutas personales y archivos locales se mantienen fuera de Git; ver el flujo y `.gitignore`. Una propuesta no autoriza publicar, contactar, reservar, comprar ni programar.

## Comprobar el repositorio

Sin dependencias adicionales para validar:

```sh
python3 scripts/catalogar-recursos.py --check
python3 scripts/validar.py
```

En Windows: `py -3 -X utf8 scripts/validar.py`. Si cambian recursos, regenerar primero el índice con `python3 scripts/catalogar-recursos.py`. Los generadores y dependencias opcionales están en [herramientas](scripts/LEEME.md). La validación de integridad no sustituye revisión editorial, escucha ni prueba de exportación.
