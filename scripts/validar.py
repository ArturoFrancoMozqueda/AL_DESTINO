#!/usr/bin/env python3
"""Comprueba artefactos del kit sin dependencias ni acceso a red."""
from pathlib import Path
import hashlib,json,re,struct,sys,base64,xml.etree.ElementTree as ET
from urllib.parse import unquote
R=Path(__file__).resolve().parents[1]
errors=[];checks=0
IGNORED_PARTS={'originales','.git','.hyperframes','node_modules','.venv','__pycache__'}
def skip_file(p):return bool(IGNORED_PARTS.intersection(p.parts)) or p.name.endswith('.local.json')

def check(ok,message):
 global checks
 checks+=1
 if not ok:errors.append(message)
def read(p):return json.loads((R/p).read_text(encoding="utf-8"))
manifest=read('contexto/manifiesto-originales.json')
for f in manifest['files']:
 p=R/f['path'];check(p.is_file(),f"Original ausente: {p}")
 if p.is_file():check(hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],f"Original alterado: {p}")
# Current owned JSON must parse; inherited artifacts retain their original formats.
for p in R.rglob('*.json'):
 if skip_file(p):continue
 try:json.loads(p.read_text(encoding="utf-8"));check(True,str(p))
 except Exception as e:check(False,f"JSON inválido {p}: {e}")
# Local Markdown/HTML links: ignore URLs, anchors and historical originals.
for p in list(R.rglob('*.md'))+[R/'marca/index.html',R/'marca/archivo/v03-aplicaciones/index.html',R/'marca/design-system.html',R/'marca/exportaciones/v05-png/index.html',R/'marca/exportaciones/index.html',R/'marca/video/v01/index.html']:
 if skip_file(p):continue
 s=p.read_text(encoding="utf-8")
 targets=re.findall(r'\]\(([^)]+)\)',s) if p.suffix=='.md' else re.findall(r'(?:src|href)="([^"]+)"',s)
 for t in targets:
  t=t.strip('<>');t=unquote(t.split('#')[0])
  if not t or re.match(r'^[a-zA-Z][\w+.-]*:',t):continue
  check((p.parent/t).exists(),f"Enlace roto {p.relative_to(R)} → {t}")
tokens=read('marca/tokens/brand_tokens.json');css=(R/'marca/tokens/brand_tokens.css').read_text(encoding="utf-8");manual=(R/'marca/manual.md').read_text(encoding="utf-8")
for k,v in tokens['color'].items():
 check(f"--al-{k.replace('_','-')}: {v['$value']}" in css,f"CSS no coincide con token {k}")
 check(v['$value'] in manual,f"Manual no coincide con token {k}")
for pair in tokens['contrast_checks']:
 if pair['foreground']=='cafe_oscuro' and pair['background']=='arena':check(pair['ratio']>=4.5,'Texto principal con contraste insuficiente')
# The standalone design system must export the same tokens and preserve the source logo.
ds=(R/'marca/design-system.html').read_text(encoding="utf-8")
snapshot=re.search(r'<script id="brand-data" type="application/json">(.*?)</script>',ds,re.S)
check(snapshot is not None,'Tokens del HTML ausentes')
if snapshot:check(json.loads(snapshot.group(1))==tokens,'Tokens HTML y JSON divergentes')
ids=re.findall(r'\bid="([^"]+)"',ds)
check(len(ids)==len(set(ids)),'IDs duplicados en design system')
check('@import' not in ds and '<script src=' not in ds,'Design system requiere recursos externos')
source=re.search(r'<image id="al-logo-source" href="data:image/png;base64,([^"]+)"',ds)
check(source is not None,'Fuente de logo del HTML ausente')
if source:
 original_logo=(R/'marca/originales/extraido/AL_DESTINO_Design_System_v0.1/04_Referencias_visuales/Logo_horizontal_composicion_aprobada.png').read_bytes()
 check(hashlib.sha256(base64.b64decode(source.group(1))).digest()==hashlib.sha256(original_logo).digest(),'Logo del HTML modificado')
