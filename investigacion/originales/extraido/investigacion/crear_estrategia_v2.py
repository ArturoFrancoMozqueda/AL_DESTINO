from pathlib import Path
import json,re,html,statistics,datetime,unicodedata,base64,shutil
from html.parser import HTMLParser
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,LongTable,TableStyle,Image,KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader,PdfWriter

BASE=Path(__file__).resolve().parent.parent
SRC=BASE/'investigacion';OUT=BASE/'output';TMP=BASE/'tmp/pdfs';TMP.mkdir(parents=True,exist_ok=True)
original=(SRC/'crear_informe.py').read_text()
# Reuse only the presentation helpers; never run the original data writer.
helpers=original[original.index('fontbase=Path('):original.index("story.extend([Spacer(1,35)")]
exec(compile(helpers,'pdf_helpers','exec'))
base_pdfinline=pdfinline
def pdfinline(s):
 s=re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>',r'<a href="\1">',s)
 s=re.sub(r'</?(?:span|small|mark|time|sup)\b[^>]*>','',s)
 s=re.sub(r'<code\b[^>]*>','<code>',s)
 return base_pdfinline(s)

def inner_main(s):
 return re.search(r'<main[^>]*>([\s\S]*?)</main>',s).group(1)
action=(SRC/'07_estrategia_accion.html').read_text()
emerging=(SRC/'04_referentes_emergentes.html').read_text()
audit=inner_main((SRC/'05_auditoria_cuantitativa.html').read_text())
# The audit's full 96-row coding table remains in the linked searchable HTML/JSON.
audit=audit[:audit.index('<h2>Los 96 registros')]
audit=re.sub(r'<div class="filters">[\s\S]*?</div>','',audit)
audit=re.sub(r'<p>Para títulos y miniaturas,[\s\S]*?</p>','<p>Para títulos y miniaturas, consultar las herramientas, requisitos y límites del apartado de distribución y medición.</p>',audit)
distribution=inner_main((SRC/'06_distribucion_medicion.html').read_text())
distribution=re.sub(r'<h1>.*?</h1>','',distribution,count=1)
audit=re.sub(r'<h1>.*?</h1>','',audit,count=1)

scope='''<h2>Cómo leer y usar este informe</h2>
<p>Actualización: 6 de octubre de 2026. Las observaciones de competidores son fotografías públicas a esta fecha. La recomendación es provisional hasta conocer protagonistas, ciudad, recursos y objetivos del canal. No representa una garantía ni una estimación numérica de éxito.</p>
<table><tr><th>Parte</th><th>Para qué sirve</th></tr>
<tr><td>1. Estrategia y ejecución.</td><td>Elegir la promesa, preparar doce ideas, asignar recursos y ejecutar un primer ciclo con seis pilotos.</td></tr>
<tr><td>2. Tres referentes de menor escala.</td><td>Estudiar catálogos regionales, frecuencia y decisiones desde México. Son canales con trayectoria, no una muestra de debuts.</td></tr>
<tr><td>3. Auditoría cuantitativa.</td><td>Interpretar edades, formatos, extremos y comparaciones sin atribuir causalidad a una miniatura o tema.</td></tr>
<tr><td>4. Distribución y medición.</td><td>Diagnosticar elección, atención, continuidad y puentes entre plataformas con documentación oficial.</td></tr>
<tr><td>5. Registro de trabajo.</td><td>Completar una ficha antes de publicar y snapshots a 7/28 días; el archivo JSON conserva campos vacíos.</td></tr>
<tr><td>Anexo. Benchmark original.</td><td>41 páginas: doce creadores, títulos, frecuencias, Instagram, fuentes y galería de miniaturas. Conserva su paginación propia.</td></tr></table>
<p><strong>Prioridad de lectura:</strong> comenzar por la estrategia, presupuesto y calendario; usar la auditoría para evaluar evidencia y el anexo para consultar ejemplos. Las reglas actualizadas del cuerpo principal prevalecen sobre propuestas más generales del primer informe.</p>
<h2>Alcance de la evidencia</h2><p>15 identidades, 114 entradas documentadas en Videos (96 originales y 18 adicionales). La auditoría detallada clasifica las 96 originales: 90 editoriales, tres trailers, un sorteo, un cierre y una pieza breve. Las otras 18 no se incorporaron a esa clasificación ni al cálculo de pares. Por separado, el benchmark original registra 27 Shorts y 39 publicaciones de Instagram con caption.</p>
<p>Se inspeccionaron al menos 36 miniaturas en los doce referentes originales. No se vieron íntegros los 114 videos, no hay transcripciones completas ni analíticas privadas. La estructura se estudia mediante títulos, descripciones, capítulos y secuencias; no se afirma eficacia de aperturas o montaje. En los tres referentes añadidos se verificaron videos y vínculos de identidad en Instagram, sin una nueva auditoría visual o una muestra profunda de sus publicaciones. Su frecuencia de seis publicaciones describe una ventana, no una pauta anual.</p>
<p>La muestra es intencional y tiene sesgo de supervivencia: no incluye una cohorte de proyectos que abandonaron o fracasaron. No mide volumen de demanda, CTR, retención, costos, ingresos, tráfico pagado ni conversiones de competidores. La estrategia controla lo que podemos producir y comprobar; el encaje se debe contrastar con audiencia propia.</p>'''

