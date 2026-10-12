/* AL DESTINO · render de SVG; requiere playwright disponible en Node. */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
(async()=>{
 const root=path.resolve(__dirname,'../..');
 const catalog=JSON.parse(fs.readFileSync(path.join(root,'marca/archivo/v03-aplicaciones/catalogo.json')));
 const browser=await chromium.launch({headless:true, ...(process.env.AL_DESTINO_BROWSER ? {executablePath:process.env.AL_DESTINO_BROWSER} : {})});
 for(const t of catalog.items){
  const w=t.id.startsWith('YT0')?1280:t.width;
  const h=Math.round(w*t.height/t.width);
  const page=await browser.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(root,'marca',t.svg)).href);
  await page.evaluate(async({w,h})=>{const s=document.documentElement;s.setAttribute('width',w);s.setAttribute('height',h);await document.fonts.ready;},{w,h});
  await page.screenshot({path:path.join(root,'marca',t.preview),omitBackground:true});
  await page.close();
  console.log(t.id,w,h);
 }
 for(const name of ['logo-horizontal-borrador','monograma-borrador','logo-horizontal-claro-borrador','logo-horizontal-oscuro-borrador']){
  const svgPath=path.join(root,'marca/assets',name+'.svg');
  const content=fs.readFileSync(svgPath,'utf8');
  const match=content.match(/width="(\d+)" height="(\d+)"/);
  const w=Number(match[1]),h=Number(match[2]);
  const p=await browser.newPage({viewport:{width:w,height:h}});
  await p.goto(pathToFileURL(svgPath).href);
  await p.screenshot({path:path.join(root,'marca/assets',name+'.png'),omitBackground:true});
  await p.close();
 }
 const page=await browser.newPage({viewport:{width:1440,height:1100}});
 await page.goto(pathToFileURL(path.join(root,'marca/index.html')).href);
 await page.evaluate(()=>document.fonts.ready);
 await page.screenshot({path:path.join(root,'marca/previews/estudio-desktop.png')});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const original=await page.locator('.canvas text').first().textContent();
 page.once('dialog',d=>d.accept('Prueba editorial'));
 await page.locator('.canvas text').first().click();
 if(await page.locator('.canvas text').first().textContent()!=='Prueba editorial')throw Error('Edición no aplicada');
 await page.evaluate(v=>document.querySelector('.canvas text').textContent=v,original);
 await page.locator('#guides').check();
 if(await page.locator('.canvas .guide').first().evaluate(g=>getComputedStyle(g).display)==='none')throw Error('Guías no visibles');
 await page.locator('#guides').uncheck();
 const downloadPromise=page.waitForEvent('download');await page.locator('.save').first().click();
 const download=await downloadPromise;
 const tmp=await download.path();const out=fs.readFileSync(tmp,'utf8');
 if(!out.includes('width="3840"')||out.includes('id="guias"'))throw Error('Exportación no conserva tamaño o guías');
 console.log('Edición de texto, guías y descarga SVG: OK');
 await page.setViewportSize({width:390,height:844});
 await page.evaluate(()=>scrollTo(0,0));
 await page.screenshot({path:path.join(root,'marca/previews/estudio-mobile.png')});
 if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Overflow móvil');
 if(errors.length)throw Error(errors.join('\n'));
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
