/* Prepara el recorte raster existente; no vuelve a generar imágenes con IA. */
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {pathToFileURL}=require('url');
const {chromium}=require('playwright');
const root=path.resolve(__dirname,'..');
const source=path.join(root,'marca/video/v03');
const output=path.join(root,'marca/exportaciones/video-v03');
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const write=(p,s)=>fs.writeFileSync(p,s+'\n');
async function main(){
 fs.mkdirSync(output,{recursive:true});
 const items=[];
 for(const [id,title,filename,usage] of [['pan-cafe-recortado','Pan y café sin placa','pan-cafe-master.png','Ilustración genérica; no producto ni vajilla exactos consumidos.'],['pan-almendrado-recortado','Pan almendrado sin placa','pan-almendrado-master.png','Ilustración generada a partir del pan visible en material propio; no fotografía exacta del producto.']]){
  const master=path.join(source,'fuentes',filename);
  if(!fs.existsSync(master))throw new Error('Falta el maestro generado: '+filename);
  const png=fs.readFileSync(master);
  if(!png.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10]))||![4,6].includes(png[25]))throw new Error('El maestro debe ser PNG con alfa.');
  const exported=path.join(output,id+'.png');fs.copyFileSync(master,exported);
  items.push({id,title,source:'fuentes/'+filename,png:'../../exportaciones/video-v03/'+id+'.png',width:png.readUInt32BE(16),height:png.readUInt32BE(20),alpha:true,status:'borrador',usage,source_sha256:hash(master),png_sha256:hash(exported)});
 }
 write(path.join(source,'catalogo.json'),JSON.stringify({brand:'AL DESTINO',version:'0.3',status:'borrador',created_at:'2026-11-16',generator:'scripts/preparar-graficos-sin-placa.cjs',provenance:'procedencia.json',direction:'Recorte aislado, sin tarjeta, papel, borde blanco ni texto integrado. Propuesta aún sin prueba en Clipo.',items},null,2));
 const html=`<!doctype html><html lang="es"><meta charset="utf-8"><title>AL DESTINO · Recortes sin placa · BORRADOR</title><style>@font-face{font-family:J;src:url('../../assets/fuentes/PlusJakartaSans%5Bwght%5D.ttf')}*{box-sizing:border-box}body{margin:0;padding:52px;background:#e9e6de;color:#302722;font-family:J,Arial,sans-serif}small{font-weight:700;letter-spacing:3px}h1{font-size:44px;letter-spacing:-2px;max-width:900px}p{line-height:1.6;max-width:950px}.grid{display:flex;gap:20px;margin:28px 0}.sample{width:33.33%;padding:22px;border-radius:12px}.sample img{width:100%;display:block}.sample h2{font-size:16px}.light{background:white}.dark{background:#162829;color:#fff}.check{background:repeating-conic-gradient(#ddd 0% 25%,#fff 0% 50%) 0 0/24px 24px}a{color:inherit}</style><small>AL DESTINO / PNG RECORTADO / BORRADOR</small><h1>El elemento sobre la imagen.<br>Sin una tarjeta detrás.</h1><p>Propuesta de ilustración genérica para un momento de sabores: pan y taza de café. No es fotografía de una visita, producto consumido ni vajilla de un establecimiento. Recurso generado con image_gen y conservado con su procedencia.</p><div class="grid"><section class="sample light"><h2>Sobre claro</h2><img src="pan-cafe-recortado.png" alt="Pan y café recortados"></section><section class="sample dark"><h2>Sobre oscuro</h2><img src="pan-cafe-recortado.png" alt="El mismo PNG sobre oscuro"></section><section class="sample check"><h2>Transparencia real</h2><img src="pan-cafe-recortado.png" alt="El mismo PNG sobre cuadrícula"></section></div><p>La muestra sólo comprueba el recorte estático. Escala, posición y oportunidad se eligen sobre la toma, sin ocultar manos, producto ni reacción. Importación y animación en Clipo pendientes. Los diseños de papel de v02 se conservan como antecedente descartado para esta dirección.</p><a href="../../design-system.html#video">Volver al design system →</a></html>`;
 const secondRow='<h2>Pan almendrado · ilustración a partir del material propio</h2><div class="grid">'+['light','dark','check'].map(cls=>`<section class="sample ${cls}"><img src="pan-almendrado-recortado.png" alt="Ilustración del pan almendrado sin placa"></section>`).join('')+'</div>';
 write(path.join(output,'index.html'),html.replace('<p>La muestra sólo',secondRow+'<p>La muestra sólo'));
 const browser=await chromium.launch({headless:true,...(process.env.AL_DESTINO_BROWSER?{executablePath:process.env.AL_DESTINO_BROWSER}:{})});
 try{const page=await browser.newPage({viewport:{width:1440,height:1000}});await page.goto(pathToFileURL(path.join(output,'index.html')).href);await page.evaluate(()=>document.fonts.ready);await page.screenshot({path:path.join(output,'mesa-de-revision.png'),fullPage:true});}finally{await browser.close();}
 console.log('PNG v03, fuente, catálogo y prueba de transparencia preparados. BORRADOR; sin aplicar en Clipo.');
}
main().catch(e=>{console.error(e);process.exitCode=1;});
