import urllib.request,re,html,json,pathlib,concurrent.futures
D=json.load(open('investigacion/00_instagram_grids.json'))
indexes={'veronicaweffer':[0,1,2],'planetajuan':[0,1,2],'misiasperoviajeras':[1,2,6],'lavidadeviaje':[0,3,4]}
sample={}
def get(p):
 try:
  s=urllib.request.urlopen(urllib.request.Request(p['url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read().decode()
  metas={}
  for m in re.findall(r'<meta[^>]+>',s):
   prop=re.search(r'(?:property|name)="([^"]+)"',m);content=re.search(r'content="([^"]+)"',m)
   if prop and content and prop.group(1)in ['og:description','description','og:title']:metas[prop.group(1)]=html.unescape(content.group(1))
  return {'url':p['url'],'gridAlt':p['images'][0]['alt'],'meta':metas}
 except Exception as e:return {'url':p['url'],'error':str(e)}
for h,ind in indexes.items():
 with concurrent.futures.ThreadPoolExecutor(max_workers=3)as ex:sample[h]=list(ex.map(get,[D[h][i]for i in ind]))
 print(h,json.dumps(sample[h],ensure_ascii=False))
pathlib.Path('investigacion/02_instagram_posts.json').write_text(json.dumps(sample,ensure_ascii=False,indent=2))