working=re.search(r'<image id="al-logo-working"[^>]*href="data:image/png;base64,([^"]+)"',ds)
check(working is not None,'Logo de aplicación transparente ausente')
if working:check(base64.b64decode(working.group(1))==(R/'marca/assets/logos/piezas/logo-horizontal-transparente.png').read_bytes(),'Extracción transparente HTML/PNG divergente')
check(tokens['logo']['preferred_background']=='arena','Fondo del logo no corresponde a preferencia declarada')
research=read('marca/investigacion-redes.json')
check(len(research['sources'])>=9,'Registro de investigación incompleto')
check(len(research['sources'])==len(re.findall(r'<li>',re.search(r'<ol class="source-list">(.*?)</ol>',ds,re.S).group(1))),'Fuentes HTML/JSON incoherentes')
check(tokens['signature']['gesture']['replaces_logo'] is False,'La firma no debe sustituir el logo')
profile=read('contexto/perfil.json');check(profile['production']['weekly_hours_total']==8,'Capacidad incorrecta')
check(profile['research']['radius_hours'] is None,'Radio permanente no solicitado')
check(profile['research']['budget_per_night_mxn'] is None,'Presupuesto permanente no solicitado')
cat=read('marca/archivo/v03-aplicaciones/catalogo.json');ns={'s':'http://www.w3.org/2000/svg'}
for t in cat['items']:
 p=R/'marca'/t['svg'];root=ET.parse(p).getroot()
 check(int(root.attrib['width'])==t['width'] and int(root.attrib['height'])==t['height'],f"Tamaño SVG {t['id']}")
 check(root.attrib['viewBox']==' '.join(map(str,[0,0]+t['viewbox'])),f"Proporción SVG {t['id']}")
 check(bool(root.findall('.//s:g',ns)),f"Grupos editables ausentes {t['id']}")
 check(bool(root.findall('.//s:text',ns)) or t['id']=='avatar',f"Texto editable ausente {t['id']}")
 png=R/'marca'/t['preview'];check(png.exists(),f"Preview ausente {t['id']}")
 if png.exists():
  b=png.read_bytes();check(b[:8]==b'\x89PNG\r\n\x1a\n',f"PNG inválido {t['id']}")
  w,h=struct.unpack('>II',b[16:24]);check(abs(w/h-t['width']/t['height'])<.001,f"Preview deformado {t['id']}")
  if t['id']=='YT-banner':check(len(b)<6*1024*1024,'Banner supera 6 MB')
  if t['id'].startswith('YT0'):check(len(b)<2*1024*1024,'Miniatura ligera supera 2 MB')
original=(R/'marca/originales/extraido/AL_DESTINO_Design_System_v0.1/04_Referencias_visuales/Logo_horizontal_composicion_aprobada.png').read_bytes()
active=(R/'marca/archivo/v03-aplicaciones/assets/logo-referencia-original.png').read_bytes()
check(hashlib.sha256(original).digest()==hashlib.sha256(active).digest(),'El logo original fue modificado')
for t in cat['items']:
 root=ET.parse(R/'marca'/t['svg']).getroot()
 group=root.find(".//s:g[@id='logo-original']",ns)
 check(group is not None,f"Logo no separado {t['id']}")
 if group is not None:
  images=group.findall('.//s:image',ns)
  check(bool(images),f"Logo original ausente {t['id']}")
  for image in images:
   src=image.attrib.get('href','');check(src.startswith('data:image/png;base64,'),f"Logo no raster original {t['id']}")
   if src.startswith('data:image/png;base64,'):check(hashlib.sha256(base64.b64decode(src.split(',',1)[1])).digest()==hashlib.sha256(original).digest(),f"Logo alterado en aplicación {t['id']}")
