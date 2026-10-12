#!/usr/bin/env python3
"""Reúne recursos vigentes sin modificar originales ni composiciones."""
from pathlib import Path
import json, zipfile, hashlib, html
ROOT=Path(__file__).resolve().parents[1]
MARCA=ROOT/'marca'
OUT=MARCA/'exportaciones'
cat=json.loads((OUT/'v05-png/catalogo.json').read_text())
resources={
 '01-logos/logo-horizontal-arena.png':OUT/'v05-png/logos/logo-horizontal.png',
 '01-logos/logo-horizontal-transparente.png':MARCA/'assets/logos/piezas/logo-horizontal-transparente.png',
 '01-logos/logo-circular-arena.png':OUT/'v05-png/logos/avatar-1080.png',
}
for name,folder,filename in [('horizontal','logo-al-destino','AL-DESTINO-logo-animado.png'),('circular','logo-circular','AL-DESTINO-logo-circular-animado.png')]:
 base=MARCA/'motion'/folder/'renders'
 resources[f'02-animaciones/{name}/logo-animado.png']=base/filename
 for p in sorted((base/'secuencia-png').glob('*.png')):resources[f'02-animaciones/{name}/secuencia-png/{p.name}']=p
 resources[f'02-animaciones/{name}/poster.png']=base/('logo-poster.png' if name=='horizontal' else 'logo-circular-poster.png')
for item in cat['items']:resources['03-elementos-png/'+item['file']]=OUT/'v05-png'/item['file']
for p in (MARCA/'tokens').glob('*'):resources['04-tokens/'+p.name]=p
readme='''AL DESTINO · Kit de marca · BORRADOR

01-logos: horizontal sobre beige arena, horizontal transparente y circular.
02-animaciones: horizontal y circular; APNG + 96 cuadros PNG por versión.
03-elementos-png: 72 recursos agrupados por uso, incluidas piezas independientes.
04-tokens: colores, tipografía y espaciado.

Beige arena #E3DEC9. Animaciones de 3.2 s a 30 fps, sin audio.
Horizontal 1920 × 1080; circular 1080 × 1080. Importar secuencias a 30 fps.
El APNG usa extensión .png; algunas aplicaciones sólo muestran el primer cuadro.
La animación circular tiene exterior transparente y círculo beige.
Las historias y notas son exploraciones/placeholders; no son fotos ni experiencias reales.
Los logos reutilizan la extracción del original; no constituyen un vector maestro.
Guía editable y composiciones fuente: carpeta marca del repositorio.
'''
manifest={'status':'borrador','background':'#E3DEC9','files':[{'file':k,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for k,p in resources.items()]}
with zipfile.ZipFile(OUT/'AL-DESTINO-kit-marca.zip','w',zipfile.ZIP_DEFLATED) as z:
 for key,p in resources.items():z.write(p,key)
 z.writestr('LEEME.txt',readme);z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
(OUT/'kit-manifiesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
groups={}
for item in cat['items']:
 category=item.get('category',item['file'].split('/')[0]);groups.setdefault(category,[]).append(item)
cards=[]
for category,items in groups.items():
 cards.append(f'<section><h2>{html.escape(str(category))}</h2><div class="grid">')
 for item in items:
  url='v05-png/'+item['file'];name=item.get('name',item.get('title',Path(item['file']).stem))
  cards.append(f'<a href="{html.escape(url)}" download><img loading="lazy" src="{html.escape(url)}" alt="{html.escape(name)}"><span>{html.escape(name)} ↓</span></a>')
 cards.append('</div></section>')
(OUT/'index.html').write_text('''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AL DESTINO · Descargas · BORRADOR</title><style>*{box-sizing:border-box}body{margin:0;background:#FFFCF7;color:#2B211D;font-family:system-ui,sans-serif}main{max-width:1200px;margin:auto;padding:40px 24px}h1{font-family:Georgia,serif;font-size:42px}h2{margin-top:48px}a{color:inherit}nav{display:flex;gap:20px;flex-wrap:wrap}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px}.grid a{display:flex;flex-direction:column;border:1px solid #E3DEC9;text-decoration:none}.grid img{width:100%;height:190px;object-fit:contain;background:#E3DEC9}.grid span{padding:16px}.motion{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}.motion img{width:100%;height:280px;object-fit:contain;background:#E3DEC9}.motion article a{display:inline-block;margin:12px 16px 0 0}</style></head><body><main><nav><a href="../design-system.html#recursos">← Design system</a><a href="AL-DESTINO-kit-marca.zip" download>Kit completo ZIP ↓</a><a href="AL-DESTINO-elementos-PNG-v05.zip" download>72 elementos PNG ↓</a></nav><h1>Los recursos de AL DESTINO.</h1><p>BORRADOR · Beige arena #E3DEC9 · PNG individuales y paquetes organizados.</p><h2>Dos animaciones por elementos</h2><div class="motion"><article><img src="../motion/logo-al-destino/renders/AL-DESTINO-logo-animado.png" alt="Animación horizontal"><a href="../motion/logo-al-destino/renders/AL-DESTINO-logo-animado.png" download>Horizontal APNG ↓</a><a href="AL-DESTINO-logo-animacion-PNG.zip" download>Secuencia + piezas ↓</a></article><article><img src="../motion/logo-circular/renders/AL-DESTINO-logo-circular-animado.png" alt="Animación circular"><a href="../motion/logo-circular/renders/AL-DESTINO-logo-circular-animado.png" download>Circular APNG ↓</a><a href="AL-DESTINO-logo-circular-animacion-PNG.zip" download>Secuencia ↓</a></article></div>'''+''.join(cards)+'''</main></body></html>''')
print(f'Kit creado: {len(resources)} archivos + manifiesto y guía; catálogo: {len(cat["items"])} PNG.')
