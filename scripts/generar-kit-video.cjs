/* Kit gráfico de preedición AL DESTINO. Fuentes SVG + PNG + mesa de revisión.
   Requiere Playwright/Chromium; NODE_PATH permite usar dependencias ya instaladas.
   No genera motion: los presets son especificaciones para una prueba posterior. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname, '..');
const source = path.join(root, 'marca/video/v01');
const output = path.join(root, 'marca/exportaciones/video-v01');
const tokens = JSON.parse(fs.readFileSync(path.join(root, 'marca/tokens/brand_tokens.json'), 'utf8'));
const color = Object.fromEntries(Object.entries(tokens.color).map(([k,v]) => [k,v.$value]));
const date = '2026-11-14'; // Fecha de creación del diseño, no fecha dinámica de exportación.
const hash = file => crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
const write = (file, data) => {fs.mkdirSync(path.dirname(file), {recursive:true}); fs.writeFileSync(file, typeof data==='string'?data.replace(/[\t ]+$/gm,''):data);};
const json = (file, data) => write(file, JSON.stringify(data, null, 2)+'\n');
const escape = s => s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');

// Dibujos geométricos propios para este kit; no son logos oficiales ni piezas del logo AL DESTINO.
const icons = [
  ['ubicacion','Ubicación','<path d="M24 13c0 6-8 14-8 14S8 19 8 13a8 8 0 1 1 16 0Z"/><circle cx="16" cy="13" r="2.7"/>'],
  ['restaurante','Restaurante','<path d="M7 5v7m4-7v7M5 5v6a4 4 0 0 0 8 0V5M9 15v12m15 0V5c-5 2-6 7-6 12h6"/>'],
  ['hotel','Estancia','<path d="M5 27V8h22v19M10 8V5h12v3M13 27v-6h6v6M10 13h2m8 0h2m-12 4h2m8 0h2M3 27h26"/>'],
  ['precio','Precio','<path d="M5 7v10l10 10 13-13L18 4H8a3 3 0 0 0-3 3Z"/><circle cx="11" cy="10" r="1.8"/>'],
  ['horario','Horario','<circle cx="16" cy="16" r="11"/><path d="M16 9v7l5 3"/>'],
  ['estacionamiento','Estacionamiento','<rect x="5" y="5" width="22" height="22" rx="5"/><path d="M13 23V10h5a4 4 0 0 1 0 8h-5"/>'],
  ['reservacion','Reservación','<rect x="5" y="7" width="22" height="21" rx="4"/><path d="M10 4v6m12-6v6M5 14h22m-16 7 3 3 7-7"/>'],
  ['consejo','Consejo','<path d="M12 23h8m-7 4h6M11 20c0-3-4-4-4-9a9 9 0 0 1 18 0c0 5-4 6-4 9Z"/><path d="M13 11a3 3 0 0 1 3-3"/>'],
  ['pulgar-arriba','Nos gustó','<path d="M11 14 16 5c1-2 4-1 4 1v7h6c2 0 2 2 2 3l-3 10H11V14ZM5 14h6v12H5Z"/>'],
  ['pulgar-abajo','A considerar','<g transform="translate(32 32) rotate(180)"><path d="M11 14 16 5c1-2 4-1 4 1v7h6c2 0 2 2 2 3l-3 10H11V14ZM5 14h6v12H5Z"/></g>'],
  ['detalle','Detalle','<circle cx="14" cy="14" r="8"/><path d="m20 20 7 7M11 14h6m-3-3v6"/>'],
  ['redes','Redes · genérico','<path d="M11 8 13 5h6l2 3h5a3 3 0 0 1 3 3v13a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V11a3 3 0 0 1 3-3Z"/><circle cx="16" cy="17" r="5"/>'],
  ['flecha-curva-derecha','Mira aquí →','<path d="M4 26C5 13 13 6 26 8m-6-5 7 5-5 7"/>'],
  ['flecha-curva-izquierda','← Mira aquí','<g transform="translate(32 0) scale(-1 1)"><path d="M4 26C5 13 13 6 26 8m-6-5 7 5-5 7"/></g>'],
  ['confirmado','Confirmado','<path d="m7 16 6 6L26 8"/>'],
  ['atencion','Atención','<path d="m14 5-11 20a2 2 0 0 0 2 3h22a2 2 0 0 0 2-3L18 5a2.3 2.3 0 0 0-4 0Z"/><path d="M16 12v7m0 4v.1"/>']
];
const line = body => `<g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${body}</g>`;
const svg = (id, title, body) => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="256" height="256" role="img" aria-labelledby="icon-${id}-title" style="color:${color.cafe_oscuro}"><title id="icon-${id}-title">${escape(title)} · AL DESTINO · BORRADOR</title>${line(body)}</svg>`;
for(const [id,title,body] of icons) write(path.join(source,'iconos',id+'.svg'), svg(id,title,body));

const fields = [
  {id:'lugar', title:'Dónde estamos', icon:'ubicacion', eyebrow:'LUGAR · CONTEXTO', main:'[Nombre del lugar]', detail:'[Ciudad] · [Categoría]', inputs:['nombre','ciudad','categoria'], motion:'deslizar'},
  {id:'precio', title:'Precio con contexto', icon:'precio', eyebrow:'PRECIO DE LA EXPERIENCIA', main:'[Importe]', detail:'[Unidad] · [Fecha] · [Qué incluye]', inputs:['importe','moneda','unidad','fecha','condiciones'], motion:'enfatizar'},
  {id:'consejo', title:'Un consejo útil', icon:'consejo', eyebrow:'PARA TU VISITA', main:'[Consejo comprobado]', detail:'[Condición o detalle importante]', inputs:['titulo','detalle','icono'], motion:'deslizar'},
  {id:'opinion', title:'Nuestra opinión, con autor', icon:'pulgar-arriba', eyebrow:'ARTURO · [CRITERIO]', main:'[Lo que sí dijo Arturo]', detail:'Opinión personal · [Contexto]', inputs:['autor','criterio','comentario','contexto','valoracion_opcional'], motion:'aparecer'},
  {id:'presentacion', title:'Dos personas, una historia', icon:null, eyebrow:'VEN CON NOSOTROS', main:'Arturo + Liz', detail:'Lugares · Sabores · Experiencias', inputs:['nombres','descripcion'], motion:'deslizar'},
  {id:'cierre', title:'La conversación continúa', icon:null, eyebrow:'MÁS HISTORIAS POR VIVIR', main:'¿Qué lugar descubrimos después?', detail:'[Cuenta confirmada, si se usa]', inputs:['mensaje','cuenta_opcional'], motion:'aparecer'}
];
const logoBytes = fs.readFileSync(path.join(root,'marca/assets/logos/piezas/logo-horizontal-transparente.png'));
const logoData = 'data:image/png;base64,'+logoBytes.toString('base64');
const fontFile = path.join(root,'marca/assets/fuentes/PlusJakartaSans[wght].ttf');
const fontData = fs.readFileSync(fontFile).toString('base64');
const editorialFile = path.join(root,'marca/assets/fuentes/CormorantGaramond[wght].ttf');
const editorialData = fs.readFileSync(editorialFile).toString('base64');
function component(f) {
  const dark = f.id==='precio';
  const foreground = dark ? color.arena : color.cafe_oscuro;
  const background = dark ? color.verde_petroleo : color.arena;
  const icon = f.icon ? `<g id="icono" transform="translate(44 82) scale(1.9)" style="color:${dark?color.arena:color.verde_petroleo}">${line(icons.find(x=>x[0]===f.icon)[2])}</g>` : '';
  const x = f.icon ? 132 : 52;
  const accent = f.id === 'opinion' ? color.terracota : color.turquesa;
  const editorial = f.id==='presentacion';
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="1200" height="240" role="img" aria-label="${escape(f.title)} · mockup BORRADOR">
  <title>${escape(f.title)} · mockup tipográfico, sin experiencia real</title>
  <metadata>Fuentes OFL: marca/assets/fuentes/plusjakartasans-OFL.txt y cormorantgaramond-OFL.txt</metadata>
  <style>@font-face{font-family:'Plus Jakarta Sans';src:url(data:font/ttf;base64,${fontData}) format('truetype');font-weight:200 800}${editorial?`@font-face{font-family:'Cormorant Garamond';src:url(data:font/ttf;base64,${editorialData}) format('truetype');font-weight:300 700}`:''}</style>
  <g id="fondo"><rect x="8" y="8" width="1184" height="224" rx="4" fill="${background}"/><rect x="8.5" y="8.5" width="1183" height="223" rx="4" fill="none" stroke="${foreground}" stroke-opacity=".12"/></g>
  <g id="acento"><rect x="1120" y="33" width="32" height="3" fill="${accent}"/></g>${icon}
  <g fill="${foreground}" font-family="Plus Jakarta Sans, sans-serif">
  <text id="etiqueta" x="${x}" y="57" font-size="28" font-weight="500" letter-spacing="2">${escape(f.eyebrow)}</text>
  <text id="titulo" ${editorial?'data-font="editorial" font-family="Cormorant Garamond, serif"':''} x="${x}" y="133" font-size="${editorial?80:dark?72:f.id==='cierre'?51:60}" font-weight="${editorial?500:650}">${escape(f.main)}</text>
  ${dark?`<text id="moneda" x="615" y="133" font-size="36" font-weight="500">MXN</text>`:''}
  <text id="detalle" x="${x}" y="188" font-size="36" font-weight="500">${escape(f.detail)}</text>
  </g><g id="firma"><rect x="${x}" y="203" width="32" height="4" fill="${color.terracota}"/><rect x="${x+36}" y="203" width="32" height="4" fill="${color.turquesa}"/></g></svg>`;
}
for(const f of fields) write(path.join(source,'componentes',f.id+'.svg'),component(f));
// Los SVG autónomos conservan fuentes y capas. El tablero comparte las fuentes
// de página y antepone el componente a cada ID para evitar duplicados en el DOM.
function componentPreview(f) {
  return component(f).replace(/<style>[\s\S]*?<\/style>/, '')
    .replace(/id="([^"]+)"/g, (_, id) => `id="preview-${f.id}-${id}"`);
}
const presets = [
  {id:'aparecer',entry_ms:180,exit_ms:140,entry:[{t_ms:0,opacity:0},{t_ms:180,opacity:1}],exit:[{t_ms:0,opacity:1},{t_ms:140,opacity:0}]},
  {id:'deslizar',entry_ms:240,exit_ms:160,entry:[{t_ms:0,opacity:0,offset_x_px:-24},{t_ms:240,opacity:1,offset_x_px:0}],exit:[{t_ms:0,opacity:1,offset_x_px:0},{t_ms:160,opacity:0,offset_x_px:-12}]},
  {id:'enfatizar',entry_ms:220,exit_ms:140,entry:[{t_ms:0,opacity:0,scale:0.96},{t_ms:220,opacity:1,scale:1}],exit:[{t_ms:0,opacity:1},{t_ms:140,opacity:0}]},
  {id:'trazar',entry_ms:360,exit_ms:140,requires:'stroke_reveal',fallback:'aparecer',entry:[{t_ms:0,stroke_progress:0},{t_ms:360,stroke_progress:1}],exit:[{t_ms:0,opacity:1},{t_ms:140,opacity:0}]}
];
json(path.join(source,'motion.json'),{version:'0.1',status:'borrador',date,implementation:'especificacion_sin_render',units:{time:'milliseconds',offset:'local pixels at 1920x1080',scale:'multiplier',opacity:'0..1'},hold:'reading_hold_ms from episode; duration=entry_ms+reading_hold_ms+exit_ms; exit.t_ms relative to beginning of exit',easing_intent:{entry:'ease-out',exit:'ease-in'},editor_mapping:'pendiente_de_capacidades_reales',presets});

const css = `@font-face{font-family:Jakarta;src:url('../../assets/fuentes/PlusJakartaSans%5Bwght%5D.ttf')}@font-face{font-family:Editorial;src:url('../../assets/fuentes/CormorantGaramond%5Bwght%5D.ttf')}*{box-sizing:border-box}body{margin:0;background:#f4f1e9;color:${color.cafe_oscuro};font-family:Jakarta,sans-serif}main{max-width:1440px;margin:auto;padding:56px 64px}header{display:flex;justify-content:space-between;align-items:start}header img{width:220px}small,.eyebrow{font-size:12px;letter-spacing:2px;font-weight:700}.state{padding:9px 14px;border:1px solid #b9b5a6;border-radius:99px}h1{font-size:52px;line-height:1.1;letter-spacing:-2px;margin:30px 0 12px}h1 em{font-family:Editorial,serif;font-weight:500}p{line-height:1.6;max-width:850px}section{margin-top:42px}h2{font-size:25px;letter-spacing:-.6px;margin:0 0 8px}.sub{font-size:14px;color:#665d53;margin:0 0 20px}.icons{display:grid;grid-template-columns:repeat(8,1fr);gap:12px}.tile{background:#e9e5d8;border:1px solid #d6d1c2;border-radius:14px;min-height:124px;text-align:center;padding:20px 8px 12px}.tile svg{width:45px;height:45px;display:block;margin:0 auto 15px}.tile span{font-size:11px;font-weight:600}.components{display:grid;grid-template-columns:1fr 1fr;gap:20px}.card{background:#fffdf8;border:1px solid #dbd6c8;border-radius:16px;padding:20px}.card h3{font-size:15px;margin:0 0 13px}.card>svg{display:block;width:100%;height:auto;font-family:Jakarta}.card>svg text{font-family:Jakarta,sans-serif}.caption{font-size:12px;line-height:1.5;margin:12px 0 0;color:#665d53}.strip{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.rule{border-top:3px solid ${color.turquesa};padding:14px 12px;background:#e9e5d8;border-radius:0 0 12px 12px}.rule strong{font-size:15px}.rule p{font-size:12px;line-height:1.6;margin:8px 0 0}.footer{margin-top:32px;font-size:12px;color:#665d53;border-top:1px solid #d6d1c2;padding-top:18px}@media(max-width:850px){main{padding:28px}h1{font-size:38px}.icons{grid-template-columns:repeat(4,1fr)}.components,.strip{grid-template-columns:1fr 1fr}header img{width:150px}}@media(max-width:520px){.components,.strip{grid-template-columns:1fr}.icons{grid-template-columns:repeat(2,1fr)}}`;
const html = `<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>AL DESTINO · Mesa de edición v0.1 · BORRADOR</title><style>${css}.card>svg text[data-font="editorial"]{font-family:Editorial,serif}.system-nav{display:flex;flex-wrap:wrap;gap:12px 24px;margin-top:26px;font-size:13px}.system-nav a,.caption a{color:inherit;text-underline-offset:4px}.shared-motion{display:block;width:100%;height:210px;object-fit:contain;background:#E3DEC9}a:focus-visible{outline:2px solid #244B49;outline-offset:4px}</style><main>
<header><img alt="Logo original de AL DESTINO" src="${logoData}"><span class="state"><small>BORRADOR · V0.1</small></span></header>
<nav aria-label="Guías de AL DESTINO" class="system-nav"><a href="../../design-system.html#video">← Design system</a><a href="../../design-system.html#animacion">Logos y animaciones</a><a href="../../recursos.json">Índice de recursos</a><a href="../../exportaciones/index.html">Descargas de marca</a></nav>
<h1>La historia es de ustedes.<br><em>Los gráficos la acompañan.</em></h1>
<p>Dirección elegida por Arturo: profesional y elegante, con el video de El Mundo en Pareja como referencia de edición. Propuesta visual: jerarquía clara, espacio y acentos medidos. Conservamos el logo, las fuentes y la paleta actuales.</p>
<section id="marca-compartida"><h2>La misma marca, aplicada al video</h2><p class="sub">Estas son las animaciones existentes. Se reutilizan desde sus fuentes originales; las muestras de rótulos de abajo amplían el sistema.</p><div class="components"><article class="card"><h3>Firma horizontal · 3.2 s / 30 fps</h3><img class="shared-motion" src="../../motion/logo-al-destino/renders/AL-DESTINO-logo-animado.png" width="1920" height="1080" alt="Animación horizontal existente de AL DESTINO"><p class="caption">Sin audio · APNG transparente · uso como firma o cierre cuando aporte.<br><a href="../../motion/logo-al-destino/renders/AL-DESTINO-logo-animado.png" download>APNG horizontal</a> · <a href="../../exportaciones/AL-DESTINO-logo-animacion-PNG.zip" download>Secuencia PNG</a></p></article><article class="card"><h3>Firma circular · 3.2 s / 30 fps</h3><img class="shared-motion" src="../../motion/logo-circular/renders/AL-DESTINO-logo-circular-animado.png" width="1080" height="1080" alt="Animación circular existente de AL DESTINO"><p class="caption">Círculo arena y exterior transparente · sin audio.<br><a href="../../motion/logo-circular/renders/AL-DESTINO-logo-circular-animado.png" download>APNG circular</a> · <a href="../../exportaciones/AL-DESTINO-logo-circular-animacion-PNG.zip" download>Secuencia PNG</a></p></article></div><p class="caption">La animación del logo tiene renders. Los cuatro movimientos de rótulos siguen como especificaciones. La compatibilidad de ambos tipos de recurso en Clipo se prueba al aplicarlos.</p></section>
<section><h2>01 / Un vocabulario visual propio</h2><p class="sub">16 iconos de línea · fuente SVG · PNG transparente · cámara de redes genérica, sin logotipo de plataforma</p><div class="icons">${icons.map(([id,title,body])=>`<div class="tile">${svg(id,title,body)}<span>${escape(title)}</span></div>`).join('')}</div></section>
<section><h2>02 / Información que sí ayuda</h2><p class="sub">MOCKUPS TIPOGRÁFICOS · Campos entre corchetes pendientes · No son datos, opiniones ni visitas reales.</p><div class="components">${fields.map(f=>`<article class="card"><h3>${escape(f.title)}</h3>${componentPreview(f)}<p class="caption">${escape(f.inputs.join(' · '))}<br>Movimiento propuesto: ${f.motion} · texto/fondo/icono por separado al aplicar en el editor.<br><a href="componentes/${f.id}.svg" download>Fuente SVG</a> · <a href="../../exportaciones/video-v01/componentes/${f.id}.png" download>PNG de referencia</a></p></article>`).join('')}</div></section>
<section><h2>03 / Movimiento con una razón</h2><p class="sub">Especificaciones iniciales, sin animación ni render en este tablero. La pausa de lectura se suma a entrada y salida.</p><div class="strip"><div class="rule"><strong>Aparecer · 180 ms</strong><p>Opacidad 0 → 1<br>Dato secundario, sin distracción.</p></div><div class="rule"><strong>Deslizar · 240 ms</strong><p>−24 → 0 px + opacidad<br>Ubicación y presentación.</p></div><div class="rule"><strong>Enfatizar · 220 ms</strong><p>Escala 96 → 100 %<br>Un precio o una opinión puntual.</p></div><div class="rule"><strong>Trazar · 360 ms</strong><p>Revelar 0 → 100 % de la flecha<br>Alternativa si falta soporte: aparecer.</p></div></div></section>
<section><h2>04 / Una historia antes que una receta</h2><div class="strip"><div class="rule"><strong>Un momento que abre</strong><p>Acción o pregunta real. Sin una intro de logo obligatoria.</p></div><div class="rule"><strong>Ustedes en el lugar</strong><p>Contexto, detalle y conversación. Mantener la voz de ambos.</p></div><div class="rule"><strong>Un dato con contexto</strong><p>Precio, condición o consejo comprobado. Opiniones con autor.</p></div><div class="rule"><strong>Algo que nos llevamos</strong><p>Resolver la pregunta o reconocer qué quedó pendiente.</p></div></div></section>
<p class="footer">Fuentes: marca v0.6 y encargo de Arturo · ${date} · SVG editables en componentes/ e iconos/ · Catálogo: catalogo.json · Presets: motion.json · MCP de Clipo a cargo de Arturo. Esta mesa no demuestra integración.</p></main></html>`;
write(path.join(source,'index.html'),html);

async function exportAll(){
  const {chromium} = require('playwright');
  const browser = await chromium.launch({headless:true,...(process.env.AL_DESTINO_BROWSER?{executablePath:process.env.AL_DESTINO_BROWSER}:{})});
  try{
    const page = await browser.newPage({viewport:{width:1440,height:1100},deviceScaleFactor:1});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto(pathToFileURL(path.join(source,'index.html')).href);
    await page.evaluate(()=>document.fonts.ready);
    const loaded = await page.evaluate(()=>document.fonts.check('500 20px Jakarta')&&document.fonts.check('500 20px Editorial'));
    if(!loaded)throw Error('Las fuentes de marca no están listas.');
    await page.screenshot({path:path.join(output,'mesa-de-revision.png'),fullPage:true});
    // El SVG se coloca inline para que use las fuentes locales ya cargadas por el tablero.
    await page.evaluate(()=>{document.body.innerHTML='<div id="export" style="width:max-content;line-height:0"></div>';document.body.style.background='transparent';document.body.style.margin='0';});
    const iconItems=[];
    for(const [id,title,body] of icons){
      const png={};
      for(const variant of ['cafe_oscuro','arena','turquesa']){
        const file=`iconos/${variant}/${id}.png`;
        const markup=svg(id,title,body).replace(`color:${color.cafe_oscuro}`,`color:${color[variant]}`);
        await page.locator('#export').evaluate((el,s)=>el.innerHTML=s,markup);
        fs.mkdirSync(path.dirname(path.join(output,file)),{recursive:true});
        await page.locator('#export svg').screenshot({path:path.join(output,file),omitBackground:true});
        png[variant]={file:'../../exportaciones/video-v01/'+file,sha256:hash(path.join(output,file)),width:256,height:256};
      }
      iconItems.push({id,title,status:'borrador',source:'iconos/'+id+'.svg',source_sha256:hash(path.join(source,'iconos',id+'.svg')),png});
    }
    const componentItems=[];
    for(const f of fields){
      await page.locator('#export').evaluate((el,s)=>el.innerHTML=s,component(f));
      await page.evaluate(()=>document.fonts.ready);
      // En fuentes autónomas SVG la familia es Plus Jakarta Sans; el tablero la registra con alias Jakarta.
      await page.locator('#export svg text').evaluateAll(els=>els.forEach(el=>el.style.fontFamily=el.getAttribute('data-font')==='editorial'?'Editorial':'Jakarta'));
      const file='componentes/'+f.id+'.png';fs.mkdirSync(path.dirname(path.join(output,file)),{recursive:true});
      await page.locator('#export svg').screenshot({path:path.join(output,file),omitBackground:true});
      componentItems.push({id:f.id,title:f.title,status:'borrador',source:'componentes/'+f.id+'.svg',source_sha256:hash(path.join(source,'componentes',f.id+'.svg')),preview:{file:'../../exportaciones/video-v01/'+file,sha256:hash(path.join(output,file)),width:1200,height:240},fields:f.inputs,layers:['fondo','acento',...(f.icon?['icono']:[]),'etiqueta','titulo',...(f.id==='precio'?['moneda']:[]),'detalle','firma'],motion_preset:f.motion,editability:'SVG fuente por capas; PNG aplanado; aplicación nativa Clipo pendiente'});
    }
    if(errors.length)throw Error(errors.join('\n'));
    json(path.join(source,'catalogo.json'),{brand:'AL DESTINO',version:'0.1',status:'borrador',created_at:date,brand_version:tokens.version,color_values:color,source:'Dibujos geométricos y muestras tipográficas creados en este proyecto; no derivados del referente audiovisual',reference_scope:'mockups_sin_material_real',motion:'motion.json',font:{file:'../../assets/fuentes/PlusJakartaSans[wght].ttf',sha256:hash(fontFile),license:'../../assets/fuentes/plusjakartasans-OFL.txt',svg_embedding:true},icon_style:{viewBox:[0,0,32,32],stroke:1.8,linecap:'round',linejoin:'round'},icons:iconItems,components:componentItems,board:{file:'../../exportaciones/video-v01/mesa-de-revision.png',sha256:hash(path.join(output,'mesa-de-revision.png'))}});
    console.log(`${iconItems.length} iconos SVG; ${iconItems.length*3} PNG; ${componentItems.length} componentes SVG/PNG; mesa de revisión. BORRADOR.`);
  }finally{await browser.close();}
}
fs.mkdirSync(output,{recursive:true});
exportAll().catch(e=>{console.error(e.message);process.exitCode=1;});
