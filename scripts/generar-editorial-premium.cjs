/* Fuentes reproducibles de overlays editoriales. BORRADOR; no modifica episodios. */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');
const base = path.join(root, 'marca/motion/editorial-v01');
const output = path.join(root, 'marca/exportaciones/editorial-v01');
const hash = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const write = (p, text) => { fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, text + '\n'); };
const json = (p, obj) => write(p, JSON.stringify(obj, null, 2));
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const rel = (from, file) => path.relative(from, file).split(path.sep).join('/');
const font = path.join(root, 'marca/assets/fuentes/PlusJakartaSans[wght].ttf');
const gsap = path.join(root, 'marca/motion/logo-al-destino/assets/gsap.min.js');
const symbols = path.join(base, 'assets/social');
const variants = [
  ...['instagram','youtube','tiktok'].map(platform => ({id:'redes.'+platform, slug:'redes-'+platform, title:platform[0].toUpperCase()+platform.slice(1), kind:'redes', duration:6, platform, account:'[cuenta por confirmar]', invitation:'Síguenos en', confirmed:false, is_mockup:true})),
  {id:'lugar',slug:'lugar',title:'Lugar / restaurante',kind:'lugar',duration:6,category:'Restaurante · demostración',place_name:'[Nombre del lugar]',locality:'[Ciudad por confirmar]',show_pin:true,confirmed:false,is_mockup:true},
  {id:'mapa',slug:'mapa',title:'Ubicación / mapa',kind:'mapa',duration:6,place_name:'[Lugar por confirmar]',locality:'Plantilla · sustituir por mapa verificado',map_attribution:'DEMOSTRACIÓN · esquema sin ubicación real',pin_x:.61,pin_y:.48,confirmed:false,is_mockup:true},
  {id:'flecha-curva',slug:'flecha-curva',title:'Flecha curva',kind:'flecha',duration:4,shape:'curva',is_mockup:false},
  {id:'flecha-bucle',slug:'flecha-bucle',title:'Flecha con bucle',kind:'flecha',duration:4,shape:'bucle',is_mockup:false},
  {id:'like',slug:'like',title:'Like editorial',kind:'like',duration:4,is_mockup:false}
];

