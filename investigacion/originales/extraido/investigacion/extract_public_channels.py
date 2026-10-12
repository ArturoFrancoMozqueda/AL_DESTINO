import urllib.request,re,json,concurrent.futures,pathlib
channels={'Misias pero viajeras':'@misiasperoviajeras','Viajando con Vero':'@ViajandoconVero','La Vida de Viaje':'lavidadeviaje','PlanetaJuan':'@planetajuan'}
out={}
def fetch(u):return urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read().decode()
def walk(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
def watchmeta(v):
 try:
  s=fetch(v['url']);m=re.search(r'var ytInitialPlayerResponse = (.*?);</script>',s)
  if m:
   p=json.loads(m.group(1));d=p.get('videoDetails',{});micro=p.get('microformat',{}).get('playerMicroformatRenderer',{})
   v.update({'datePublished':micro.get('publishDate'),'dateUploaded':micro.get('uploadDate'),'lengthSeconds':d.get('lengthSeconds'),'viewsExact':d.get('viewCount'),'author':d.get('author'),'description':d.get('shortDescription'),'titleExact':d.get('title')})
  else:
   v['datesFromMeta']=re.findall(r'itemprop="(?:datePublished|uploadDate)" content="([^"]+)"',s)
 except Exception as e:v['watchError']=str(e)
 return v
for name,h in channels.items():
 try:
  u='https://www.youtube.com/'+h+'/videos';s=fetch(u);d=json.loads(re.search(r'var ytInitialData = (.*?);</script>',s).group(1));rows=[];ids=set()
  for x in walk(d):
   if 'lockupViewModel' in x:
    r=x['lockupViewModel'];i=r.get('contentId','');meta=r.get('metadata',{}).get('lockupMetadataViewModel',{});title=meta.get('title',{}).get('content');im=r.get('contentImage',{}).get('thumbnailViewModel',{});parts=[a.get('text',{}).get('content') for row in meta.get('metadata',{}).get('contentMetadataViewModel',{}).get('metadataRows',[]) for a in row.get('metadataParts',[])];badges=[z['thumbnailBadgeViewModel'].get('text') for z in walk(im) if 'thumbnailBadgeViewModel'in z]
    if r.get('contentType')=='LOCKUP_CONTENT_TYPE_VIDEO' and title and i not in ids:ids.add(i);rows.append({'videoId':i,'url':'https://www.youtube.com/watch?v='+i,'title':title,'metadata':parts,'duration':badges[0]if badges else None,'thumbnail':im.get('image',{}).get('sources',[])})
   elif 'videoRenderer' in x:
    r=x['videoRenderer'];i=r.get('videoId');title=''.join(z['text']for z in r.get('title',{}).get('runs',[]))
    if i not in ids:ids.add(i);rows.append({'videoId':i,'url':'https://www.youtube.com/watch?v='+i,'title':title,'metadata':[r.get('viewCountText'),r.get('publishedTimeText')],'duration':r.get('lengthText',{}).get('simpleText')})
  with concurrent.futures.ThreadPoolExecutor(max_workers=4)as ex:rows=list(ex.map(watchmeta,rows[:8]))
  out[name]={'channelUrl':u,'source':'HTML público ytInitialData + ytInitialPlayerResponse','observedDate':'2026-10-06','videos':rows}
  print(name,json.dumps([{k:v.get(k)for k in ['title','url','metadata','duration','datePublished','lengthSeconds','viewsExact']}for v in rows],ensure_ascii=False))
 except Exception as e:out[name]={'error':str(e)};print(name,str(e))
pathlib.Path('investigacion/02_parejas_nomadas_datos.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
