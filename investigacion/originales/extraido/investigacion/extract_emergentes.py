import json,pathlib,re,urllib.request,concurrent.futures,datetime,statistics
D=json.load(open('investigacion/04_emergentes_raw.json'))
def get(v):
 try:
  s=urllib.request.urlopen(urllib.request.Request(v['url'],headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read().decode();m=re.search(r'var ytInitialPlayerResponse = (.*?);</script>',s);p=json.loads(m.group(1));d=p.get('videoDetails',{});micro=p.get('microformat',{}).get('playerMicroformatRenderer',{});v.update({'datePublished':micro.get('publishDate'),'viewsExact':d.get('viewCount'),'lengthSeconds':d.get('lengthSeconds'),'titleExact':d.get('title'),'author':d.get('author'),'description':d.get('shortDescription')})
 except Exception as e:v['error']=str(e)
 return v
out={}
for n,c in D.items():
 m=next(h for h in c['headers']if 'title'in h);header=c['headers'][0]['header']['contentMetadataViewModel']['metadataRows'];meta=[p.get('text',{}).get('content')for row in header for p in row.get('metadataParts',[])];c2={k:c[k]for k in ['channelID','channelUrl','observedDate']};c2.update({'name':m['title'].strip(),'handle':meta[0],'subscribersVisible':meta[1],'totalVideosVisible':meta[2],'descriptionChannel':m['description'],'primaryHandleUrl':m['ownerUrls'][0].replace('http:','https:')})
 with concurrent.futures.ThreadPoolExecutor(max_workers=4)as ex:c2['videos']=list(ex.map(get,c['videos']))
 links=[]
 for v in c2['videos']:
  links+=re.findall(r'https?://(?:www\.)?instagram\.com/[^\s<>"\)]+',v.get('description',''))
 c2['instagramLinksFromVideoDescriptions']=sorted(set(links));dates=[datetime.datetime.fromisoformat(v['datePublished']).date()for v in c2['videos']if v.get('datePublished')];gaps=[(a-b).days for a,b in zip(dates,dates[1:])];dur=[int(v['lengthSeconds'])for v in c2['videos']if v.get('lengthSeconds')];views=[int(v['viewsExact'])for v in c2['videos']if v.get('viewsExact')];c2['sampleStats']={'n':len(c2['videos']),'firstDate':str(min(dates)),'lastDate':str(max(dates)),'spanDays':(max(dates)-min(dates)).days,'intervalDaysNewestFirst':gaps,'videosPerWeekObserved':7*(len(dates)-1)/(max(dates)-min(dates)).days,'medianDurationSeconds':statistics.median(dur),'minViews':min(views),'maxViews':max(views),'medianViews':statistics.median(views)};out[n]=c2;print(n,json.dumps({k:c2[k]for k in ['handle','subscribersVisible','instagramLinksFromVideoDescriptions','sampleStats','videos']},ensure_ascii=False)[:24000])
pathlib.Path('investigacion/04_referentes_emergentes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
