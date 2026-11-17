/* Iconos propios; el logo se reutiliza sin redibujar ni recolorear. */
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {pathToFileURL}=require('url');const {chromium}=require('playwright');
const root=path.resolve(__dirname,'..'),source=path.join(root,'marca/video/v04'),out=path.join(root,'marca/exportaciones/video-v04');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const write=(p,s)=>fs.writeFileSync(p,s+'\n');
const tokens=JSON.parse(fs.readFileSync(path.join(root,'marca/tokens/brand_tokens.json'),'utf8'));
const colors={universal:'#FFFDF5',claro:'#FFFDF5',oscuro:tokens.color.cafe_oscuro.$value,acento:tokens.color.turquesa.$value};
const hand='M12.5 14.7C14.2 12.4 15.8 9.9 17 7c.3-.7.5-1.4.6-2.1.1-.9.8-1.5 1.6-1.2 1.8.7 2.7 2.4 2.5 4.3l-.7 5.2h5.1c1.5 0 2.6 1.3 2.3 2.8l-1.8 9.4c-.2 1.3-1.3 2.2-2.6 2.2h-8.8l-2.7-1.3Z';
const icons=[
 {id:'like',title:'Like · contorno',role:'Opinión contextual o CTA según el evento; no implica una cantidad de likes.',body:`<path d="${hand}"/><rect x="4.5" y="14.2" width="5.4" height="13.4" rx="1.1"/>`},
 {id:'like-activo',title:'Like · énfasis',role:'Estado visual alternativo del like; no es animación ni puntuación por sí mismo.',body:`<path d="${hand}" fill="currentColor"/><rect x="4.5" y="14.2" width="5.4" height="13.4" rx="1.1"/>`},
 {id:'ubicacion',title:'Pin de ubicación',role:'Junto al nombre confirmado del lugar; el pin no representa coordenadas ni un mapa exacto.',body:'<path d="M25 12.6c0 6.5-9 15.1-9 15.1S7 19.1 7 12.6a9 9 0 1 1 18 0Z"/><circle cx="16" cy="12.5" r="3.25"/>'},
 {id:'corazon',title:'Corazón',role:'Afinidad o invitación contextual; no sustituye ni inventa una reacción de Arturo o Liz.',body:'<path d="M16 27S4.5 19.6 4.5 12.7c0-6.4 8.1-8.5 11.5-3.2 3.4-5.3 11.5-3.2 11.5 3.2C27.5 19.6 16 27 16 27Z"/>'}
];
function svg(item,color){const edge=color===colors.oscuro?'#FFFDF5':'#18231F';return `<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 32 32"><title>${item.title} · AL DESTINO · BORRADOR</title><defs><filter id="shadow" x="-25%" y="-25%" width="150%" height="160%"><feDropShadow dx="0" dy=".28" stdDeviation=".32" flood-color="#08100D" flood-opacity=".32"/></filter></defs><g filter="url(#shadow)" style="color:${edge}" fill="none" stroke="currentColor" stroke-width="2.55" stroke-linecap="round" stroke-linejoin="round">${item.body}</g><g style="color:${color}" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round">${item.body}</g></svg>`;}
async function main(){
 for(const dir of [source,out,...Object.keys(colors).map(c=>path.join(out,c))])fs.mkdirSync(dir,{recursive:true});
 const browser=await chromium.launch({headless:true,...(process.env.AL_DESTINO_BROWSER?{executablePath:process.env.AL_DESTINO_BROWSER}:{})});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1100}});
  await page.setContent('<style>html,body{margin:0;background:transparent}#asset{width:max-content;line-height:0}</style><div id="asset"></div>');
  const items=[];
  for(const item of icons){
   const file=item.id+'.svg';write(path.join(source,file),svg(item,colors.oscuro));const png={};
   for(const [variant,color] of Object.entries(colors)){
    const target=path.join(out,variant,item.id+'.png');await page.locator('#asset').evaluate((el,s)=>el.innerHTML=s,svg(item,color));await page.locator('#asset svg').screenshot({path:target,omitBackground:true});
    png[variant]={file:'../../exportaciones/video-v04/'+variant+'/'+item.id+'.png',sha256:hash(target),width:512,height:512,alpha:true};
   }
   items.push({id:item.id,title:item.title,role:item.role,source:file,source_sha256:hash(path.join(source,file)),png,status:'borrador'});
  }
  const original=path.join(root,'marca/assets/logos/piezas/logo-horizontal-transparente.png');
  fs.copyFileSync(original,path.join(out,'logo-horizontal.png'));
  const parts=JSON.parse(fs.readFileSync(path.join(root,'marca/assets/logos/piezas/catalogo.json'),'utf8'));
  const selected=parts.items.filter(p=>['letra-a','letra-l','sol','ola'].includes(p.id));
  const box={x:Math.min(...selected.map(p=>p.x))-parts.crop_origin_px[0],y:Math.min(...selected.map(p=>p.y))-parts.crop_origin_px[1],width:Math.max(...selected.map(p=>p.x+p.width))-Math.min(...selected.map(p=>p.x)),height:Math.max(...selected.map(p=>p.y+p.height))-Math.min(...selected.map(p=>p.y))};
  const encoded=await page.evaluate(async({src,box})=>{const image=new Image();image.src=src;await image.decode();const c=document.createElement('canvas');c.width=box.width;c.height=box.height;const ctx=c.getContext('2d');ctx.drawImage(image,box.x,box.y,box.width,box.height,0,0,box.width,box.height);return c.toDataURL('image/png').split(',')[1];},{src:'data:image/png;base64,'+fs.readFileSync(original).toString('base64'),box});
  const mono=path.join(out,'monograma-transparente.png');fs.writeFileSync(mono,Buffer.from(encoded,'base64'));
  async function support(input,filename){
   const bytes=fs.readFileSync(input),w=bytes.readUInt32BE(16),h=bytes.readUInt32BE(20),pad=14,href='data:image/png;base64,'+bytes.toString('base64');
   const markup=`<svg xmlns="http://www.w3.org/2000/svg" width="${w+2*pad}" height="${h+2*pad}" viewBox="0 0 ${w+2*pad} ${h+2*pad}"><defs><filter id="edge" x="-20%" y="-25%" width="140%" height="160%"><feMorphology in="SourceAlpha" operator="dilate" radius="2.2" result="expanded"/><feFlood flood-color="#FFFDF5" result="paper"/><feComposite in="paper" in2="expanded" operator="in"/><feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#07120E" flood-opacity=".3"/></filter></defs><image href="${href}" x="${pad}" y="${pad}" width="${w}" height="${h}" filter="url(#edge)"/><image href="${href}" x="${pad}" y="${pad}" width="${w}" height="${h}"/></svg>`;
   await page.locator('#asset').evaluate((el,s)=>el.innerHTML=s,markup);await page.locator('#asset svg').screenshot({path:path.join(out,filename),omitBackground:true});
   return{file:'../../exportaciones/video-v04/'+filename,sha256:hash(path.join(out,filename)),padding_px:pad,method:'raster_original_con_apoyo_de_alfa_detras_sin_placa'};
  }
  const logos={source:'../../assets/logos/piezas/logo-horizontal-transparente.png',source_sha256:hash(original),horizontal:{file:'../../exportaciones/video-v04/logo-horizontal.png',sha256:hash(path.join(out,'logo-horizontal.png')),method:'copia_exacta'},monogram:{file:'../../exportaciones/video-v04/monograma-transparente.png',sha256:hash(mono),crop_xywh:box,method:'recorte_sin_escalado_del_raster_existente'},horizontal_overlay:await support(original,'logo-horizontal-contraste.png'),monogram_overlay:await support(mono,'monograma-contraste.png'),policy:'Rasters originales conservados; variantes overlay con apoyo de alfa por detrás, sin redibujar ni recolorear el frente.'};
  write(path.join(source,'catalogo.json'),JSON.stringify({brand:'AL DESTINO',version:'0.4.1',status:'borrador',created_at:'2026-11-16',generator:'scripts/generar-kit-iconos-editoriales.cjs',direction:'Kit editorial de likes, ubicación y firma; PNG transparentes sin placa.',colors,default_variant:'universal',source:'Geometrías propias y raster original del logo conservado.',items,logos,motion_references:['marca/motion/logo-al-destino/renders/catalogo.json','marca/motion/logo-circular/renders/catalogo.json','marca/motion/logo-al-destino/premium/renders/catalogo.json'],compatibility:'sin_prueba_en_clipo'},null,2));
  const heads=icons.map(i=>`<th>${i.title}</th>`).join('');
  const tests=['light','dark','detail'].map(cls=>`<tr><th>${{light:'Claro',dark:'Oscuro',detail:'Detalle'}[cls]}</th>${icons.map(i=>`<td class="${cls}"><img src="universal/${i.id}.png" alt="${i.title}"></td>`).join('')}</tr>`).join('');
  const html=`<!doctype html><html lang="es"><meta charset="utf-8"><title>AL DESTINO · Iconos sobre imagen · BORRADOR</title><style>@font-face{font-family:J;src:url('../../assets/fuentes/PlusJakartaSans%5Bwght%5D.ttf')}*{box-sizing:border-box}body{margin:0;background:#f3f3f1;color:#232725;font-family:J,Arial,sans-serif;padding:42px}small{letter-spacing:3px;font-weight:700}h1{font-size:38px;letter-spacing:-1.4px}p{line-height:1.5;max-width:1060px}table{width:100%;border-collapse:separate;border-spacing:8px}th{font-size:14px;text-align:left;padding:8px}td{height:130px;text-align:center}td img{width:80px;height:80px;vertical-align:middle}.light{background:#fff}.dark{background:#111}.detail{background:repeating-linear-gradient(32deg,#fafafa 0 6px,#777 6px 12px,#222 12px 19px,#ccc 19px 24px)}.logos{display:grid;grid-template-columns:1fr 1fr;gap:10px}.logos>div{padding:35px;text-align:center}.logos img{width:250px;max-height:150px;object-fit:contain}.note{font-size:13px}a{color:inherit}</style><small>AL DESTINO / PNG PARA SUPERPONER / BORRADOR</small><h1>El mismo PNG sobre claro, oscuro y detalle.</h1><p>Contorno de contraste fino y sombra local. Sin soporte rectangular. Las tres filas usan exactamente el mismo archivo universal; los fondos sólo son una prueba técnica. La prueba con tomas propias se conserva con el episodio.</p><table><tr><th>Prueba</th>${heads}</tr>${tests}</table><h2>Firma con apoyo de contraste</h2><div class="logos"><div class="light"><img src="monograma-contraste.png" alt="Monograma con apoyo de alfa sobre claro"></div><div class="dark"><img src="monograma-contraste.png" alt="El mismo monograma sobre oscuro"></div></div><p class="note">El dibujo y los colores originales permanecen delante; el apoyo de alfa va por detrás. También se conservan las copias originales sin apoyo. No se ha verificado la importación en Clipo.</p><a href="../../motion/logo-al-destino/premium/revision.html">Ver la animación por piezas</a> · <a href="../../design-system.html#video">Design system</a></html>`;
  write(path.join(out,'index.html'),html);await page.goto(pathToFileURL(path.join(out,'index.html')).href);await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(out,'mesa-de-revision.png'),fullPage:true});
  console.log('16 PNG de iconos con contraste local y firmas originales/protegidas. BORRADOR.');
 }finally{await browser.close();}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
