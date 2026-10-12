/* Extrae píxeles visibles del logo original; no dibuja letras ni crea partes ocultas. */
const{chromium}=require('playwright'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
(async()=>{
 const root=path.resolve(__dirname,'..'),out=path.join(root,'marca/assets/logos/piezas');fs.mkdirSync(out,{recursive:true});
 const src=fs.readFileSync(path.join(root,'marca/assets/logos/logo-original-referencia.png'));const browser=await chromium.launch({headless:true,...(process.env.AL_DESTINO_BROWSER?{executablePath:process.env.AL_DESTINO_BROWSER}:{})}),p=await browser.newPage();
 const result=await p.evaluate(async source=>{
  const im=new Image();im.src=source;await im.decode();const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const ctx=c.getContext('2d');ctx.drawImage(im,0,0);const pixels=ctx.getImageData(0,0,c.width,c.height),parts={};
  const add=(name,x,y,rgba)=>{(parts[name]??=[]).push({x,y,rgba})};
  for(let y=185;y<525;y++)for(let x=240;x<1920;x++){
   const i=(y*c.width+x)*4,[r,g,b]=pixels.data.slice(i,i+3);if(Math.min(r,g,b)>238)continue;
   let key=null;if(x<880){if(x>=600&&x<=790&&y>=285&&y<=430&&r-g>20&&r-b>25)key='sol';else if(y>=389&&y<=457&&g-r>12&&b-r>12)key='ola';else if(x<=742&&Math.max(r,g,b)<220&&Math.max(r,g,b)-Math.min(r,g,b)<30){const limit=y<240?500:y<480?532:542+y-480;key=x<limit?'letra-a':'letra-l'}}
   else if(x>=895&&x<=914)key='divisor';else if(x>=955&&y>=250&&y<398)key='nombre';else if(x>=955&&y>=425&&y<465)key='tagline';
   if(key){let rgba=[r,g,b,255];if(!['sol','ola'].includes(key)&&Math.max(r,g,b)>80){const alpha=Math.min(1,Math.max(0,(254-r)/237));rgba=[17,17,14,Math.round(alpha*255)]}add(key,x,y,rgba);}
  }
  // The wordmark is also split into its nine visible glyphs for ordered entrances.
  const cols=[...new Set(parts.nombre.map(p=>p.x))].sort((a,b)=>a-b),runs=[];let run=[];
  for(const x of cols){if(run.length&&x-run.at(-1)>2){runs.push(run);run=[]}run.push(x)}if(run.length)runs.push(run);
  if(runs.length!==9)throw Error('No se identificaron nueve letras del nombre: '+runs.length);
  const names=['a','l','d','e','s','t','i','n','o'];runs.forEach((run,i)=>parts[`nombre-${String(i+1).padStart(2,'0')}-${names[i]}`]=parts.nombre.filter(p=>p.x>=run[0]&&p.x<=run.at(-1)));
  const output=[];for(const[name,list]of Object.entries(parts)){
   const xs=list.map(p=>p.x),ys=list.map(p=>p.y),x=Math.min(...xs)-2,y=Math.min(...ys)-2,w=Math.max(...xs)-x+3,h=Math.max(...ys)-y+3;
   const canvas=document.createElement('canvas');canvas.width=w;canvas.height=h;const context=canvas.getContext('2d'),data=context.createImageData(w,h);
   for(const p of list)data.data.set(p.rgba,((p.y-y)*w+p.x-x)*4);context.putImageData(data,0,0);output.push({id:name,x,y,width:w,height:h,png:canvas.toDataURL('image/png')});
  }
  // Composite for fidelity inspection and the standalone transparent lockup.
  const combined=document.createElement('canvas');combined.width=1700;combined.height=370;const cc=combined.getContext('2d'),image=cc.createImageData(1700,370);
  for(const name of ['letra-a','letra-l','sol','ola','divisor','nombre','tagline'])for(const p of parts[name])image.data.set(p.rgba,((p.y-170)*1700+p.x-230)*4);
  cc.putImageData(image,0,0);return{output,combined:combined.toDataURL('image/png')};
 },'data:image/png;base64,'+src.toString('base64'));
 const items=result.output.map(({png,...item})=>{const file=item.id+'.png',bytes=Buffer.from(png.split(',')[1],'base64');fs.writeFileSync(path.join(out,file),bytes);return{...item,file,sha256:crypto.createHash('sha256').update(bytes).digest('hex')}});
 fs.writeFileSync(path.join(out,'logo-horizontal-transparente.png'),Buffer.from(result.combined.split(',')[1],'base64'));
 fs.writeFileSync(path.join(out,'catalogo.json'),JSON.stringify({status:'borrador',source:'../logo-original-referencia.png',source_sha256:crypto.createHash('sha256').update(src).digest('hex'),coordinate_space_px:[2172,724],crop_origin_px:[230,170],method:'Extracción por regiones y color de píxeles visibles; fondo claro descartado y matte claro compensado en bordes de tinta, sin redibujar ni completar zonas ocultas. Separación A/L propuesta en su pie compartido; unión final recompone los píxeles conservados.',items},null,2)+'\n');
 await browser.close();console.log(items.length+' piezas PNG con transparencia extraídas del original.');
})().catch(e=>{console.error(e);process.exit(1)});
