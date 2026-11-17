/* Revisa con HyperFrames, renderiza RGBA y empaqueta WebM/APNG. No publica. */
const fs=require('fs'),path=require('path'),os=require('os'),{spawnSync}=require('child_process');
const kit=require('./generar-editorial-premium.cjs');
const root=path.resolve(__dirname,'..');
const launcher=process.env.AL_DESTINO_HYPERFRAMES_LAUNCHER||path.join(os.homedir(),'.agents/skills/hyperframes/scripts/plugin-cli.mjs');
const args=process.argv.slice(2),one=args.indexOf('--only'),selected=one>=0?args[one+1]:null;
const force=args.includes('--force');
const temp=fs.mkdtempSync(path.join(os.tmpdir(),'al-destino-editorial-'));
const catFile=path.join(kit.base,'catalogo.json');
let cat;
function run(cmd,args,cwd=root){const r=spawnSync(cmd,args,{cwd,encoding:'utf8',maxBuffer:32*1024*1024,windowsHide:true});if(r.error||r.status!==0)throw Error((r.stderr||'')+'\n'+(r.stdout||'')+'\n'+(r.error||''));return r;}
function hf(args,cwd){const r=run(process.execPath,[launcher,...args],cwd);fs.appendFileSync(path.join(temp,'hyperframes.local.log'),r.stdout+'\n'+r.stderr+'\n');return r;}
function save(){fs.writeFileSync(catFile,JSON.stringify(cat,null,2)+'\n');}
function encode(item,frames){
  const list=fs.readdirSync(frames).filter(p=>p.endsWith('.png')).sort();if(!list.length)throw Error('Render sin PNG: '+item.id);
  const prefix=list[0].match(/^(.*?)(\d+)\.png$/);if(!prefix)throw Error('Nombres inesperados de frames.');
  const pattern=path.join(frames,prefix[1]+'%0'+prefix[2].length+'d.png'),start=Number(prefix[2]);
  const common=['-y','-v','error','-framerate','30','-start_number',String(start),'-i',pattern];
  const apng=path.join(kit.output,item.slug+'.png'),webm=path.join(kit.output,item.slug+'.webm'),poster=path.join(kit.output,item.slug+'-poster.png');
  run('ffmpeg',[...common,'-plays','1','-f','apng',apng]);
  run('ffmpeg',[...common,'-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','0','-lossless','1','-row-mt','1','-auto-alt-ref','0','-an',webm]);
  fs.copyFileSync(path.join(frames,list[Math.min(list.length-1,45)]),poster);
  item.exports={webm:{file:kit.rel(kit.base,webm),sha256:kit.hash(webm),width:1920,height:1080},apng:{file:kit.rel(kit.base,apng),sha256:kit.hash(apng),width:1920,height:1080},poster:{file:kit.rel(kit.base,poster),sha256:kit.hash(poster),width:1920,height:1080}};
  const probe=JSON.parse(run('ffprobe',['-v','error','-show_entries','stream=width,height,r_frame_rate:stream_tags=alpha_mode:format=duration','-of','json',webm]).stdout);
  const alpha=run('ffmpeg',['-v','error','-c:v','libvpx-vp9','-i',webm,'-vf','alphaextract,signalstats,metadata=print:file=-','-f','null','-']);
  const nums=[...alpha.stdout.matchAll(/lavfi.signalstats.YMAX=(\d+)/g)].map(x=>Number(x[1]));
  if(nums.length!==list.length||nums[0]!==0||nums[nums.length-1]!==0||Math.max(...nums)!==255)throw Error('Verificación alfa fallida: '+item.id);
  if(Math.abs(Number(probe.format.duration)-item.duration_seconds)>.05)throw Error('Duración inesperada: '+item.id);
  item.checks={...item.checks,frame_count:list.length,webm_alpha_decoded:true,alpha_first_frame_max:nums[0],alpha_last_frame_max:nums[nums.length-1],duration_verified_seconds:Number(probe.format.duration),fps_verified:probe.streams[0].r_frame_rate,apng_frames:list.length,render_source_fingerprint:item.source_fingerprint,visual_review:'pendiente',audio:false,compatibility:'pendiente_de_prueba_en_clipo'};
  item.render_status='render_verificado';
  console.log(item.id+': '+list.length+' frames RGBA; WebM/APNG; alfa inicial/final transparente.');save();
}
function icon(item){
  if(item.kind!=='redes')return;
  const dir=path.join(temp,item.slug+'-symbol'),assets=path.join(dir,'assets');fs.mkdirSync(assets,{recursive:true});
  const svg=fs.readFileSync(path.join(kit.base,'assets/social',item.id.split('.')[1]+'.svg'),'utf8').replace(/<svg\b/,'<svg width="416" height="416"').replace(/<path\b/g,'<path fill="#FFFDF5" stroke="#10211D" stroke-width=".12" paint-order="stroke fill"');
  fs.writeFileSync(path.join(dir,'index.html'),`<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:transparent}#root{width:100%;height:100%;display:grid;place-items:center;background:transparent}</style></head><body><div id="root" data-composition-id="symbol" data-width="512" data-height="512" data-duration="0.1" data-no-timeline>${svg}</div></body></html>`);
  fs.writeFileSync(path.join(dir,'hyperframes.json'),'{}');
  const frames=path.join(temp,item.slug+'-symbol-frames');hf(['render','--format','png-sequence','--workers','1','--fps','30','--output',frames,'--quiet'],dir);
  const file=fs.readdirSync(frames).filter(x=>x.endsWith('.png')).sort()[0],dest=path.join(kit.output,item.slug+'-simbolo.png');fs.copyFileSync(path.join(frames,file),dest);item.exports.icon_png={file:kit.rel(kit.base,dest),sha256:kit.hash(dest),width:512,height:512};save();
}
try{
  fs.mkdirSync(kit.output,{recursive:true});
  run(process.execPath,[path.join(root,'scripts/generar-editorial-premium.cjs'),'--catalog-only']);
  cat=JSON.parse(fs.readFileSync(catFile,'utf8'));
  if(selected&&!cat.items.some(i=>i.id===selected||i.slug===selected))throw Error('Variante desconocida: '+selected);
  for(const item of cat.items.filter(i=>!selected||i.id===selected||i.slug===selected)) {
    const exportsMatch=['webm','apng','poster'].every(role=>item.exports[role])&&Object.values(item.exports).every(e=>fs.existsSync(path.resolve(kit.base,e.file))&&kit.hash(path.resolve(kit.base,e.file))===e.sha256);
    const renderCurrent=exportsMatch&&item.checks.webm_alpha_decoded&&item.checks.render_source_fingerprint===item.source_fingerprint;
    if(!force&&renderCurrent&&item.checks.hyperframes_ok&&item.checks.validation_fingerprint===item.validation_fingerprint){console.log(item.id+': exportaciones vigentes.');continue;}
    const dir=path.dirname(path.join(kit.base,item.composition_file));console.log('Comprobando '+item.id+'…');
    const r=hf(['check','--json'],dir);const check=JSON.parse(r.stdout.slice(r.stdout.indexOf('{')));
    if(!check.ok)throw Error('HyperFrames check falló: '+item.id+'\n'+r.stdout);
    item.checks={...item.checks,hyperframes_ok:check.ok,validation_fingerprint:item.validation_fingerprint,validation_pending:false,hyperframes_version:check._meta?.version,lint_errors:check.lint.errorCount,runtime_errors:check.runtime.errorCount,layout_errors:check.layout.errorCount,motion_errors:check.motion.errorCount,contrast_checks:check.contrast.checked,accepted_warnings:(check.craft?.findings||[]).filter(x=>x.code==='first_frame_empty').map(x=>({code:x.code,reason:'Entrada y salida transparentes de overlay; poster separado.'}))};
    item.validation_status='verificado';save();
    if(!force&&renderCurrent){console.log(item.id+': comprobación actualizada; imagen renderizada conservada.');continue;}
    const frames=path.join(temp,item.slug+'-frames');
    console.log('Renderizando '+item.id+'…');hf(['render','--format','png-sequence','--workers','2','--fps','30','--output',frames,'--quiet'],dir);
    encode(item,frames);icon(item);
  }
  run(process.execPath,[path.join(root,'scripts/generar-editorial-premium.cjs'),'--catalog-only']);
  console.log('Catálogo actualizado. Evidencia temporal privada: '+temp);
}catch(e){console.error(e.message);console.error('Evidencia local: '+temp);process.exitCode=1;}