skills=list((R/'.agents/skills').glob('*/SKILL.md'))
required_skills={'al-destino-local','al-destino-airbnb','al-destino-hoteles-playa','al-destino-edicion','al-destino-contenido'}
check(required_skills <= {p.parent.name for p in skills},'Faltan skills de investigación o edición')
for p in skills:
 s=p.read_text(encoding="utf-8");fm=re.match(r'^---\n(.*?)\n---',s,re.S);check(bool(fm),f"Frontmatter {p}")
 if fm:
  check(f'name: {p.parent.name}' in fm.group(1),f"Nombre skill {p}")
  check('description: ' in fm.group(1),f"Descripción skill {p}")
 check('TODO:' not in s,f"Scaffold incompleto {p}")
canva=read('marca/archivo/v02-descartado/canva-designs.json');check(canva['status']=='descartado_por_usuario','Canva sigue recomendado')
check(all(row['status']=='descartado_por_usuario' for row in canva['items']),'Conversión descartada no marcada')
results=read('resultados/plantilla-episodio.json')
check([r['age_days']for r in results['observations']]==[7,28],'Cortes de medición incorrectos')
check(all(r['views'] is None for r in results['observations']),'Resultados de plantilla inventados')
# PNG export catalog and logo components must remain coherent with the actual files.
png_catalog=read('marca/exportaciones/v05-png/catalogo.json')
check(len(png_catalog['items'])==72,'Cantidad de PNG del sistema incompleta')
for item in png_catalog['items']:
 p=R/'marca/exportaciones/v05-png'/item['file'];check(p.exists(),f"PNG ausente: {item['file']}")
 if p.exists():
  data=p.read_bytes();check(data[:8]==b'\x89PNG\r\n\x1a\n',f"Formato PNG incorrecto: {item['file']}")
  check(struct.unpack('>II',data[16:24])==(item['width'],item['height']),f"Tamaño PNG incorrecto: {item['file']}")
  check(hashlib.sha256(data).hexdigest()==item['sha256'],f"PNG alterado: {item['file']}")
 check(item['status']=='borrador',f"Estado PNG no autorizado: {item['file']}")
pieces=read('marca/assets/logos/piezas/catalogo.json')
check(pieces['source_sha256']==hashlib.sha256(original).hexdigest(),'Fuente de piezas del logo divergente')
check(len(pieces['items'])==16,'Piezas individuales del logo incompletas')
for item in pieces['items']:
 p=R/'marca/assets/logos/piezas'/item['file'];data=p.read_bytes()
 check(data[25]==6,f"Pieza sin canal alfa: {item['id']}")
 check(hashlib.sha256(data).hexdigest()==item['sha256'],f"Pieza de logo alterada: {item['id']}")
active_source=(R/'marca/assets/logos/logo-original-referencia.png').read_bytes()
check(active_source==original,'Copia de trabajo del original alterada')
frames=list((R/'marca/motion/logo-al-destino/renders/secuencia-png').glob('*.png'))
check(len(frames)==96,'Secuencia PNG de animación incompleta')
for frame in frames:
 data=frame.read_bytes();check(struct.unpack('>II',data[16:24])==(1920,1080),f"Fotograma deformado: {frame.name}")
 check(data[25]==6,f"Fotograma sin RGBA: {frame.name}")
animated=R/'marca/motion/logo-al-destino/renders/AL-DESTINO-logo-animado.png'
check(animated.exists(),'PNG animado ausente')
if animated.exists():
 data=animated.read_bytes();at=8;count=None
 while at+12<=len(data):
  length=struct.unpack('>I',data[at:at+4])[0];kind=data[at+4:at+8]
  if kind==b'acTL':count=struct.unpack('>I',data[at+8:at+12])[0]
  at+=length+12
 check(count==96,'APNG no contiene 96 fotogramas')
 check(data[25]==6,'APNG sin RGBA')
org=read('contexto/organizacion-repo.json')
for move in org['moves']:check((R/move['to']).exists(),f"Archivo histórico perdido: {move['to']}")

