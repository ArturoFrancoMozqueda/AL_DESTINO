/* Variante de movimiento: reutiliza las piezas raster originales de AL DESTINO. */
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root=path.resolve(__dirname,'..'),base=path.join(root,'marca/motion/logo-al-destino/premium');
const piecesDir=path.join(root,'marca/assets/logos/piezas');
const catalog=JSON.parse(fs.readFileSync(path.join(piecesDir,'catalogo.json'),'utf8'));
const pieces=catalog.items.filter(p=>['letra-a','letra-l','sol','ola','divisor','tagline'].includes(p.id)||p.id.startsWith('nombre-'));
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const write=(p,s)=>fs.writeFileSync(p,s+'\n');
fs.mkdirSync(path.join(base,'assets/piezas'),{recursive:true});
for(const p of pieces){const source=path.join(piecesDir,p.file);if(hash(source)!==p.sha256)throw Error('Pieza distinta del catálogo: '+p.id);fs.copyFileSync(source,path.join(base,'assets/piezas',p.file));}
fs.copyFileSync(path.join(root,'marca/motion/logo-al-destino/assets/gsap.min.js'),path.join(base,'assets/gsap.min.js'));
function images(prefix){return pieces.map(p=>{const pos=`left:${((p.x-230)*.8).toFixed(2)}px;top:${((p.y-170)*.8).toFixed(2)}px;width:${(p.width*.8).toFixed(2)}px;height:${(p.height*.8).toFixed(2)}px`;return prefix==='core'?`<img id="${prefix}-${p.id}" class="piece part-${p.id}" src="assets/piezas/${p.file}" alt="${p.id}" style="${pos}">`:`<div id="${prefix}-${p.id}" class="piece part-${p.id}" style="${pos};background-image:url('assets/piezas/${p.file}');background-size:100% 100%"></div>`;}).join('\n');}
const html=`<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=1920,height=1080"><title>AL DESTINO · Firma por piezas · BORRADOR</title><script src="assets/gsap.min.js"></script><style>*{box-sizing:border-box;margin:0;padding:0}html,body{width:1920px;height:1080px;overflow:hidden;background:transparent}#al-destino-premium{width:1920px;height:1080px;background:transparent}#scene{position:absolute;inset:0}#logo-stage{position:absolute;left:280px;top:392px;width:1360px;height:296px}.layer{position:absolute;inset:0}.piece{position:absolute;display:block;object-fit:contain;will-change:transform,opacity}#support{filter:url(#ink-support);z-index:0}#original{z-index:1}</style></head><body><div id="al-destino-premium" class="clip" data-composition-id="al-destino-premium" data-start="0" data-duration="4" data-width="1920" data-height="1080"><svg width="0" height="0" aria-hidden="true" data-layout-ignore><defs><filter id="ink-support" x="-8%" y="-15%" width="116%" height="140%"><feMorphology in="SourceAlpha" operator="dilate" radius="1.8" result="edge"/><feFlood flood-color="#FFFDF5" result="light"/><feComposite in="light" in2="edge" operator="in"/><feDropShadow dx="0" dy="1" stdDeviation="1.6" flood-color="#07120E" flood-opacity=".32"/></filter></defs></svg><div id="scene"><div id="logo-stage"><div id="support" class="layer" aria-hidden="true">${images('edge')}</div><div id="original" class="layer">${images('core')}</div></div></div></div><script>
const tl=gsap.timeline({paused:true});
tl.fromTo('.part-letra-a',{y:22,opacity:0},{y:0,opacity:1,duration:.72,ease:'power4.out'},.04);
tl.fromTo('.part-letra-l',{y:-14,opacity:0},{y:0,opacity:1,duration:.72,ease:'power4.out'},.18);
tl.fromTo('.part-sol',{y:24,scale:.92,opacity:0},{y:0,scale:1,opacity:1,duration:.82,ease:'circ.out',transformOrigin:'50% 100%'},.28);
tl.fromTo('.part-ola',{x:-16,opacity:0,clipPath:'inset(0% 100% 0% 0%)'},{x:0,opacity:1,clipPath:'inset(0% 0% 0% 0%)',duration:.95,ease:'power3.out'},.4);
tl.fromTo('.part-divisor',{scaleY:0,opacity:0},{scaleY:1,opacity:1,duration:.7,ease:'power3.out',transformOrigin:'50% 50%'},.76);
for(let i=1;i<=9;i++){const name=${JSON.stringify(pieces.filter(p=>p.id.startsWith('nombre-')).map(p=>p.id))}[i-1];tl.fromTo('.part-'+name,{x:3,y:9,opacity:0,clipPath:'inset(0% 0% 100% 0%)'},{x:0,y:0,opacity:1,clipPath:'inset(0% 0% 0% 0%)',duration:.62,ease:'power3.out'},.86+(i-1)*.045);}
tl.fromTo('.part-tagline',{y:5,opacity:0},{y:0,opacity:1,duration:.7,ease:'power2.out'},1.5);
tl.addLabel('firma-completa',2.2);tl.addLabel('lectura',2.4);
tl.to('#scene',{y:-2,opacity:0,duration:.42,ease:'power2.in'},3.48);
window.__timelines=window.__timelines||{};window.__timelines['al-destino-premium']=tl;tl.seek(0);
</script></body></html>`;
write(path.join(base,'index.html'),html);
write(path.join(base,'package.json'),JSON.stringify({name:'al-destino-premium',private:true,type:'module',scripts:{check:'npx --yes hyperframes@0.9.58 check',preview:'npx --yes hyperframes@0.9.58 preview',render:'npx --yes hyperframes@0.9.58 render'}},null,2));
write(path.join(base,'hyperframes.json'),JSON.stringify({paths:{assets:'assets',blocks:'compositions',components:'compositions/components'}},null,2));
write(path.join(base,'meta.json'),JSON.stringify({id:'al-destino-premium',name:'AL DESTINO · Firma por piezas · BORRADOR'},null,2));
write(path.join(base,'index.motion.json'),JSON.stringify({duration:4,assertions:[{kind:'appearsBy',selector:'#core-letra-a',bySec:.8},{kind:'appearsBy',selector:'#core-sol',bySec:1.1},{kind:'appearsBy',selector:'#core-tagline',bySec:2.25},{kind:'before',a:'#core-letra-a',b:'#core-tagline'},{kind:'staysInFrame',selector:'#logo-stage'},{kind:'keepsMoving',withinSelector:'#scene',maxStaticSec:1.5}]},null,2));
write(path.join(base,'fuentes.json'),JSON.stringify({status:'borrador',generator:'scripts/generar-logo-premium.cjs',source_catalog:'../../../assets/logos/piezas/catalogo.json',duration_seconds:4,fps:30,alpha:true,audio:false,core_policy:'Piezas originales intactas; capa de alfa de apoyo por detrás. Sin placa, redibujo ni recolor del frente.',parts:pieces.map(p=>({id:p.id,file:'assets/piezas/'+p.file,sha256:p.sha256})),proof_times:[0,.2,.55,1,1.6,2.3,3.2,3.7,3.98]},null,2));
console.log('Variante de 4 s preparada con 15 piezas originales, apoyo de contraste y salida transparente. BORRADOR.');
