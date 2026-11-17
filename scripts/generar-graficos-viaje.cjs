/* Recursos originales de AL DESTINO. SVG editables + PNG transparentes.
   Sin fotografías, logos nuevos ni material gráfico de terceros. */
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
const root=path.resolve(__dirname,'..');
const source=path.join(root,'marca/video/v02');
const output=path.join(root,'marca/exportaciones/video-v02');
const episode=path.join(root,'produccion/episodios/ad-0001/proyecto-local/graficos-v02');
for(const p of [source,output,episode])fs.mkdirSync(p,{recursive:true});
const tokens=JSON.parse(fs.readFileSync(path.join(root,'marca/tokens/brand_tokens.json'),'utf8'));
const c=Object.fromEntries(Object.entries(tokens.color).map(([k,v])=>[k,v.$value]));
const font=fs.readFileSync(path.join(root,'marca/assets/fuentes/PlusJakartaSans[wght].ttf')).toString('base64');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const write=(p,s)=>fs.writeFileSync(p,s+'\n');
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;');
const defs=`<defs><filter id="sombra" x="-25%" y="-25%" width="160%" height="160%"><feDropShadow dx="0" dy="7" stdDeviation="7" flood-color="${c.cafe_oscuro}" flood-opacity=".18"/></filter><linearGradient id="papel" x2=".7" y2="1"><stop stop-color="#fffdf5"/><stop offset="1" stop-color="${c.arena}"/></linearGradient><linearGradient id="pan" x2=".5" y2="1"><stop stop-color="#e8b568"/><stop offset=".55" stop-color="#c9893d"/><stop offset="1" stop-color="#a5652c"/></linearGradient></defs>`;
// Formas e ilustraciones propias, con volumen por planos y una silueta recortada.
const shapes={
 ubicacion:`<path d="M40 78Q24 28 86 25L206 35Q255 38 249 94L242 202Q230 253 173 246L62 229Q16 213 27 155Z" fill="#fffdf5" filter="url(#sombra)"/><g transform="rotate(-9 135 140)"><path d="M49 82L103 64L164 81L221 64V207L164 223L103 205L49 221Z" fill="${c.arena}"/><path d="M49 82L103 64V205L49 221Z" fill="#c6ded3"/><path d="M103 64L164 81V223L103 205Z" fill="#eae4cd"/><path d="M164 81L221 64V207L164 223Z" fill="#adcfc2"/><path d="M59 176Q90 135 111 162T154 159T208 177" fill="none" stroke="${c.turquesa}" stroke-width="8" stroke-linecap="round"/><path d="M65 120Q99 104 124 135T192 107" fill="none" stroke="${c.cafe_oscuro}" stroke-opacity=".5" stroke-width="3" stroke-dasharray="3 8" stroke-linecap="round"/><path d="M163 92C129 92 119 125 141 150L163 178L185 150C207 125 197 92 163 92Z" fill="${c.terracota}"/><circle cx="163" cy="122" r="12" fill="#fff4db"/><path d="M153 100Q140 103 138 115" fill="none" stroke="#f2b39b" stroke-width="5" stroke-linecap="round"/></g><path d="M238 48v23m-11-12h23" stroke="${c.mostaza}" stroke-width="4" stroke-linecap="round"/>`,
 sabores:`<path d="M24 150Q13 118 48 99L78 36Q98 12 134 36L196 38Q235 28 251 60L257 184Q264 232 213 244L71 247Q25 247 22 202Z" fill="#fffdf5" filter="url(#sombra)"/><ellipse cx="129" cy="207" rx="96" ry="24" fill="${c.arena}"/><ellipse cx="126" cy="200" rx="91" ry="20" fill="#f8f3e6"/><g transform="rotate(-10 110 155)"><path d="M44 169Q46 122 73 118L159 111Q184 113 192 153Q199 180 168 190L70 198Q39 196 44 169Z" fill="url(#pan)"/><path d="M62 144Q91 155 87 188M98 126Q127 141 118 190M137 122Q163 142 152 188" fill="none" stroke="#f7d59d" stroke-width="12" stroke-linecap="round"/><path d="M57 158L179 148" stroke="#935624" stroke-opacity=".3" stroke-width="3"/><path d="M62 128Q111 109 166 118" fill="none" stroke="#e9bb7a" stroke-width="4"/></g><g transform="rotate(8 193 109)"><path d="M201 71H224Q250 71 247 99Q243 117 223 117" fill="none" stroke="${c.verde_petroleo}" stroke-width="12"/><path d="M156 64H224L218 137Q215 151 187 151T159 137Z" fill="${c.turquesa}"/><ellipse cx="190" cy="65" rx="34" ry="10" fill="#5daba5"/><ellipse cx="190" cy="66" rx="26" ry="6" fill="${c.cafe_oscuro}"/><path d="M170 80V128" stroke="#90c3b5" stroke-width="7" stroke-linecap="round"/><path d="M179 44Q168 30 182 20M201 44Q190 30 204 20" fill="none" stroke="${c.cafe_oscuro}" stroke-opacity=".45" stroke-width="3" stroke-linecap="round"/></g>`,
 consejo:`<path d="M48 42Q65 16 102 24L205 30Q245 34 248 79L245 217Q238 252 201 251L62 239Q23 232 28 190L30 83Z" fill="#fffdf5" filter="url(#sombra)"/><g transform="rotate(-8 138 138)"><path d="M57 58L205 52L216 219L69 232Z" fill="${c.terracota}"/><path d="M69 51L217 45L221 210L79 221Z" fill="url(#papel)"/><path d="M79 51L91 219" stroke="#b8a996" stroke-width="2"/><path d="M105 90L192 83M108 115L195 108M111 140L183 134M114 164L197 157" stroke="${c.cafe_oscuro}" stroke-opacity=".35" stroke-width="3" stroke-linecap="round"/><path d="M107 65L139 63" stroke="${c.turquesa}" stroke-width="6" stroke-linecap="round"/></g><g transform="translate(160 131) rotate(12)"><circle r="48" fill="${c.verde_petroleo}"/><circle r="38" fill="${c.arena}"/><path d="M0-30L9-6L0 27L-10 4Z" fill="${c.terracota}"/><path d="M0-30L9-6L0 0Z" fill="${c.cafe_oscuro}"/><circle r="5" fill="#fffdf5"/></g><path d="M45 72L29 63M239 43L253 30" stroke="${c.mostaza}" stroke-width="4" stroke-linecap="round"/>`
};
const svg=(body,w=280,h=280)=>`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">${defs}${body}</svg>`;
function label(icon,eyebrow,title){
 return `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320">${defs}<style>@font-face{font-family:Jakarta;src:url(data:font/ttf;base64,${font}) format('truetype');font-weight:200 800}</style><g transform="translate(10 16)">${shapes[icon]}</g><g filter="url(#sombra)"><path d="M298 59L1140 55L1155 90L1137 115L1155 148L1135 185L1144 225L295 232L303 201L290 170L305 130L291 94Z" fill="#fffdf5"/></g><path d="M322 226Q588 235 805 226" fill="none" stroke="${c.terracota}" stroke-width="5" stroke-linecap="round"/><text x="330" y="109" fill="${c.verde_petroleo}" font-family="Jakarta" font-size="25" font-weight="700" letter-spacing="4">${esc(eyebrow)}</text><text x="330" y="184" fill="${c.cafe_oscuro}" font-family="Jakarta" font-size="${title.length>23?48:64}" font-weight="700" letter-spacing="-2">${esc(title)}</text></svg>`;
}
const labels=[['patzcuaro','ubicacion','MICHOACÁN','Pátzcuaro'],['mesa','sabores','SABORES COMPARTIDOS','Una mesa para dos'],['domingo','consejo','NUESTRA EXPERIENCIA','Así lo vivimos un domingo']];
async function main(){
 const browser=await chromium.launch({headless:true,...(process.env.AL_DESTINO_BROWSER?{executablePath:process.env.AL_DESTINO_BROWSER}:{})});
 try{
  const page=await browser.newPage({viewport:{width:1440,height:1100}});
  await page.goto('about:blank');
  await page.setContent('<style>html,body{margin:0;background:transparent}#asset{line-height:0;width:max-content}</style><div id="asset"></div>');
  async function raster(markup,file){await page.locator('#asset').evaluate((el,s)=>el.innerHTML=s,markup);await page.evaluate(()=>document.fonts.ready);await page.locator('#asset svg').screenshot({path:file,omitBackground:true});}
  const items=[];
  for(const [id,body] of Object.entries(shapes)){
   const name=`${id}.svg`;write(path.join(source,name),svg(body));await raster(svg(body),path.join(output,id+'.png'));
   items.push({id,title:({ubicacion:'Mapa y ubicación',sabores:'Pan y café',consejo:'Cuaderno y brújula'})[id],source:name,png:`../../exportaciones/video-v02/${id}.png`,width:280,height:280,alpha:true,status:'borrador',source_sha256:hash(path.join(source,name)),png_sha256:hash(path.join(output,id+'.png'))});
  }
  const episodeItems=[];
  for(const [id,icon,eye,title] of labels){const markup=label(icon,eye,title);write(path.join(episode,id+'.svg'),markup);await raster(markup,path.join(episode,id+'.png'));episodeItems.push({id,title,png:id+'.png',source:id+'.svg',sha256:hash(path.join(episode,id+'.png')),width:1200,height:320,status:'borrador'});}
  const cards=items.map(i=>`<div class="card"><img src="${i.id}.png"><h2>${i.title}</h2><p>PNG transparente · ilustración independiente</p></div>`).join('');
  const html=`<!doctype html><html lang="es"><meta charset="utf-8"><title>AL DESTINO · Gráficos de viaje v02 · BORRADOR</title><style>@font-face{font-family:J;src:url('../../../marca/assets/fuentes/PlusJakartaSans%5Bwght%5D.ttf')}body{margin:0;padding:52px;background:#ece7db;color:${c.cafe_oscuro};font-family:J,Arial,sans-serif}h1{font-size:44px;margin:8px 0 18px;letter-spacing:-2px}small{font-weight:bold;letter-spacing:3px}p{line-height:1.6;max-width:900px}.grid{display:flex;gap:24px;margin:30px 0}.card{background:#faf8f0;padding:24px;width:29%;border-radius:20px}.card img{display:block;width:240px;margin:auto}.card h2{font-size:22px}.card p{font-size:13px}.note{padding:20px 0;border-top:1px solid #bfb5a1}a{color:inherit}</style><small>AL DESTINO / DIRECCIÓN DE VIAJE / BORRADOR</small><h1>Ilustraciones con carácter.<br>La imagen conserva el protagonismo.</h1><p>Propuesta original para reemplazar la barra genérica de los rótulos del piloto. Silueta recortada, volumen por planos, tipografía de marca y textura sugerida por los bordes. Recursos nuevos sin copiar gráficos, logo ni colores de Alan por el mundo.</p><div class="grid">${cards}</div><p class="note">Estos PNG son ilustraciones reutilizables. Las composiciones de Pátzcuaro y las pruebas sobre material propio se conservan con el episodio. No son aprobación del estilo ni animaciones ya verificadas en Clipo. <a href="../../design-system.html#video">Volver a la guía</a></p></html>`;
  write(path.join(output,'index.html'),html);await page.goto(pathToFileURL(path.join(output,'index.html')).href);await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(output,'mesa-de-revision.png'),fullPage:true});
  if(fs.existsSync(path.join(episode,'fondo-mesa.png'))){
   await page.setViewportSize({width:1920,height:1080});
   const bg=pathToFileURL(path.join(episode,'fondo-mesa.png')).href, graphic=pathToFileURL(path.join(episode,'mesa.png')).href;
   write(path.join(episode,'prueba-mesa.html'),`<!doctype html><meta charset="utf-8"><title>Prueba estática · BORRADOR</title><style>html,body{margin:0;width:1920px;height:1080px;overflow:hidden}body{background:url('${bg}') center/cover}.label{position:absolute;left:96px;bottom:76px;width:850px}.note{position:absolute;top:32px;left:40px;padding:12px 18px;background:#fffdf5;color:#302722;font:20px Arial;letter-spacing:2px}</style><img class="label" src="${graphic}"><div class="note">PROPUESTA GRÁFICA · BORRADOR · PRUEBA ESTÁTICA</div>`);
   await page.goto(pathToFileURL(path.join(episode,'prueba-mesa.html')).href);
   await page.screenshot({path:path.join(episode,'prueba-mesa.png')});
  }
  write(path.join(source,'catalogo.json'),JSON.stringify({brand:'AL DESTINO',version:'0.2',status:'borrador',created_at:'2026-11-16',brand_version:tokens.version,generator:'scripts/generar-graficos-viaje.cjs',source:'Ilustraciones SVG originales y tipografía de marca; sin fotos de lugares ni recursos de terceros.',items,board:'../../exportaciones/video-v02/mesa-de-revision.png'},null,2));
  write(path.join(episode,'catalogo.local.json'),JSON.stringify({episode_id:'ad-0001',status:'borrador',generator:'scripts/generar-graficos-viaje.cjs',items:episodeItems,clipo_status:'sin_importar_sin_animar'},null,2));
  console.log('3 ilustraciones SVG/PNG transparentes y 3 rótulos de Pátzcuaro. BORRADOR.');
 }finally{await browser.close();}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