worksheet='''<h2>Una ficha por episodio</h2><p>Duplicar esta ficha antes de grabar. ND significa que el dato no está disponible; un campo vacío significa que todavía no se registró. No completar datos futuros con valores supuestos. El registro editable está en output/registro_experimentos.json.</p>
<table><tr><th>Momento</th><th>Campo a completar</th><th>Registro</th></tr>
<tr><td>Antes.</td><td>ID / pilar / destinatario / pregunta / promesa.</td><td>________________________</td></tr>
<tr><td>Antes.</td><td>Comparables y preguntas con enlace / prueba diferente.</td><td>________________________</td></tr>
<tr><td>Antes.</td><td>Tope MXN / horas / destino / fecha / conceptos de portada.</td><td>________________________</td></tr>
<tr><td>Después de producir.</td><td>Horas por fase / desembolso incremental / costo total del viaje / incidentes.</td><td>________________________</td></tr>
<tr><td>A 7 días.</td><td>Vistas / impresiones / CTR y consumo por fuente cuando disponible / siguiente video / notas.</td><td>________________________</td></tr>
<tr><td>A 28 días.</td><td>Mismos campos, misma definición / audiencia y formatos separados.</td><td>________________________</td></tr>
<tr><td>Decisión.</td><td>Repetir / rediseñar / inconcluso / aplazar; evidencia, explicación alternativa y siguiente prueba.</td><td>________________________</td></tr></table>
<h2>Revisión antes de una nueva inversión</h2><p>Revisar si la pieza respondió su pregunta, cuánto trabajo requirió y qué señal permite la siguiente decisión. Una portada atractiva sin información sobre distribución o atención no justifica por sí sola un viaje más caro. El tope de recursos se mantiene hasta que una repetición entregue información útil y el equipo pueda sostenerla.</p>'''