function required(c, names) { for(const key of names) if(typeof c[key] !== 'string' || !c[key].trim()) throw Error('Falta '+key); }
function validate(c) {
  if(!Number.isFinite(c.duration)||c.duration<3||c.duration>30)throw Error('duration debe estar entre 3 y 30 segundos.');
  for(const key of ['place_name','account','category','locality','invitation']) if(c[key] && (typeof c[key]!=='string'||c[key].length>110)) throw Error(key+' demasiado largo o de tipo incorrecto: acortar el texto o preparar otra composición.');
  if(c.is_mockup) return;
  if(['redes','lugar','mapa'].includes(c.kind) && c.confirmed !== true) throw Error('Datos sin confirmar: no generar pieza real.');
  if(c.kind==='redes') {
    required(c,['account','account_url']);
    if(!/^https:\/\//.test(c.account_url)) throw Error('account_url debe ser un enlace HTTPS confirmado.');
    if(/[\[\]]/.test(c.account)) throw Error('La cuenta real no puede contener un placeholder.');
  }
  if(c.kind==='lugar') { required(c,['place_name','category','locality','source','observed_at']); if(/[\[\]]/.test(c.place_name)) throw Error('Nombre de lugar pendiente.'); }
  if(c.kind==='mapa') {
    required(c,['place_name','locality','place_url','map_file','map_source','map_attribution','observed_at']);
    if(c.location_verified!==true) throw Error('Confirmar ubicación y pin antes de generar el mapa real.');
    if(!fs.existsSync(c.map_file)) throw Error('No existe map_file.');
    if(![c.pin_x,c.pin_y].every(n=>typeof n==='number'&&n>=0&&n<=1)) throw Error('pin_x/pin_y deben estar entre 0 y 1 sobre la imagen suministrada.');
    if(![c.map_width_px,c.map_height_px].every(n=>Number.isInteger(n)&&n>0)) throw Error('Indicar dimensiones reales map_width_px/map_height_px.');
  }
}

function svgContent(file) {
  return fs.readFileSync(file,'utf8').replace(/<svg\b/, '<svg class="symbol"').replace(/<title>[\s\S]*?<\/title>/g,'').replace(/role="img"/g,'aria-hidden="true"');
}
function genericSvg(shape) {
  const d=shape==='bucle'?'M60 200 C100 200 171 138 161 101 C151 69 103 116 129 145 C166 190 252 145 313 71':'M52 205 C70 105 163 60 302 80';
  const tip=shape==='bucle'?'M283 76 L313 71 L306 101':'M276 57 L302 80 L270 98';
  return `<svg class="arrow" viewBox="0 0 360 260" xmlns="http://www.w3.org/2000/svg" aria-label="Flecha ${shape}"><defs><filter id="arrow-shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="1.5" stdDeviation="1.5" flood-color="#10211D" flood-opacity=".65"/></filter></defs><g fill="none" stroke-linecap="round" stroke-linejoin="round" filter="url(#arrow-shadow)"><path pathLength="1000" class="ink-support" d="${d}"/><path pathLength="1000" class="tip-support" d="${tip}"/><path pathLength="1000" class="ink" d="${d}"/><path pathLength="1000" class="tip" d="${tip}"/></g></svg>`;
}
function demoMap() {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="#E3DEC9"/><path d="M0 0H410C550 165 230 290 420 470S610 830 400 1080H0Z" fill="#287C7A" opacity=".4"/><g fill="none" stroke="#fffdf5" stroke-width="35"><path d="M500 0L1600 1080M1920 90L520 1080M810 0L650 1080M0 650L1920 430"/></g><g fill="none" stroke="#b6b4a4" stroke-width="5"><path d="M500 0L1600 1080M1920 90L520 1080M810 0L650 1080M0 650L1920 430"/></g><text x="770" y="180" font-family="sans-serif" font-size="34" fill="#302722">ESQUEMA DE DEMOSTRACIÓN</text><text x="770" y="228" font-family="sans-serif" font-size="26" fill="#302722">Sin calles, ruta ni ubicación reales</text></svg>`;
}
function compose(c) {
  const duration=c.duration, end=duration-.4;
  let markup='', motion='', style='';
  if(c.kind==='redes') {
    markup=`<div id="graphic" class="social"><div class="brand-symbol" id="symbol">${svgContent(path.join(symbols,c.platform+'.svg'))}</div><div id="divider"></div><div class="social-copy"><div id="invitation" class="kicker" data-var-text="invitation">${esc(c.invitation)}</div><div class="account-clip"><div id="account" data-var-text="account">${esc(c.account)}</div></div></div></div>`;
    style=`.social{display:flex;align-items:center;gap:27px;width:1140px;min-height:132px}.brand-symbol{width:80px;height:80px;flex:none;filter:drop-shadow(0 1px 2px #10211D)}.symbol{width:100%;height:100%;fill:#FFFDF5;stroke:#10211D;stroke-width:.12;paint-order:stroke fill}#divider{width:2px;height:112px;background:#FFFDF5;flex:none;box-shadow:0 1px 2px #10211D}.social-copy{min-width:0;width:1004px}.kicker{font-size:32px;font-weight:500;line-height:1.3;margin-bottom:9px}.account-clip{overflow:hidden;padding:8px 8px 8px 0;margin:-8px -8px -8px 0}#account{font-size:${Math.max(36,Math.min(54,Math.floor(1004/(String(c.account).length*.57))))}px;line-height:1.24;font-weight:750;letter-spacing:-.7px;overflow-wrap:anywhere;max-width:1004px}`;
    motion=`tl.fromTo('#divider',{scaleY:0,opacity:0},{scaleY:1,opacity:1,duration:.34,ease:'power3.out',transformOrigin:'50% 50%'},.08);tl.fromTo('#symbol',{x:30,opacity:0},{x:0,opacity:1,duration:.38,ease:'power4.out'},.25);tl.fromTo('#invitation',{x:-18,opacity:0},{x:0,opacity:1,duration:.4,ease:'power3.out'},.34);tl.fromTo('#account',{x:-200,opacity:0,filter:'blur(9px)'},{x:0,opacity:1,filter:'blur(0px)',duration:.48,ease:'power4.out'},.4);tl.to('#account',{x:-180,opacity:0,filter:'blur(8px)',duration:.29,ease:'power3.in'},${end-.45});tl.to('#invitation',{x:-12,opacity:0,duration:.23,ease:'power2.in'},${end-.35});tl.to('#symbol',{x:24,opacity:0,duration:.28,ease:'power3.in'},${end-.27});tl.to('#divider',{scaleY:0,opacity:0,duration:.22,ease:'power3.in'},${end});`;
  } else if(c.kind==='lugar') {
    markup=`<div id="graphic" class="place">${c.show_pin?`<div id="pin">${svgContent(path.join(root,'marca/video/v04/ubicacion.svg'))}</div>`:''}<div id="place-copy"><div class="category" data-var-text="category">${esc(c.category)}</div><div class="place-name" data-var-text="place_name">${esc(c.place_name)}</div><div class="locality" data-var-text="locality">${esc(c.locality)}</div></div></div>`;
    style='.place{display:flex;align-items:center;gap:25px;width:1400px;min-height:164px}#pin{width:84px;height:84px;flex:none}.symbol{width:100%;height:100%}.category{font-size:36px;font-weight:500;line-height:1.3;margin-bottom:6px}.place-name{font-size:68px;font-weight:780;letter-spacing:-1.7px;line-height:1.14;max-width:1290px;overflow-wrap:anywhere}.locality{font-size:30px;font-weight:500;line-height:1.3;margin-top:9px}';
    motion=`tl.fromTo('#graphic',{x:-130,opacity:0,filter:'blur(9px)'},{x:0,opacity:1,filter:'blur(0px)',duration:.46,ease:'power4.out'},.08);tl.to('#graphic',{x:-140,opacity:0,filter:'blur(9px)',duration:.32,ease:'power3.in'},${duration-.52});`;
  } else if(c.kind==='mapa') {
    const iw=c.map_width_px||1920,ih=c.map_height_px||1080,scale=Math.min(1728/iw,690/ih),w=iw*scale,h=ih*scale,left=(1920-w)/2,top=66+(690-h)/2;
    markup=`<div id="map-scene"><div id="map-world" style="left:${left}px;top:${top}px;width:${w}px;height:${h}px"><img id="map-image" src="assets/mapa.svg" alt="${c.is_mockup?'Esquema de demostración sin ubicación real':'Mapa de '+esc(c.place_name)}" style="width:100%;height:100%"><div id="map-pin" style="left:${c.pin_x*100}%;top:${c.pin_y*100}%">${svgContent(path.join(root,'marca/video/v04/ubicacion.svg'))}</div></div><div class="map-heading"><div class="category">${esc(c.is_mockup?'DEMOSTRACIÓN · SIN UBICACIÓN REAL':c.locality)}</div><div class="place-name" data-var-text="place_name">${esc(c.place_name)}</div></div><div id="attribution">${esc(c.map_attribution)}</div></div>`;
    style='#map-scene{position:absolute;inset:0;overflow:hidden;background:#E3DEC9;color:#302722;text-shadow:none}#map-world{position:absolute;transform-origin:50% 50%}#map-pin{position:absolute;width:80px;height:80px;margin-left:-40px;margin-top:-69.25px}.symbol{width:100%;height:100%}.map-heading{position:absolute;left:192px;top:796px;max-width:1300px;padding:16px 24px;background:#E3DEC9}.map-heading .category{font-size:30px;line-height:1.4;margin-bottom:8px}.map-heading .place-name{font-size:64px;font-weight:750;letter-spacing:-1px;line-height:1.15}#attribution{position:absolute;left:96px;bottom:42px;font-size:26px;font-weight:600;padding:9px 16px;background:#E3DEC9;max-width:1728px;line-height:1.3}';
    motion=`tl.fromTo('#map-scene',{opacity:0},{opacity:1,duration:.24,ease:'power2.out'},.04);tl.fromTo('#map-world',{scale:1},{scale:1.02,duration:${duration-.6},ease:'sine.inOut'},.1);tl.fromTo('#map-pin',{scale:.86,opacity:0},{scale:1,opacity:1,duration:.44,ease:'power4.out',transformOrigin:'50% 100%'},.34);tl.to('#map-scene',{opacity:0,duration:.24,ease:'power2.in'},${duration-.32});`;
  } else if(c.kind==='flecha') {
    markup=`<div id="graphic" class="arrow-stage">${genericSvg(c.shape)}</div>`;
    style='.arrow-stage{width:360px;height:260px}.arrow{width:100%;height:100%}.ink-support,.tip-support{stroke:#10211D;stroke-width:7;opacity:.68}.ink,.tip{stroke:#FFFDF5;stroke-width:4}.ink,.ink-support{stroke-dasharray:1000;stroke-dashoffset:1000}.tip,.tip-support{opacity:0}';
    motion=`tl.fromTo('#graphic',{opacity:0},{opacity:1,duration:.1},.08);tl.to('.ink,.ink-support',{strokeDashoffset:0,duration:.66,ease:'power2.inOut'},.12);tl.to('.tip,.tip-support',{opacity:1,duration:.13,ease:'power2.out'},.68);tl.to('#graphic',{opacity:0,duration:.28,ease:'power2.in'},${duration-.4});`;
  } else {
    markup=`<div id="graphic" class="like">${svgContent(path.join(root,'marca/video/v04/like.svg'))}</div>`;
    style='.like{width:105px;height:105px}.symbol{width:100%;height:100%}';
    motion=`tl.fromTo('#graphic',{y:24,scale:.9,opacity:0},{y:0,scale:1,opacity:1,duration:.46,ease:'power4.out',transformOrigin:'50% 50%'},.08);tl.to('#graphic',{y:-8,opacity:0,duration:.28,ease:'power3.in'},${duration-.4});`;
  }
  const vars=['invitation','account','category','place_name','locality'].filter(x=>c[x]).map(id=>({id,type:'string',label:id,default:c[id]}));
  return `<!doctype html><html lang="es" data-composition-variables='${esc(JSON.stringify(vars))}'><head><meta charset="utf-8"><title>${esc(c.title)} · AL DESTINO · BORRADOR</title><script src="assets/gsap.min.js"></script><style>@font-face{font-family:'Plus Jakarta Sans';src:url('assets/fonts/PlusJakartaSans.ttf');font-weight:200 800}*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:transparent;font-family:'Plus Jakarta Sans',sans-serif;color:#FFFDF5}#root{width:100%;height:100%;position:relative;background:transparent}#placement{position:absolute;left:192px;bottom:130px;max-width:1536px;text-shadow:0 1px 2px #10211D,0 0 3px rgba(16,33,29,.65)}${style}</style></head><body><div id="root" class="clip" data-composition-id="${c.slug}" data-start="0" data-duration="${duration}" data-width="1920" data-height="1080" data-fps="30" data-track-kind="graphics" data-motion-blur="on">${c.kind==='mapa'?markup:`<div id="placement">${markup}</div>`}</div><script>const tl=gsap.timeline({paused:true});${motion}window.__timelines=window.__timelines||{};window.__timelines['${c.slug}']=tl;tl.seek(0);</script></body></html>`;
}

function generate(c, dir) {
  validate(c); fs.mkdirSync(dir,{recursive:true});
  const assets=path.join(dir,'assets');fs.mkdirSync(path.join(assets,'fonts'),{recursive:true});
  fs.copyFileSync(font,path.join(assets,'fonts/PlusJakartaSans.ttf'));fs.copyFileSync(gsap,path.join(assets,'gsap.min.js'));
  if(c.kind==='mapa') {
    if(c.is_mockup)write(path.join(assets,'mapa.svg'),demoMap());
    else {const extension=path.extname(c.map_file).toLowerCase();if(!['.png','.jpg','.jpeg','.webp','.svg'].includes(extension))throw Error('Formato de mapa no admitido.');fs.copyFileSync(c.map_file,path.join(assets,'mapa'+extension));c.map_asset='mapa'+extension;}
  }
  let html=compose(c);if(c.map_asset)html=html.replace('assets/mapa.svg','assets/'+c.map_asset);
  write(path.join(dir,'index.html'),html);json(path.join(dir,'config.json'),c);
  json(path.join(dir,'hyperframes.json'),{paths:{assets:'assets',blocks:'compositions',components:'components'}});
  json(path.join(dir,'package.json'),{name:'al-destino-'+c.slug,private:true,type:'module',devDependencies:{hyperframes:'0.9.59'}});
  json(path.join(dir,'index.motion.json'),{duration:c.duration,assertions:[{kind:'appearsBy',selector:c.kind==='mapa'?'#map-scene':'#graphic',bySec:1.2}]});
}

function gallery(items) {
  return `<!doctype html><html lang="es"><meta charset="utf-8"><title>AL DESTINO · Editorial animado · BORRADOR</title><style>@font-face{font-family:J;src:url('../../assets/fuentes/PlusJakartaSans%5Bwght%5D.ttf');font-weight:200 800}*{box-sizing:border-box}body{margin:0;background:#eeeade;color:#302722;font-family:J,sans-serif;padding:52px}main{max-width:1440px;margin:auto}small{font-size:12px;letter-spacing:2px;font-weight:750}h1{font-size:46px;letter-spacing:-2px;line-height:1.1;max-width:950px}p{line-height:1.65;max-width:1050px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:35px}.card{background:#fffdf5;padding:22px}.card h2{margin:6px 0 10px;font-size:23px}.badge{font-size:12px;font-weight:750;color:#244B49}.screen{background:repeating-linear-gradient(45deg,#d2d0c6 0 12px,#c0beb4 12px 24px);aspect-ratio:16/9;margin-top:18px}video{width:100%;height:100%;object-fit:contain}.links{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;margin-top:14px}a{color:#244B49;text-underline-offset:4px}.note{padding:20px 24px;border-left:3px solid #287C7A;background:#fffdf5}footer{margin-top:35px;font-size:13px}@media(max-width:800px){body{padding:22px}.grid{grid-template-columns:1fr}h1{font-size:34px}}</style><main><small>AL DESTINO / RECURSOS REUTILIZABLES / BORRADOR</small><h1>Identificar el lugar.<br>Dejar vivir la imagen.</h1><p>Rótulos sin placa, redes con revelado por fases y acentos de trazo. Fuentes HyperFrames editables con tipografía local y pausa de lectura estable. Todos los recursos conservan revisión editorial propia.</p><div class="note"><strong>Las cuentas y los lugares son MOCKUPS.</strong> Sustituir y confirmar los datos antes de producir una pieza real. El mapa es un esquema de demostración sin ubicación real. Flechas y like son elementos independientes reutilizables, sin escala de valoración implícita. El damero pertenece a esta mesa; no forma parte del alfa.</div><div class="grid">${items.map(i=>`<article class="card"><small class="badge">${i.is_mockup?'MOCKUP · DATOS PENDIENTES':'ELEMENTO REUTILIZABLE'} / ${i.duration_seconds} S</small><h2>${esc(i.title)}</h2><div class="screen"><video controls loop muted playsinline preload="metadata" poster="${i.slug}-poster.png" src="${i.slug}.webm"></video></div><div class="links"><a href="${i.slug}.webm">WebM transparente</a><a href="${i.slug}.png">APNG</a><a href="${i.slug}-poster.png">PNG fijo</a><a href="../../motion/editorial-v01/${i.composition_file}">Fuente editable</a>${i.kind==='redes'?`<a href="${i.slug}-simbolo.png">Símbolo PNG</a>`:''}</div></article>`).join('')}</div><footer><a href="../../design-system.html#video">← Design system</a> · <a href="../../motion/editorial-v01/catalogo.json">Catálogo y procedencia</a><p>Compatibilidad en Clipo pendiente: el render y el alfa son pruebas distintas de la importación y exportación en el editor.</p></footer></main></html>`;
}

function run() {
  const args=process.argv.slice(2),cfg=args.indexOf('--config'),out=args.indexOf('--out');
  const catalogOnly=args.includes('--catalog-only'),regenerate=args.includes('--write');
  if(cfg!==-1) {
    if(out===-1||!args[out+1])throw Error('--config requiere --out explícito para no sobrescribir las demos.');
    const raw=JSON.parse(fs.readFileSync(args[cfg+1],'utf8')),preset=variants.find(v=>v.id===raw.id);
    if(!preset)throw Error('id desconocido.');
    const c={...preset,...raw,id:preset.id,kind:preset.kind,slug:preset.slug,title:preset.title,is_mockup:raw.is_mockup===true};generate(c,path.resolve(args[out+1]));console.log('Fuente preparada: '+path.resolve(args[out+1]));return;
  }
  const items=[];for(const preset of variants) {
    const dir=path.join(base,'variantes',preset.slug),configPath=path.join(dir,'config.json');
    const c=fs.existsSync(configPath)?JSON.parse(fs.readFileSync(configPath,'utf8')):{...preset};
    if(c.id!==preset.id||c.kind!==preset.kind||c.slug!==preset.slug)throw Error('Identidad de variante modificada en '+configPath);
    if(!fs.existsSync(path.join(dir,'index.html'))){if(catalogOnly)throw Error('Falta la composición: '+preset.slug);generate(c,dir);}
    else if(regenerate)generate(c,dir);
    const fields=c.kind==='redes'?['platform','account','account_url','invitation','confirmed']:c.kind==='lugar'?['category','place_name','locality','show_pin','source','observed_at','confirmed']:c.kind==='mapa'?['place_name','locality','place_url','map_file','map_width_px','map_height_px','map_source','map_attribution','pin_x','pin_y','location_verified','observed_at','confirmed']:[];
    const sources=[['editable_composition',path.join(dir,'index.html')],['configuration',path.join(dir,'config.json')],['font',path.join(dir,'assets/fonts/PlusJakartaSans.ttf')],['animation_runtime',path.join(dir,'assets/gsap.min.js')]];
    if(c.kind==='redes')sources.push(['platform_symbol',path.join(symbols,c.platform+'.svg')]);
    if(['lugar','mapa'].includes(c.kind))sources.push(['pin_source',path.join(root,'marca/video/v04/ubicacion.svg')]);
    if(c.kind==='mapa')sources.push(['map_image',path.join(dir,'assets',c.map_asset||'mapa.svg')]);
    if(c.kind==='like')sources.push(['icon_source',path.join(root,'marca/video/v04/like.svg')]);
    const item={id:c.id,slug:c.slug,title:c.title,kind:c.kind,composition_file:rel(base,path.join(dir,'index.html')),config_file:rel(base,path.join(dir,'config.json')),is_mockup:c.is_mockup,fields,duration_seconds:c.duration,fps:30,size_px:[1920,1080],source_files:sources.map(([role,file])=>({file:rel(base,file),sha256:hash(file),role})),provenance_file:'procedencia.json',exports:{},compatibility:'pendiente_de_prueba_en_clipo',checks:{}};
    const assertions=path.join(dir,'index.motion.json');
    item.validation_files=[{file:rel(base,assertions),sha256:hash(assertions),role:'motion_assertions'}];
    for(const [role,extension] of [['webm','.webm'],['apng','.png'],['poster','-poster.png'],...(c.kind==='redes'?[['icon_png','-simbolo.png']]:[])]) {
      const file=path.join(output,c.slug+extension);if(fs.existsSync(file))item.exports[role]={file:rel(base,file),sha256:hash(file),width:role==='icon_png'?512:1920,height:role==='icon_png'?512:1080};
    }
    items.push(item);
  }
  const previous=fs.existsSync(path.join(base,'catalogo.json'))?JSON.parse(fs.readFileSync(path.join(base,'catalogo.json'),'utf8')):null;
  for(const item of items){
    const old=previous?.items?.find(i=>i.id===item.id);
    const fingerprint=crypto.createHash('sha256').update(JSON.stringify(item.source_files)).digest('hex');
    item.source_fingerprint=fingerprint;
    item.validation_fingerprint=crypto.createHash('sha256').update(JSON.stringify({source_fingerprint:fingerprint,files:item.validation_files})).digest('hex');
    const exportRoles=Object.keys(item.exports).sort(),oldExportRoles=Object.keys(old?.exports||{}).sort();
    const requiredRoles=['webm','apng','poster',...(item.kind==='redes'?['icon_png']:[])];
    const sameExports=old&&requiredRoles.every(role=>item.exports[role])&&
      exportRoles.length===oldExportRoles.length&&
      exportRoles.every((role,index)=>role===oldExportRoles[index]&&old.exports[role].sha256===item.exports[role].sha256);
    if(old&&sameExports&&JSON.stringify(old.source_files)===JSON.stringify(item.source_files)){
      item.checks={...old.checks};
      if(item.checks.webm_alpha_decoded&&!item.checks.render_source_fingerprint)item.checks.render_source_fingerprint=fingerprint;
      if(old.validation_fingerprint!==item.validation_fingerprint||item.checks.validation_fingerprint!==item.validation_fingerprint){item.checks.hyperframes_ok=false;item.checks.validation_pending=true;}
      item.render_status=old.checks?.webm_alpha_decoded?'render_verificado':'pendiente';
    }else{item.exports={};item.checks={};item.render_status='pendiente';}
    item.validation_status=item.checks.hyperframes_ok&&item.checks.validation_fingerprint===item.validation_fingerprint?'verificado':'pendiente';
  }
  json(path.join(base,'catalogo.json'),{brand:'AL DESTINO',version:'1.0',status:'borrador',generator:'scripts/generar-editorial-premium.cjs',renderer:'scripts/renderizar-editorial-premium.cjs',framework:'HyperFrames',framework_version:'0.9.59',audio:false,items});
  write(path.join(output,'index.html'),gallery(items));
  write(path.join(base,'BRIEF.md'),'# Editorial animado · BORRADOR\n\nPaquete de overlays para AL DESTINO, autorizado para preparar y renderizar como parte de la mejora horizontal. Fuente de intención: video vPsSfW0X_sI, ventanas registradas en la revisión documental. Ocho variantes, 1920 × 1080, 30 fps, sin audio, identidad actual conservada. Datos de muestra identificados como mockup; mapas reales sólo con ubicación e imagen verificadas. Fuentes locales; no publicar ni modificar episodios.');
  json(path.join(base,'shot-plan.json'),{status:'borrador',framework:'HyperFrames',canvas:[1920,1080],fps:30,export:'alpha-overlay',reference:'https://www.youtube.com/watch?v=vPsSfW0X_sI',registry_reference:'lt-mask-reveal',customization:'Revelado sin tarjeta; tipografía AL DESTINO, divisor de redes, entrada lateral con pausa nítida. Extensiones propias para flechas, like y mapa verificado.',variants:variants.map(v=>({id:v.id,duration_seconds:v.duration,is_mockup:v.is_mockup}))});
  console.log(catalogOnly?'Catálogo y mesa actualizados sin reescribir fuentes.':'Fuentes existentes conservadas; catálogo y mesa actualizados. --write regenera desde config.json.');
}
if(require.main===module){try{run();}catch(e){console.error(e.message);process.exitCode=1;}}
module.exports={variants,validate,generate,base,output,hash,rel};
