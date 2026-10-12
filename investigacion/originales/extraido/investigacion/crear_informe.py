from pathlib import Path
import json,re,html,statistics,datetime,unicodedata,base64
from zoneinfo import ZoneInfo
from html.parser import HTMLParser
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,LongTable,TableStyle,Image,KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

BASE=Path(__file__).resolve().parent.parent
SRC=BASE/'investigacion'; OUT=BASE/'output';OUT.mkdir(exist_ok=True)
PDF=OUT/'pdf';PDF.mkdir(exist_ok=True)
TZ=ZoneInfo('America/Mexico_City'); CUT=datetime.date(2026,10,6)
def localdate(s):
    dt=datetime.datetime.fromisoformat(s.replace('Z','+00:00'))
    if dt.tzinfo:dt=dt.astimezone(TZ)
    return dt.date().isoformat()
def dur(s):
    s=int(round(float(s)));h=s//3600;m=s%3600//60;x=s%60
    return f'{h}:{m:02d}:{x:02d}' if h else f'{m}:{x:02d}'
def num(v):return f'{int(v):,}'.replace(',',' ')
def load(p):return json.loads((SRC/p).read_text())
data={}
for p in ['00_referencias_datos.json','02_parejas_nomadas_datos.json','03_aventura_datos.json']:
    data.update(load(p))
for name,h in [('Alan por el mundo','alanxelmundo'),('Luisito Comunica','luisitocomunica'),('Lethal Crysis','lethalcrysis')]:
    raw=load('evidencia_grandes/'+h+'_watch.json')
    data[name]={'channelUrl':f'https://www.youtube.com/@{h}/videos','source':'Página pública del canal y del video','observedDate':CUT.isoformat(),'videos':[
      dict(videoId=v['video_id'],url=v['url'],title=v['title'],datePublished=v['publishDate'],lengthSeconds=v['lengthSeconds'],viewsExact=v['viewCount'],duration=v['duration_channel'],thumbnail=v['thumbnail'],description=v['shortDescription']) for v in raw]}
order=['heyitspriguel','El Mundo en Pareja','Alan por el mundo','Luisito Comunica','Lethal Crysis','Viajando con Vero','PlanetaJuan','Ramilla de Aventura','Clavero','Molaviajar','Misias pero viajeras','La Vida de Viaje']
meta={
'heyitspriguel':('Vlog familiar / pareja','Publicación espaciada; último 26-jun-2026','Continuidad de personajes','heyitspriguel'),
'El Mundo en Pareja':('Pareja / hoteles / guías','Actividad reciente en Videos','Experiencia + criterio para decidir','elmundoenpareja_'),
'Alan por el mundo':('Series de destinos','Actividad reciente en Videos','Una decisión útil por capítulo','alanxelmundo'),
'Luisito Comunica':('Experiencias y curiosidad','Actividad reciente en Videos','Pregunta cotidiana + prueba personal','luisitocomunica'),
'Lethal Crysis':('Documental / exploración','Cadencia variable reciente','Acceso y una historia humana','lethalcrysis_'),
'Viajando con Vero':('Vlog / cultura / familia','Actividad reciente en Videos','Primera persona y contraste emocional','veronicaweffer'),
'PlanetaJuan':('Vlog / cultura / encuentros','Actividad reciente en Videos','Expectativas frente a experiencia local','planetajuan'),
'Ramilla de Aventura':('Misiones / transporte','Cadencia variable reciente','El desplazamiento como historia','soyramilladeaventura'),
'Clavero':('Retos / reportaje','Videos: último 28-dic-2024; IG reciente','Regla y evidencia del reto','hiclavero'),
'Molaviajar':('Guías / vlog breve','Videos: bloque feb–mar-2026; pausa posterior','Biblioteca de preguntas prácticas','molaviajar'),
'Misias pero viajeras':('Guías / dupla de amigas','Cierre declarado 30-may-2025','Presupuesto y llegada práctica','misiasperoviajeras'),
'La Vida de Viaje':('Naturaleza / cicloturismo','Videos: último jul-2024; retorno IG may-2026','Especialización y paisaje protagonista','lavidadeviaje')}
records=[];summary=[]
for name in order:
 c=data[name];v=c['videos'];assert len(v)==8,(name,len(v))
 for x in v:
  assert x.get('datePublished') and x.get('viewsExact') and x.get('lengthSeconds'),(name,x)
  x['dateMexicoCity']=localdate(x['datePublished']);x['durationExact']=dur(x['lengthSeconds'])
  assert x['dateMexicoCity']<=CUT.isoformat()
  records.append({'channel':name,**x})
 dates=[datetime.date.fromisoformat(x['dateMexicoCity']) for x in v]
 gaps=[abs((a-b).days) for a,b in zip(dates,dates[1:])]
 summary.append({'channel':name,'channelUrl':c['channelUrl'],'instagramUrl':'https://www.instagram.com/'+meta[name][3]+'/',
 'focus':meta[name][0],'status':meta[name][1],'transfer':meta[name][2],
 'latest':max(dates).isoformat(),'oldest':min(dates).isoformat(),'gapsDays':gaps,'medianGapDays':statistics.median(gaps),
 'medianDurationSeconds':statistics.median(int(x['lengthSeconds']) for x in v),'medianViews':statistics.median(int(x['viewsExact']) for x in v),
 'gapSinceLatestDays':(CUT-max(dates)).days})