sections=[('Estrategia y ejecución',action),('Referentes de menor escala',emerging),('Auditoría cuantitativa',audit),('Distribución y medición',distribution),('Registro de trabajo',worksheet)]
oldhtml=(OUT/'analisis_youtube_instagram_viajes.html').read_text()
oldcss=re.search(r'<style>([\s\S]*?)</style>',oldhtml).group(1)
body='<header><span>ESTRATEGIA EDITORIAL · 6 OCTUBRE 2026</span><h1>Un canal de viajes<br>con un sistema para aprender</h1><p>15 referentes · 114 entradas de Videos · estrategia, recursos y pruebas. Recomendación provisional basada en evidencia pública y documentación oficial.</p></header>'
body+='<nav>'+''.join(f'<a href="#s{i}">{title}</a>' for i,(title,_) in enumerate(sections,1))+'<a href="analisis_youtube_instagram_viajes.html">Benchmark original</a></nav><main><section>'+scope+'</section>'
for i,(title,content) in enumerate(sections,1):body+=f'<section id="s{i}"><h1>{i}. {title}</h1>'+content+'</section>'
body+='<section><h2>Datos y evidencia consultables</h2><p><a href="auditoria_cuantitativa.html">Auditoría completa con filtros de 96 registros</a> · <a href="datos_benchmark_v2.json">Datos consolidados de 114 entradas</a> · <a href="registro_experimentos.json">Registro en blanco</a> · <a href="analisis_youtube_instagram_viajes.html">Benchmark original y galería</a></p></section></main>'
body=re.sub(r'<summary>(.*?)</summary>',r'<h3>\1</h3>',body)
body=re.sub(r'<header[^>]*>[\s\S]*?</header>',lambda m:m.group(0),body,count=1)
page='<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Estrategia de lanzamiento · vlogs y viajes</title><style>'+oldcss+'main h1{font-size:30px;letter-spacing:-.7px} .muted,.eyebrow{color:#596b74} .finding{padding:0;border:0} .finding strong{color:#17484e}</style></head><body>'+body+'</body></html>'
page=page.replace('<table>', '<div class="tablewrap"><table>').replace('</table>','</table></div>')
(OUT/'estrategia_youtube_viajes_v2.html').write_text(page)
shutil.copyfile(SRC/'05_auditoria_cuantitativa.html',OUT/'auditoria_cuantitativa.html')
# Fix local evidence links in the copied standalone audit.
audpath=OUT/'auditoria_cuantitativa.html';a=audpath.read_text();a=a.replace('href="05_auditoria_cuantitativa.json"','href="../investigacion/05_auditoria_cuantitativa.json"').replace('href="evidencia_grandes/','href="../investigacion/evidencia_grandes/');audpath.write_text(a)

olddata=json.loads((OUT/'datos_benchmark.json').read_text())
extra=json.loads((SRC/'04_referentes_emergentes.json').read_text())
expanded=[]
for name,c in extra.items():
 for v in c['videos']:expanded.append({'channel':name,**v})
dataset={'observedDate':'2026-10-06','methodology':'96 originales más 18 adicionales; vistas acumuladas de distinta edad. Clasificación y auditoría se aplican sólo a los 96 originales. No es una cohorte de lanzamientos.','originalChannels':olddata['channels'],'additionalChannels':[{k:v for k,v in c.items() if k!='videos'} for c in extra.values()],'videos':olddata['videos']+expanded}
assert len(dataset['videos'])==114
assert len(set(x.get('videoId') or x.get('video_id') or x.get('url') for x in dataset['videos']))==114
(OUT/'datos_benchmark_v2.json').write_text(json.dumps(dataset,ensure_ascii=False,indent=2))
snapshot={'recorded_at':None,'age_days':None,'views':None,'impressions':None,'ctr':None,'average_view_duration_seconds':None,'average_percentage_viewed':None,'watch_hours':None,'traffic_source_breakdown':[],'retention_notes':None,'subscribers_gained':None,'next_video_evidence':None,'availability_notes':None}
experiments=[]
for i,pilar in enumerate(['A','B','C','A','B','C'],1):
 experiments.append({'episode_id':f'P{i:02}','pillar':pilar,'audience':None,'question':None,'hypothesis':None,'demand_evidence_links':[],'destination':None,'title':None,'thumbnail_concepts':[],'budget_limit_mxn':None,'hours_limit':None,'published_at':None,'actual_incremental_cost_mxn':None,'total_trip_cost_mxn':None,'actual_hours_by_phase':{},'day_7':dict(snapshot),'day_28':dict(snapshot),'decision':None,'evidence':None,'alternative_explanation':None,'next_test':None})
(OUT/'registro_experimentos.json').write_text(json.dumps({'status':'Plantilla vacía, no resultados medidos','instructions':'Duplicar por episodio. Datos no disponibles: ND en availability_notes. Mantener formatos y fuentes separados; registrar fecha y edad exacta. No usar reglas propuestas como significancia estadística.','context':{'city':None,'protagonists':None,'hours_per_week':None,'quarter_budget_mxn':None,'existing_channel':None},'experiments':experiments},ensure_ascii=False,indent=2))

class ResearchDoc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if getattr(f,'section_id',None):self.section_pages[f.section_id]=self.page
def heading(s,key=None):
 f=par(s,'HeadR1');f.section_id=key;return f
