/* AL DESTINO · revisión v0.3 · requiere Playwright y Chromium. */
const { chromium }=require('playwright');
const fs=require('fs'),path=require('path'),{pathToFileURL}=require('url');
(async()=>{
 const root=path.resolve(__dirname,'../..'),mark=path.join(root,'marca'),v=path.join(mark,'archivo/v03-aplicaciones');
 const cat=JSON.parse(fs.readFileSync(path.join(mark,'archivo/v03-aplicaciones/catalogo.json')));
 const browser=await chromium.launch({headless:true,...(process.env.AL_DESTINO_BROWSER?{executablePath:process.env.AL_DESTINO_BROWSER}:{})});
 for(const t of cat.items){
  const w=t.id.startsWith('YT0')?1280:t.width,h=Math.round(w*t.height/t.width);
  const p=await browser.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
  await p.goto(pathToFileURL(path.join(mark,t.svg)).href);
  await p.evaluate(async({w,h})=>{document.documentElement.setAttribute('width',w);document.documentElement.setAttribute('height',h);await document.fonts.ready;},{w,h});
  await p.screenshot({path:path.join(mark,t.preview),omitBackground:true});await p.close();console.log(t.id,w,h);
 }
 const p=await browser.newPage({viewport:{width:1440,height:1100},acceptDownloads:true});
 const errors=[];p.on('pageerror',e=>errors.push(e.message));
 await p.goto(pathToFileURL(path.join(v,'index.html')).href);await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:path.join(v,'previews/estudio-desktop.png')});
 const title=p.locator('.canvas text[data-editable]').first(),original=await title.textContent();await title.click();
 await p.locator('#textValue').fill('Prueba de edición');await p.locator('#applyText').click();
 if(await title.textContent()!=='Prueba de edición')throw Error('Texto no editable');
 await title.click();await p.locator('#textValue').fill(original);await p.locator('#applyText').click();
 const image=p.locator('article').first().locator('image[data-photo]'),href=await image.getAttribute('href');
 await p.locator('article').first().locator('.photo-input').setInputFiles(path.join(v,'assets/lifestyle-mockup.png'));
 await p.waitForFunction(old=>document.querySelector('image[data-photo]').getAttribute('href')!==old,href);
 await image.evaluate((img,old)=>img.setAttribute('href',old),href);
 await p.locator('#guides').check();const guide=p.locator('.guide').first();
 if(await guide.evaluate(g=>getComputedStyle(g).display)==='none')throw Error('Guías no visibles');
 await p.locator('#guides').uncheck();
 let wait=p.waitForEvent('download');await p.locator('.save').first().click();let d=await wait;
 const svg=fs.readFileSync(await d.path(),'utf8');if(!svg.includes('width="3840"')||svg.includes('id="guias"'))throw Error('Exportación SVG incorrecta');
 wait=p.waitForEvent('download');await p.locator('.png').first().click();d=await wait;
 const png=fs.readFileSync(await d.path());if(png.readUInt32BE(16)!==1280||png.readUInt32BE(20)!==720)throw Error('Exportación PNG incorrecta');
 await p.setViewportSize({width:390,height:844});await p.evaluate(()=>scrollTo(0,0));
 await p.screenshot({path:path.join(v,'previews/estudio-mobile.png')});
 if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Overflow móvil');
 if(errors.length)throw Error(errors.join('\n'));
 console.log('Edición de texto y foto, guías, exportaciones SVG/PNG y móvil: OK');
 // Review board composed from the exported templates, without changing source photos or logos.
 const board=await browser.newPage({viewport:{width:1600,height:2040}});
 const thumbs=cat.items.slice(0,3).map(t=>'<figure><img src="'+pathToFileURL(path.join(mark,t.preview)).href+'"><figcaption>'+t.id+' · MOCKUP</figcaption></figure>').join('');
 const html='<html><head><style>body{margin:0;background:#fffcf7;color:#2b211d;font-family:Arial;padding:55px 64px}h1{font-family:Georgia;font-weight:normal;font-size:60px;margin:0 0 18px}p{font-size:19px;margin:0 0 38px}figure{margin:0 0 26px}img{width:100%;display:block}figcaption{font-size:14px;letter-spacing:2px;margin:12px 0}.thumbs{display:grid;grid-template-columns:1fr 1fr;gap:26px}.thumbs figure:first-child{grid-column:1/-1}.banner{margin-top:24px}.banner img{height:500px;object-fit:cover}</style></head><body><h1>AL DESTINO</h1><p>Logo original. Nueva aplicación. · v0.3 · BORRADOR</p><section class="thumbs">'+thumbs+'</section><figure class="banner"><img src="'+pathToFileURL(path.join(v,'previews/YT-banner.png')).href+'"><figcaption>BANNER · LOGO ORIGINAL INTACTO</figcaption></figure><p>Escenas generadas para revisar diseño; sustituir por fotografías propias.</p></body></html>';
 await board.goto(pathToFileURL(path.join(v,'index.html')).href);await board.setContent(html);await board.screenshot({path:path.join(v,'previews/tablero-v03.png'),fullPage:true});
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