# The editing kit is separate from the existing brand exports. Validate the actual
# layer sources, transparent PNGs and their catalog, not only the file count.
video_base=R/'marca/video/v01'
video=read('marca/video/v01/catalogo.json')
check(video['status']=='borrador','Kit de edición aprobado sin decisión')
check(video['brand_version']==tokens['version'],'Kit de edición con marca desactualizada')
check(video['color_values']=={k:v['$value'] for k,v in tokens['color'].items()},'Colores del kit y tokens divergentes')
video_ids=[]
for kind in ('icons','components'):
 for item in video[kind]:
  video_ids.append(kind+'/'+item['id'])
  check(item['status']=='borrador',f"Estado de recurso de edición no autorizado: {item['id']}")
  source=video_base/item['source']
  check(source.is_file(),f"SVG de edición ausente: {item['id']}")
  if source.is_file():
   check(hashlib.sha256(source.read_bytes()).hexdigest()==item['source_sha256'],f"Fuente de edición divergente: {item['id']}")
   try:
    svg_root=ET.parse(source).getroot()
    check(svg_root.tag=='{http://www.w3.org/2000/svg}svg',f"Fuente no SVG: {item['id']}")
    layer_ids={n.attrib['id'] for n in svg_root.iter() if 'id' in n.attrib}
    for layer in item.get('layers',[]):check(layer in layer_ids,f"Capa ausente {item['id']}: {layer}")
   except ET.ParseError as e:check(False,f"SVG inválido {item['id']}: {e}")
  exports=list(item['png'].values()) if kind=='icons' else [item['preview']]
  for export in exports:
   file=video_base/export['file'];check(file.is_file(),f"Exportación de edición ausente: {export['file']}")
   if file.is_file():
    data=file.read_bytes()
    check(data[:8]==b'\x89PNG\r\n\x1a\n',f"Exportación no PNG: {export['file']}")
    check(struct.unpack('>II',data[16:24])==(export['width'],export['height']),f"Tamaño de edición incorrecto: {export['file']}")
    check(data[25]==6,f"PNG de edición sin RGBA: {export['file']}")
    check(hashlib.sha256(data).hexdigest()==export['sha256'],f"PNG de edición divergente: {export['file']}")
check(len(video_ids)==len(set(video_ids)),'IDs duplicados en kit de edición')
motion=read('marca/video/v01/motion.json')
check(motion['implementation']=='especificacion_sin_render','Motion de edición presentado como implementado')
presets={p['id'] for p in motion['presets']}
for item in video['components']:check(item['motion_preset'] in presets,f"Preset ausente: {item['id']}")
for preset in motion['presets']:
 for phase in ('entry','exit'):
  points=preset[phase];times=[point['t_ms'] for point in points]
  check(times==sorted(times) and times[0]==0 and times[-1]==preset[phase+'_ms'],f"Tiempo de motion inválido: {preset['id']}/{phase}")
board=video_base/video['board']['file'];check(board.is_file(),'Mesa visual ausente')
if board.is_file():check(hashlib.sha256(board.read_bytes()).hexdigest()==video['board']['sha256'],'Mesa visual divergente')

# Portable agent entrypoints and derived resource registry.
def repo_path(value,label,base=R):
 try:
  path=Path(value)
  if path.is_absolute():raise ValueError('ruta absoluta')
  result=(base/path).resolve()
  result.relative_to(R)
  check(result.exists(),f"Ruta ausente {label}: {value}")
  return result
 except (ValueError,TypeError):
  check(False,f"Ruta fuera del repositorio o inválida {label}: {value}")
  return None

project=read('proyecto.json')
for name,value in project['entrypoints'].items():repo_path(value,'entrada '+name)
for name,value in project['context'].items():repo_path(value,'contexto '+name)
route_ids=[]
for route in project['routes']:
 route_ids.append(route['id'])
 if route['skill']:repo_path(route['skill'],'skill '+route['id'])
 for value in route['read']:repo_path(value,'lectura '+route['id'])
 repo_path(route['output_directory'],'salida '+route['id'])