def footer(canvas,doc):
 canvas.saveState();canvas.setStrokeColor(colors.HexColor('#d4dfe3'));canvas.line(45,35,A4[0]-45,35)
 canvas.setFont('Research',7.2);canvas.setFillColor(colors.HexColor('#657982'));canvas.drawString(45,22,'Estrategia y medición · 15 referentes · corte 6-oct-2026');canvas.drawRightString(A4[0]-45,22,'E'+str(doc.page));canvas.restoreState()
story.extend([Spacer(1,35),par('INVESTIGACIÓN AMPLIADA · OCTUBRE 2026','HeadR4'),par('Un canal de viajes con un sistema para aprender','HeadR1'),par('Estrategia de lanzamiento, recursos y decisiones respaldadas por una revisión de 15 referentes en YouTube e Instagram.'),Spacer(1,14),par('<b>114 entradas de Videos · 12 ideas · seis pilotos · evaluación a 7 y 28 días</b>'),par('Incluye una auditoría del benchmark, tres canales activos de menor escala, documentación oficial de distribución y el informe original completo como anexo.'),Spacer(1,14),par('<b>Propuesta inicial:</b> escapadas cercanas, protagonistas reconocibles, costo y tiempo reales, una decisión por episodio.'),par('La investigación no garantiza crecimiento. Define qué producir, cómo limitar el costo de aprendizaje y qué señales permiten repetir o corregir.'),Spacer(1,20),par('Para Arturo · versión 2 · CDMX','HeadR4')])
story.append(PageBreak());addhtml(scope)
for i,(title,content) in enumerate(sections,1):
 story.append(PageBreak());story.append(heading(f'{i}. {title}',str(i)));start=len(story);addhtml(content)
 for flow in story[start:]:
  if isinstance(flow,Paragraph) and flow.getPlainText()=='Qué documentan realmente las plataformas':flow.keepWithNext=0
story.append(PageBreak());story.append(heading('Anexo: benchmark original','annex_intro'));story.append(par('El siguiente bloque conserva las 41 páginas del primer informe y su numeración 1–41. Los marcadores del PDF permiten saltar a sus fichas y a la galería de miniaturas. Los datos y las propuestas del cuerpo ampliado prevalecen cuando añaden precisiones de metodología o de capacidad.'))
doc=ResearchDoc(str(TMP/'estrategia_cuerpo_v2.pdf'),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=46,bottomMargin=48,title='Estrategia de lanzamiento: vlogs y viajes',author='Investigación para Arturo');doc.section_pages={}
doc.build(story,onFirstPage=footer,onLaterPages=footer)
reader=PdfReader(TMP/'estrategia_cuerpo_v2.pdf');offset=len(reader.pages)
writer=PdfWriter();writer.append(reader,import_outline=False);writer.append(PdfReader(OUT/'pdf/analisis_youtube_instagram_viajes.pdf'),import_outline=False)
writer.add_outline_item('Guía de lectura',1)
for i,(title,_) in enumerate(sections,1):writer.add_outline_item(f'{i}. {title}',doc.section_pages[str(i)]-1)
ann=writer.add_outline_item('Anexo: benchmark original de 12 creadores',offset)
for title,p in [('Mapa comparativo',2),('Referencias y frecuencia',3),('Alan, Luisito y Lethal',11),('Duplas, Vero, La Vida y PlanetaJuan',19),('Clavero, Ramilla y Molaviajar',30),('Galería de miniaturas',38)]:writer.add_outline_item(title,offset+p-1,parent=ann)
writer.add_metadata({'/Title':'Estrategia y benchmark de vlogs y viajes - versión 2','/Author':'Investigación para Arturo','/Subject':'15 referentes, 114 entradas, 90 días de lanzamiento y decisiones basadas en evidencia'})
target=OUT/'pdf/estrategia_y_benchmark_v2.pdf'
with target.open('wb') as f:writer.write(f)
result={'strategyPages':offset,'annexPages':41,'totalPages':len(writer.pages),'sectionPages':doc.section_pages,'pdf':str(target),'html':str(OUT/'estrategia_youtube_viajes_v2.html')}
(TMP/'v2_manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