dataset={'observedDate':CUT.isoformat(),'timezone':'America/Mexico_City','method':'8 entradas por canal en Videos; títulos/fecha/vistas/duración de página individual. No son series de vistas a igual edad.','channels':summary,'videos':records}
(OUT/'datos_benchmark.json').write_text(json.dumps(dataset,ensure_ascii=False,indent=2))

def inline(s):
 s=html.escape(s,quote=False)
 s=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',r'\1',s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
 s=re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 return s
def markdown(s):
 lines=s.splitlines();res=[];i=0
 while i<len(lines):
  l=lines[i].strip()
  if not l:i+=1;continue
  if l.startswith('```'):
   i+=1;code=[]
   while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]);i+=1
   res.append('<p>'+inline(' '.join(code))+'</p>');i+=1;continue
  m=re.match(r'^(#{1,4})\s+(.*)',l)
  if m:
   n=min(4,len(m[1])+1);res.append(f'<h{n}>{inline(m[2])}</h{n}>');i+=1;continue
  if l.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    cells=lines[i].strip().strip('|').split('|')
    if not all(re.fullmatch(r'[\s:\-]+',c) for c in cells):rows.append(cells)
    i+=1
   res.append('<table>'+''.join('<tr>'+''.join(('<th>' if ri==0 else '<td>')+inline(c.strip())+('</th>' if ri==0 else '</td>') for c in row)+'</tr>' for ri,row in enumerate(rows))+'</table>');continue
  if re.match(r'^[-*]\s',l):res.append('<p class="bullet">• '+inline(l[2:])+'</p>');i+=1;continue
  para=[l];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||[-*]\s|```)',lines[i].strip()):para.append(lines[i].strip());i+=1
  res.append('<p>'+inline(' '.join(para))+'</p>')
 return '\n'.join(res)

def table(headers,rows):
 return '<table><thead><tr>'+''.join('<th>'+h+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+str(c)+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table>'
matrix='<h2>Mapa comparativo de 12 creadores</h2><p>Medianas de duración de las ocho entradas; incluyen clips y trailers cuando aparecen en Videos. La tabla es un mapa de oferta, no un ranking de eficiencia. Abrir las fichas para interpretar pausas y periodos.</p>'
matrix+=table(['Creador / fuentes','Propuesta','Último video','Duración mediana','Situación'],[
 [f'<a href="{s["channelUrl"]}">{s["channel"]}</a><br><a href="{s["instagramUrl"]}">Instagram</a>',s['focus'],s['latest'],dur(s['medianDurationSeconds']),s['status']] for s in summary])
cadence='<h2>Frecuencia: datos antes de conclusiones</h2><p>Se utiliza el intervalo entre fechas de calendario en CDMX. La mediana de siete intervalos se acompaña de su rango y de los días desde la última publicación. Una mediana corta puede coexistir con una pausa larga. Las fichas también muestran densidad de publicaciones en ventanas fijas; es otra medida y no debe mezclarse con esta.</p>'
cadence+=table(['Canal','Ventana de ocho videos','Intervalo mediano','Rango de intervalos','Días desde último'],[[s['channel'],s['oldest']+' a '+s['latest'],f'{s["medianGapDays"]:g} días',f'{min(s["gapsDays"])}–{max(s["gapsDays"])} días',s['gapSinceLatestDays']] for s in summary])
root= (SRC/'00_analisis_editorial.html').read_text()
rootTables='<h2>Muestra de videos de tus dos referencias</h2>'
for name in order[:2]:
 rootTables+='<h3>'+name+'</h3>'+table(['Video y fuente','Fecha CDMX','Duración exacta','Vistas al consultar'],[[f'<a href="{v["url"]}">{html.escape(v["title"])}</a>',v['dateMexicoCity'],v['durationExact'],num(v['viewsExact'])] for v in data[name]['videos']])
chapters=[('Estrategia y ejemplos principales',root+rootTables+cadence)]
for title,file in [('Alan, Luisito y Lethal','01_referentes_grandes.md'),('Duplas, naturaleza y vlogs personales','02_parejas_nomadas.md'),('Aventura y guías prácticas','03_aventura_utilidad.md')]:
 chapters.append((title,markdown((SRC/file).read_text())))
gallery=[('heyitspriguel','evidencia/miniaturas_priguel.png'),('El Mundo en Pareja','evidencia/miniaturas_elmundoenpareja.png'),('Viajando con Vero','evidencia/miniaturas_vero.png'),('La Vida de Viaje','evidencia/miniaturas_lavidadeviaje.png'),('Misias pero viajeras','evidencia/miniaturas_misias_contacto.png'),('PlanetaJuan','evidencia/miniaturas_planetajuan_contacto.png'),('Alan, Luisito y Lethal','evidencia_grandes/miniaturas_9_referentes.jpg'),('Clavero, Ramilla y MolaViajar','evidencia/miniaturas_aventura.jpg')]
galleryHtml='<h2>Evidencia visual de las miniaturas</h2><p>Capturas y láminas observadas. Algunas imágenes secundarias no cargaron en las capturas de pantalla; el análisis se limita a las que sí se ven. Los títulos de la interfaz pueden estar traducidos; la base de datos conserva el título de la página del video.</p>'
for title,p in gallery:
 mime='image/png' if p.endswith('.png') else 'image/jpeg'
 embedded='data:'+mime+';base64,'+base64.b64encode((SRC/p).read_bytes()).decode()
 galleryHtml+=f'<figure><img src="{embedded}" alt="Miniaturas de {title}" loading="lazy"><figcaption>{title} · consulta 6-oct-2026</figcaption></figure>'
css='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font:16px/1.65 system-ui,-apple-system,sans-serif;color:#213047;background:#f2f5f7}header{background:#123c43;color:white;padding:66px max(24px,calc((100vw - 1100px)/2));}h1{font-size:clamp(32px,5vw,56px);line-height:1.1;letter-spacing:-2px;max-width:900px;margin:16px 0}header p{max-width:800px;color:#d2e5e7}nav{position:sticky;top:0;background:#fff;border-bottom:1px solid #dce4e7;padding:12px 24px;display:flex;gap:20px;flex-wrap:wrap;z-index:3}nav a{color:#17484e;text-decoration:none;font-size:14px;font-weight:700}main{max-width:1150px;margin:auto;padding:28px 24px 80px}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:30px}.stat{border:1px solid #5c7c81;padding:16px;border-radius:12px}.stat strong{font-size:30px;display:block}.stat span{font-size:14px;color:#e1eff0}section{background:white;border:1px solid #dae4e7;border-radius:14px;padding:32px;margin:22px 0;scroll-margin-top:100px}h2{font-size:28px;color:#17484e;line-height:1.3;margin:35px 0 14px}h3{font-size:22px;margin:30px 0 12px;color:#294553}h4{font-size:18px;color:#294553}table{width:100%;border-collapse:collapse;font-size:13px;line-height:1.5;margin:18px 0;display:table}td,th{padding:12px 10px;text-align:left;border-bottom:1px solid #dae4e7;vertical-align:top}th{background:#e9f1f2;color:#123c43}tr:nth-child(even){background:#f7fafb}a{color:#056270;overflow-wrap:anywhere}p,li{max-width:100%}li{margin:10px 0}code{font:12px ui-monospace,monospace;background:#edf1f4;padding:2px 4px}details{border-top:1px solid #dae4e7;padding:18px 0}summary{font-size:23px;font-weight:700;color:#17484e;cursor:pointer}figure{margin:24px 0}figure img{display:block;width:100%;height:auto;border-radius:10px;border:1px solid #ddd}figcaption{font-size:14px;color:#586675;margin-top:8px}.filters{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0}input,select{font:inherit;padding:10px;border:1px solid #9eafb8;border-radius:7px;width:100%}.filter{min-width:180px;flex:1}.filter label{display:block;font-size:13px;font-weight:650}#videoTable td:nth-child(2){width:45%}.note{background:#eef5f6;padding:16px;border-left:4px solid #318797}.tablewrap{overflow:auto}footer{padding:20px;color:#607080;font-size:13px}@media(max-width:700px){.stats{grid-template-columns:repeat(2,1fr)}section{padding:18px}table{min-width:640px}h1{letter-spacing:-1px}nav{position:static}}@media print{nav,.filters{display:none}details{display:block}section{border:0;page-break-inside:auto}body{background:white}header{background:white;color:#123c43}header p{color:#456}.tablewrap{overflow:visible}}'''
js='''const rows=DATA;const creator=document.querySelector('#creator');const search=document.querySelector('#search');const sort=document.querySelector('#sort');for(const c of [...new Set(rows.map(r=>r.channel))]){const o=document.createElement('option');o.value=c;o.textContent=c;creator.append(o)}function draw(){let r=rows.filter(v=>(!creator.value||v.channel===creator.value)&&(!search.value||(v.title+' '+v.channel).toLocaleLowerCase().includes(search.value.toLocaleLowerCase())));if(sort.value==='date')r.sort((a,b)=>b.dateMexicoCity.localeCompare(a.dateMexicoCity));if(sort.value==='views')r.sort((a,b)=>Number(b.viewsExact)-Number(a.viewsExact));if(sort.value==='length')r.sort((a,b)=>Number(b.lengthSeconds)-Number(a.lengthSeconds));const body=document.querySelector('#videoBody');body.replaceChildren();for(const v of r){const tr=document.createElement('tr');for(const val of [v.channel,v.title,v.dateMexicoCity,v.durationExact,new Intl.NumberFormat('es-MX').format(Number(v.viewsExact))]){const td=document.createElement('td');if(val===v.title){const a=document.createElement('a');a.href=v.url;a.target='_blank';a.rel='noopener noreferrer';a.textContent=val;td.append(a)}else td.textContent=val;tr.append(td)}body.append(tr)}document.querySelector('#count').textContent=r.length+' de '+rows.length+' videos'}for(const x of [creator,search,sort])x.addEventListener('input',draw);draw();'''
explorer='''<h2>Explorar los 96 videos</h2><p class="note">Vistas acumuladas de distintas edades y escalas. Ordenar por vistas ayuda a localizar ejemplos; no mide calidad ni causa de rendimiento. Fecha y duración proceden de la página individual.</p><div class="filters"><div class="filter"><label for="creator">Creador</label><select id="creator"><option value="">Todos los creadores</option></select></div><div class="filter"><label for="search">Buscar título o tema</label><input id="search" type="search" placeholder="Ej. hotel, Japón, presupuesto"></div><div class="filter"><label for="sort">Ordenar</label><select id="sort"><option value="group">Por creador</option><option value="date">Publicación reciente</option><option value="views">Vistas acumuladas</option><option value="length">Mayor duración</option></select></div></div><p id="count" aria-live="polite"></p><div class="tablewrap"><table id="videoTable"><thead><tr><th>Creador</th><th>Video / fuente</th><th>Publicación CDMX</th><th>Duración</th><th>Vistas</th></tr></thead><tbody id="videoBody"></tbody></table></div>'''
body=f'''<header><span>INVESTIGACIÓN EDITORIAL · 6 OCTUBRE 2026</span><h1>Vlogs y viajes:<br>qué aprender antes de lanzar</h1><p>12 creadores en YouTube e Instagram, tus dos referentes y decisiones concretas para construir un canal nuevo.</p><div class="stats"><div class="stat"><strong>12</strong><span>creadores distintos</span></div><div class="stat"><strong>96</strong><span>videos documentados</span></div><div class="stat"><strong>39</strong><span>posts / Reels con caption</span></div><div class="stat"><strong>36+</strong><span>miniaturas inspeccionadas</span></div></div></header><nav><a href="#mapa">Comparación</a><a href="#estrategia">Estrategia</a><a href="#fichas">Fichas</a><a href="#galeria">Miniaturas</a><a href="#datos">Videos y fuentes</a></nav><main><section id="mapa">{matrix}</section><section id="estrategia">{chapters[0][1]}</section><section id="fichas"><h2>Fichas de los otros diez creadores</h2><p>Abrir cada grupo para consultar contenido, títulos, frecuencia, miniaturas, Instagram, negocio visible y límites de evidencia.</p>'''
for title,content in chapters[1:]:body+=f'<details><summary>{title}</summary>{content}</details>'
body+='</section><section id="galeria">'+galleryHtml+'</section><section id="datos">'+explorer+'</section><footer>Fuentes primarias enlazadas en cada observación. Datos y archivos de investigación en la carpeta del proyecto. PDF completo: output/pdf/analisis_youtube_instagram_viajes.pdf.</footer></main>'
browserRecords=[{k:r[k] for k in ['channel','title','url','dateMexicoCity','durationExact','viewsExact','lengthSeconds']} for r in records]
output='<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Análisis de vlogs y viajes · 12 creadores</title><style>'+css+'</style></head><body>'+body+'<script>const DATA='+json.dumps(browserRecords,ensure_ascii=False).replace('</',r'<\/')+';'+js+'</script></body></html>'
# Wrap all tables in static sections for responsive overflow.
output=output.replace('<table>', '<div class="tablewrap"><table>').replace('</table>','</table></div>')
# Explorer table already has wrapper; repair its closing wrapper added above.
output=output.replace('</tbody></table></div></div>','</tbody></table></div>')
(OUT/'analisis_youtube_instagram_viajes.html').write_text(output)

# PDF: use the same editorial content and complete agent dossiers.
fontbase=Path('/System/Library/Fonts/Supplemental')
pdfmetrics.registerFont(TTFont('Research',str(fontbase/'Arial.ttf')))
pdfmetrics.registerFont(TTFont('ResearchBold',str(fontbase/'Arial Bold.ttf')))
pdfmetrics.registerFont(TTFont('ResearchItalic',str(fontbase/'Arial Italic.ttf')))
pdfmetrics.registerFontFamily('Research',normal='Research',bold='ResearchBold',italic='ResearchItalic',boldItalic='ResearchBold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyR',fontName='Research',fontSize=9.2,leading=13.4,spaceAfter=8,textColor=colors.HexColor('#233345'),splitLongWords=1))
styles.add(ParagraphStyle(name='CellR',fontName='Research',fontSize=7.4,leading=10.2,spaceAfter=0,splitLongWords=1))
styles.add(ParagraphStyle(name='HeadCellR',parent=styles['CellR'],fontName='ResearchBold',textColor=colors.HexColor('#123c43')))
for i,size in [(1,25),(2,18),(3,13.5),(4,11)]:styles.add(ParagraphStyle(name=f'HeadR{i}',fontName='ResearchBold',fontSize=size,leading=size*1.22,spaceBefore=14,spaceAfter=9,keepWithNext=True,textColor=colors.HexColor('#17484e')))
def clean(s):
 s=unicodedata.normalize('NFC',s)
 s=''.join(c for c in s if ord(c)<0x1f000 and c not in '\ufe0f\u200d')
 return s.replace('–','-').replace('—','-').replace('‑','-').replace('−','-').replace('…','...')
def pdfinline(s):
 s=clean(s);s=re.sub(r'<a href="([^"]+)">',r'<link href="\1" color="#066877">',s).replace('</a>','</link>')
 s=s.replace('<strong>','<b>').replace('</strong>','</b>').replace('<code>','').replace('</code>','').replace('<br>','<br/>')
 return s
class Node:
 def __init__(self,tag,attrs=None):self.tag=tag;self.attrs=dict(attrs or []);self.children=[]
 def inner(self):return ''.join(c if isinstance(c,str) else c.outer() for c in self.children)
 def outer(self):
  if self.tag=='br':return '<br/>'
  attrs=''.join(' '+k+'="'+html.escape(v or '',quote=True)+'"' for k,v in self.attrs.items())
  return '<'+self.tag+attrs+'>'+self.inner()+'</'+self.tag+'>'
class Tree(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=False);self.root=Node('root');self.stack=[self.root]
 def handle_starttag(self,t,a):
  n=Node(t,a);self.stack[-1].children.append(n)
  if t not in ['img','br','hr','meta','input']:self.stack.append(n)
 def handle_endtag(self,t):
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i].tag==t:self.stack=self.stack[:i];break
 def handle_data(self,s):self.stack[-1].children.append(html.escape(s,quote=False))
 def handle_entityref(self,s):self.stack[-1].children.append('&'+s+';')
 def handle_charref(self,s):self.stack[-1].children.append('&#'+s+';')
WIDTH=A4[0]-90
story=[]
def par(s,style='BodyR'):return Paragraph(pdfinline(s),styles[style])
def descend(n,tag):
 for c in n.children:
  if isinstance(c,Node):
   if c.tag==tag:yield c
   else:yield from descend(c,tag)
def emit(n):
 for c in n.children:
  if isinstance(c,str):continue
  if c.tag in ['h1','h2','h3','h4']:story.append(par(c.inner(),'HeadR'+c.tag[1]))
  elif c.tag in ['p','li']:story.append(par(('• ' if c.tag=='li' else '')+c.inner()))
  elif c.tag=='table':
   trs=list(descend(c,'tr'));rows=[]
   for ri,tr in enumerate(trs):
    cells=[x for x in tr.children if isinstance(x,Node) and x.tag in ['td','th']]
    rows.append([par(x.inner(),'HeadCellR' if ri==0 else 'CellR') for x in cells])
   if not rows:continue
   cols=max(map(len,rows));rows=[r+[par('','CellR')]*(cols-len(r)) for r in rows]
   headers=' '.join(x.getPlainText().lower() for x in rows[0]);weights=[1]*cols
   if cols==4 and any(x in headers for x in ['video','vídeo','post','publicación']):
    ix=next((i for i,x in enumerate(rows[0]) if any(s in x.getPlainText().lower() for s in ['video','vídeo','post','enlace'])),0)
    weights=[.85]*cols;weights[ix]=2.9
   elif cols==5:weights=[1.45,2,1,1,1.65]
   elif cols==6:weights=[1.1,1.5,1.45,1.15,1.1,1.8]
   t=LongTable(rows,colWidths=[WIDTH*w/sum(weights) for w in weights],repeatRows=1,hAlign='LEFT')
   t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e5eff1')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.5,colors.HexColor('#79959c')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#d5e0e4')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f5f8fa')]),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
   story.extend([t,Spacer(1,12)])
  else:emit(c)
def addhtml(s):t=Tree();t.feed(s);emit(t.root)
story.extend([Spacer(1,35),par('INVESTIGACIÓN EDITORIAL · 6 OCTUBRE 2026','HeadR4'),par('Vlogs y viajes:<br/>qué aprender antes de lanzar','HeadR1'),par('Análisis detallado de 12 creadores en YouTube e Instagram, con tus dos referentes como punto de partida.'),Spacer(1,12),par('<b>96 videos · 39 publicaciones con caption · 36+ miniaturas</b>'),par('Incluye comparación, frecuencia, títulos, miniaturas, formatos, conexiones entre plataformas, negocio visible y un plan de experimentos para el nuevo canal.'),par('Fuentes enlazadas y datos auditables. Las observaciones públicas se separan de las hipótesis editoriales. No se estiman CTR, retención o ingresos de terceros.'),Spacer(1,25),par('Contenido','HeadR2')])
for s in ['1. Mapa de los 12 creadores','2. Estrategia y tus dos ejemplos','3. Frecuencia y muestras de YouTube','4. Alan, Luisito y Lethal','5. Misias, Vero, La Vida y PlanetaJuan','6. Clavero, Ramilla y MolaViajar','7. Evidencia visual de miniaturas']:story.append(par(s))
story.append(PageBreak());addhtml(matrix)
for title,content in chapters:story.append(PageBreak());story.append(par(title,'HeadR1'));addhtml(content)
story.append(PageBreak());story.append(par('Evidencia visual de miniaturas','HeadR1'));story.append(par('Imágenes inspeccionadas, pertenecientes a sus creadores. Las capturas de interfaz pueden traducir títulos o mostrar una imagen en blanco; sólo se analizan las miniaturas visibles.'))
from PIL import Image as PILImage
for title,p in gallery:
 story.append(par(title,'HeadR3'))
 im=PILImage.open(SRC/p);w,h=im.size;scale=min(WIDTH/w,530/h)
 story.append(Image(str(SRC/p),width=w*scale,height=h*scale));story.append(Spacer(1,14))
doc=SimpleDocTemplate(str(PDF/'analisis_youtube_instagram_viajes.pdf'),pagesize=A4,rightMargin=45,leftMargin=45,topMargin=46,bottomMargin=48,title='Análisis de vlogs y viajes: YouTube e Instagram',author='Investigación editorial para Arturo')
def footer(canvas,doc):
 canvas.saveState();canvas.setStrokeColor(colors.HexColor('#d4dfe3'));canvas.line(45,35,A4[0]-45,35);canvas.setFont('Research',7.2);canvas.setFillColor(colors.HexColor('#657982'));canvas.drawString(45,22,'Vlogs y viajes · 12 creadores · corte 6-oct-2026');canvas.drawRightString(A4[0]-45,22,str(doc.page));canvas.restoreState()
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(json.dumps({'creators':len(data),'videos':len(records),'html':str(OUT/'analisis_youtube_instagram_viajes.html'),'pdf':str(PDF/'analisis_youtube_instagram_viajes.pdf')},ensure_ascii=False))