check(len(route_ids)==len(set(route_ids)),'Rutas de trabajo duplicadas')
for field in ('episode_template','episode_index','resource_generator','validation'):repo_path(project[field],field)
try:
 from catalogar_recursos import build_catalog
except ImportError:
 # El nombre de script contiene guion para mantener las convenciones del repo.
 import importlib.util
 spec=importlib.util.spec_from_file_location('catalogar_recursos',R/'scripts/catalogar-recursos.py')
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 build_catalog=module.build_catalog
try:
 resources=read('marca/recursos.json')
 check(resources==build_catalog(),'Índice común desactualizado; ejecutar scripts/catalogar-recursos.py')
 resource_ids={item['id'] for item in resources['resources']}
 check(len(resource_ids)==len(resources['resources']),'IDs de recursos duplicados')
 for item in resources['resources']:
  for file in item['files']:repo_path(file['path'],'recurso '+item['id'])
  if 'motion_id' in item:check(item['motion_id'] in resource_ids,f"Movimiento sin recurso: {item['id']}")
except (OSError,ValueError,KeyError) as e:
 check(False,f"Índice común inválido: {e}")
 resource_ids=set()

# New episode metadata separates progress, review and publication authorization.
episode_ids=[]
indexed_paths=set()
episodes=read('produccion/episodios/catalogo.json')
for row in episodes['episodes']:
 episode_ids.append(row['episode_id'])
 p=repo_path(row['path'],'episodio '+row['episode_id'])
 if p is None or not p.is_file():continue
 indexed_paths.add(p.resolve())
 try:
  ep=json.loads(p.read_text(encoding='utf-8'))
  check(ep['episode_id']==row['episode_id'],f"ID de episodio divergente: {p}")
  check(ep['status'] in {'borrador','en_revision','aprobado','descartado'},f"Estado inválido: {p}")
  check(ep['stage'] in {'idea','preparacion','captura','preedicion','revision','entrega','publicado'},f"Etapa inválida: {p}")
  check(ep['experience_status'] in {'por_confirmar','planificada','realizada'},f"Experiencia inválida: {p}")
  if ep['status']=='aprobado':
   check(all(ep['approval'].get(k) for k in ('decided_by','decided_at','scope','decision_source')),f"Aprobación sin evidencia: {p}")
  if ep['stage']=='publicado':
   check(all(ep['publication'].get(k) for k in ('requested','request_source','published_at','url')),f"Publicación sin registro completo: {p}")
  for value in ep['documents'].values():repo_path(value,'documento del episodio',p.parent)
  for resource_id in ep['resource_ids']:check(resource_id in resource_ids,f"Recurso desconocido en episodio: {resource_id}")
 except (OSError,ValueError,KeyError,TypeError) as e:check(False,f"Metadatos de episodio inválidos: {p}: {e}")
check(len(episode_ids)==len(set(episode_ids)),'IDs de episodios duplicados')
for p in (R/'produccion/episodios').rglob('episodio.json'):
 if not skip_file(p):check(p.resolve() in indexed_paths,f"Episodio sin registrar: {p.relative_to(R)}")

video_html=(R/'marca/video/v01/index.html').read_text(encoding='utf-8')
html_ids=re.findall(r'\bid="([^"]+)"',video_html)
check(len(html_ids)==len(set(html_ids)),'IDs duplicados en módulo de video')
check('href="video/v01/index.html"' in ds,'Design system sin acceso al módulo de video')
check('href="../../design-system.html#video"' in video_html,'Módulo de video sin retorno a la guía')
for folder,filename in [('logo-al-destino','AL-DESTINO-logo-animado.png'),('logo-circular','AL-DESTINO-logo-circular-animado.png')]:
 check(f'../../motion/{folder}/renders/{filename}' in video_html,f"Animación existente sin enlazar: {folder}")

print(f'{checks} comprobaciones; {len(errors)} fallos.')
for e in errors:print('ERROR:',e)
sys.exit(bool(errors))
