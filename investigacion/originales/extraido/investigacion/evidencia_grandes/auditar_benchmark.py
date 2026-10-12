import json,pathlib,datetime,statistics,math,hashlib,html
from collections import Counter,defaultdict
from zoneinfo import ZoneInfo

ROOT=pathlib.Path(__file__).resolve().parents[2]
SOURCE=ROOT/'output/datos_benchmark.json'
D=json.loads(SOURCE.read_text()); assert len(D['videos'])==96
TAX={
 'guia_logistica_costo':'Guía, logística o costos: resolver una decisión o explicar acceso, precio, itinerario o funcionamiento.',
 'review_alojamiento':'Review de alojamiento: probar o evaluar hotel, resort o glamping como objeto principal.',
 'reto_transporte':'Reto o transporte: desplazamiento, cruce, vehículo o misión con restricción como historia principal.',
 'cultura_reportaje':'Cultura o reportaje: vida de personas, lugares, historia, comunidades, instituciones o problemas.',
 'personal':'Personal: familia, relaciones, embarazo, cambios vitales, miedo o hitos del creador.',
 'listas':'Lista: selección explícita numerada de recomendaciones o alternativas; números de tiempo, edad o episodios no cuentan.',
 'gastronomia':'Gastronomía: probar alimentos o bebidas como promesa principal.',
 'naturaleza_paisaje':'Naturaleza y paisaje: entorno natural, safari, paisajes y cicloturismo escénico.',
 'promocion_trailer':'Promoción o trailer: sorteo o adelanto de otra obra, sin equipararlo al episodio editorial.',
}
G='guia_logistica_costo';H='review_alojamiento';R='reto_transporte';C='cultura_reportaje';P='personal';L='listas';F='gastronomia';N='naturaleza_paisaje';A='promocion_trailer'
# Codificación manual congelada de los 96 registros, ligada al SHA-256 de la fuente.
# Categoría primaria primero; secundarias sólo cuando hay una segunda promesa explícita.
MAP=[
 [P],[P],[P,C],[P,C],[P],[P],[P],[P],
 [H],[H,G],[H],[H],[H],[R],[G],[G],
 [G,C],[C],[C],[G],[C],[G,C],[G,C],[C],
 [C,P],[C,F],[H,P],[F,C],[R,G],[C],[F],[R,G],
 [C],[C],[C],[C,P],[C,R],[C,R],[C],[C],
 [P,N],[G],[P],[C],[N],[C],[N,C],[R,P],
 [C,P],[C],[C],[C],[R,C],[C],[C],[L,P],
 [R,N],[R],[P,C],[C],[R],[R],[R],[C],
 [C],[R,G],[C],[C],[R],[C],[C],[C],
 [H,G],[C,P],[C,P],[G,C],[L,G],[A],[G],[R,G],
 [P],[L,G],[G,C],[C],[G,N],[H],[C],[L,F],
 [N],[H,N],[N,R],[A,N],[N,R],[A,N],[N,R],[A,N],
]
assert len(MAP)==96
WHY={
 G:'El título o la descripción plantea una decisión, logística, costos o guía práctica.',
 H:'La promesa central es evaluar un alojamiento nombrado o una experiencia de hotelería.',
 R:'El viaje, vehículo, cruce o regla temporal/de presupuesto constituye la promesa central.',
 C:'La promesa central describe un lugar, comunidad, historia o acceso a una realidad.',
 P:'La promesa central es un momento personal, familiar, una emoción o un hito del creador.',
 L:'El título presenta una selección numerada de recomendaciones, países, platos u opciones.',
 F:'El alimento o bebida es la promesa dominante, aunque el recorrido incluya otros sitios.',
 N:'La promesa central es un paisaje, experiencia de naturaleza o cicloturismo escénico.',
 A:'El título y/o descripción identifica sorteo o trailer de otro episodio.',
}
NOTES={
 2:'Babymoon combina viaje y familia; prima el hito personal. Descripción comercial poco informativa.',
 3:'Viaje antes de nacimiento: el conflicto dominante es familiar, no una guía del destino.',
 5:'Título genérico; clasificación personal de menor certeza. No se infiere el cambio concreto.',
 13:'Cuatro parques en un día es una misión temporal; no una lista de recomendaciones.',
 16:'Título de visita; descripción promete todo lo necesario para visitar pirámides: guía + historia.',
 18:'Descripción de Dendera repite texto de crucero. Se prioriza título para cultura; inconsistencia marcada.',
 20:'La descripción identifica una hacienda de tequila. No se presupone degustación como promesa central.',
 24:'Recorrido por Madrid y Barcelona según descripción; VLOG no significa automáticamente vida personal.',
 25:'Visita a lugares antiguos; la cantina añade gastronomía secundaria.',
 26:'Review de un hotel en que invierte: alojamiento primario; emprendimiento personal secundario.',
 27:'El título concentra un recorrido amplio en Coca-Cola; se codifica gastronomía primaria.',
 31:'Trámites y tren hasta consulado: transporte + logística. No promete una guía exhaustiva de visado.',
 33:'Conflicto en una convivencia turística: reportaje, no experimento controlado de estafa.',
 36:'Subcultura de carreras: cultura primaria con transporte secundario.',
 37:'Vida dentro de buque: acceso institucional primario, transporte secundario.',
 41:'Costos de vivir en Venezuela; categoría información de costos, no asesoría financiera.',
 46:'Título emocional ambiguo; isla/cultura por descripción. Se evita interpretar romance no comprobado.',
 47:'Descripción explicita cruce terrestre a Gambia, con miedo como componente personal.',
 48:'Interacción social ligada a búsqueda de pareja; cultura primaria, personal secundaria.',
 55:'Cinco países seleccionados desde experiencia: lista primaria, personal secundaria.',
 58:'País número100: hito personal, no lista ni reto temporal.',
 61:'Siete maravillas en siete días: misión con tiempo, no lista editorial de recomendaciones.',
 75:'Llegada, aeropuerto, taxi y hotel: logística útil a pesar del formato vlog.',
 76:'Cinco observatorios comparados: lista + costos de entrada.',
 79:'Ruta14h y ahorro400$: reto temporal + presupuesto.',
 80:'La descripción declara cierre del proyecto; evento de ciclo de vida, no video turístico ordinario.',
 81:'Diez actividades recomendadas: lista + guía.',
 82:'Primeras24h orientadas a qué hacer/seguridad; no reto temporal explícito.',
 86:'Título inespecífico; cultura como clasificación provisional de baja certeza, sin inferir motivo.',
 87:'Cinco platos: lista primaria y gastronomía secundaria.',
 88:'Pieza breve de localización; naturaleza provisional, no capítulo largo convencional.',
 89:'La descripción explica búsqueda de glamping y alojamiento.',
 91:'Trailer del episodio de ciclismo: promoción primaria, naturaleza secundaria.',
 93:'Trailer del episodio de ciclismo: promoción primaria, naturaleza secundaria.',
 95:'Trailer del episodio de ciclismo: promoción primaria, naturaleza secundaria.',
}
OBS=datetime.date.fromisoformat(D['observedDate'])
rows=[]
for i,(raw,labels) in enumerate(zip(D['videos'],MAP)):
 dt=datetime.datetime.fromisoformat(raw['datePublished']).astimezone(ZoneInfo(D['timezone']))
 r={'source_index':i,'channel':raw['channel'],'video_id':raw['videoId'],'title':raw.get('titleExact') or raw['title'],'source_url':raw['url'],'date_local':dt.date().isoformat(),'age_days':(OBS-dt.date()).days,'views':int(raw['viewsExact']),'duration_seconds':int(raw['lengthSeconds']),'primary_category':labels[0],'labels':labels,'classification_basis':'Título y descripción públicos de la fuente; no visionado completo','rationale':NOTES.get(i,WHY[labels[0]]),'classification_confidence':'baja' if i in [5,46,86,88] else 'media' if i in [2,3,18,20,24,27,31,48,75] else 'alta','format_flag':'trailer' if i in [91,93,95] else 'sorteo' if i==77 else 'anuncio_cierre' if i==80 else 'pieza_breve' if i==88 else 'editorial','channel_lifecycle':next(c['status'] for c in D['channels'] if c['channel']==raw['channel'])}
 rows.append(r)
def median(a):return statistics.median(a) if a else None
def ranks(a):
 pos=defaultdict(list)
 for i,x in enumerate(sorted(a)):pos[x].append(i+1)
 return [sum(pos[x])/len(pos[x]) for x in a]
def pearson(a,b):
 ma=statistics.mean(a);mb=statistics.mean(b);den=(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))**.5
 return sum((x-ma)*(y-mb) for x,y in zip(a,b))/den if den else None
def rho(a,b):return pearson(ranks(a),ranks(b))
summaries=[];pairs=[];outliers=[]
for ch in D['channels']:
 rs=[r for r in rows if r['channel']==ch['channel']];v=[r['views'] for r in rs];base=median(v);sv=sorted(v);q1=median(sv[:4]);q3=median(sv[4:]);iqr=q3-q1
 s={'channel':ch['channel'],'n':8,'age_min_days':min(r['age_days'] for r in rs),'age_max_days':max(r['age_days'] for r in rs),'age_span_days':max(r['age_days'] for r in rs)-min(r['age_days'] for r in rs),'median_views':base,'mean_views':statistics.mean(v),'median_without_max':median(sv[:-1]),'median_without_min':median(sv[1:]),'median_without_both':median(sv[1:-1]),'mean_without_max':statistics.mean(sv[:-1]),'mean_without_min':statistics.mean(sv[1:]),'median_editorial_only':median([r['views'] for r in rs if r['format_flag']=='editorial']),'n_editorial':sum(r['format_flag']=='editorial' for r in rs),'spearman_age_views':rho([r['age_days'] for r in rs],v),'category_counts':dict(Counter(r['primary_category'] for r in rs)),'lifecycle':ch['status'],'use_for_launch_hypotheses':ch['gapSinceLatestDays']<=60}
 for key in ['median_without_max','median_without_min','median_without_both','mean_without_max','mean_without_min']:
  refer=base if key.startswith('median') else s['mean_views'];s[key+'_change_pct']=(s[key]/refer-1)*100
 summaries.append(s)
 for r in rs:
  r['relative_to_channel_sample_median']=r['views']/base
  r['tukey_high_flag']=r['views']>q3+1.5*iqr
  r['exploratory_high_2x_flag']=r['views']/base>=2
  if r['tukey_high_flag'] or r['exploratory_high_2x_flag']:
   outliers.append({'channel':r['channel'],'video_id':r['video_id'],'title':r['title'],'views':r['views'],'age_days':r['age_days'],'relative_to_channel_sample_median':r['relative_to_channel_sample_median'],'tukey_high_flag':r['tukey_high_flag'],'exploratory_2x_flag':r['exploratory_high_2x_flag'],'format_flag':r['format_flag'],'source_url':r['source_url']})
 for j,a in enumerate(rs):
  for b in rs[j+1:]:
   agegap=abs(a['age_days']-b['age_days']);ratio=max(a['age_days'],b['age_days'])/min(a['age_days'],b['age_days']) if min(a['age_days'],b['age_days']) else float('inf')
   if min(a['age_days'],b['age_days'])>=14 and agegap<=7 and ratio<=1.5 and a['format_flag']=='editorial' and b['format_flag']=='editorial':
    hi,lo=sorted([a,b],key=lambda r:r['views'],reverse=True)
    pairs.append({'channel':ch['channel'],'higher_id':hi['video_id'],'lower_id':lo['video_id'],'higher_title':hi['title'],'lower_title':lo['title'],'higher_age_days':hi['age_days'],'lower_age_days':lo['age_days'],'age_gap_days':agegap,'age_ratio':ratio,'views_ratio':hi['views']/lo['views'],'higher_category':hi['primary_category'],'lower_category':lo['primary_category'],'different_primary_categories':hi['primary_category']!=lo['primary_category'],'recent_channel':ch['gapSinceLatestDays']<=60,'higher_url':hi['source_url'],'lower_url':lo['source_url'],'interpretation':'Par de edades próximas; no es medición al mismo día de vida, no independiente de otros pares ni prueba causal.'})
counts=Counter(r['primary_category'] for r in rows)
res={'observedDate':D['observedDate'],'timezone':D['timezone'],'input_file':str(SOURCE),'input_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'n_records':96,'n_channels':12,'taxonomy':TAX,'classification_method':'Manual, primaria exclusiva y secundarias explícitas; tabla MAP por índice congelada al hash de entrada, resultados también ligados a video_id. Basada en títulos/descripciones, sin simular visionado. No se ejecutó doble codificación independiente.','age_matching_rule':{'min_age_days':14,'max_absolute_age_gap_days':7,'max_age_ratio':1.5,'same_channel':True,'editorial_only':True,'meaning':'Filtro descriptivo de proximidad, nunca comparabilidad perfecta.'},'primary_category_counts':dict(counts),'category_channel_counts':{k:len(set(r['channel'] for r in rows if r['primary_category']==k)) for k in TAX},'format_counts':dict(Counter(r['format_flag'] for r in rows)),'channel_summaries':summaries,'candidate_age_near_pairs':pairs,'exploratory_outliers':outliers,'classified_records':rows,'prohibitions':['No causalidad','No vistas/días ni aproximación de velocidad','No ranking global por vistas absolutas','No conclusiones de CTR/retención/conversión/ingresos no observados','No promediar ratios entre pares solapados como muestra independiente'],'limitations':['Últimas8 piezas por canal: selección no aleatoria, fechas y destinos muy distintos.','Vistas acumuladas a distinta edad y sin historial longitudinal.','Taxonomía subjetiva; confianza y ambigüedades declaradas.','Fama/escala, destino, promoción, distribución y miniatura no controlados.','Cierre/pausa y trailers afectan comparación de calendario y temas.','No se tienen impresiones, alcance no suscriptor ni métricas privadas.']}
res['matching_sensitivity']={'base_recent_channel_pairs':sum(p['recent_channel'] for p in pairs),'base_recent_pairs_different_categories':sum(p['recent_channel'] and p['different_primary_categories'] for p in pairs),'max_gap_3_days_recent_pairs':sum(p['recent_channel'] and p['age_gap_days']<=3 for p in pairs),'min_age_30_days_recent_pairs':sum(p['recent_channel'] and min(p['higher_age_days'],p['lower_age_days'])>=30 for p in pairs),'warning':'Pares solapados y reglas elegidas descriptivamente; no son réplicas independientes ni significancia estadística.'}
themes=[]
for ch in D['channels']:
 for cat in TAX:
  rs=[r for r in rows if r['channel']==ch['channel'] and r['primary_category']==cat and r['format_flag']=='editorial']
  if not rs:continue
  amin=min(r['age_days'] for r in rs);amax=max(r['age_days'] for r in rs)
  eligible=len(rs)>=2 and amin>=14 and amax-amin<=7 and amax/amin<=1.5
  themes.append({'channel':ch['channel'],'primary_category':cat,'n_editorial':len(rs),'age_min':amin,'age_max':amax,'age_near_group_eligible':eligible,'median_views_if_age_near':median([r['views'] for r in rs]) if eligible else None,'video_ids':[r['video_id'] for r in rs],'meaning':'Sin mediana temática de desempeño cuando el grupo mezcla edades demasiado diferentes.'})
res['within_channel_theme_groups']=themes
res['findings']=[{'id': 1, 'claim': 'El benchmark describe sistemas editoriales distintos, no 96 estrenos comparables.', 'evidence': 'Hay 90 registros editoriales, 3 trailers, 1 sorteo, 1 anuncio de cierre y 1 pieza breve. Las edades van de 2 a 1,923 días. Sólo 7 de los 12 canales tienen una publicación de Videos dentro de los últimos 60 días.', 'implication': 'Separar formato y ciclo de vida antes de planificar cadencia o tomar un canal como referencia actual.', 'test': 'Registrar Videos, Shorts, Reels y anuncios por separado. Elegir referentes de etapa y capacidad semejantes.'}, {'id': 2, 'claim': 'La edad impide declarar un ganador temático con vistas acumuladas.', 'evidence': 'En PlanetaJuan, los 8 registros aumentan sus vistas estrictamente con su edad: Spearman 1.00, edades de 2 a 34 días. Esa relación no separa tiempo, destino, tema ni empaquetado.', 'implication': 'El mayor acumulado de su lista de países no demuestra que las listas superen otros temas.', 'test': 'Comparar métricas propias a los 7 y 28 días exactos desde el estreno. No dividir vistas entre edad.'}, {'id': 3, 'claim': 'La proximidad de edad reduce mucho la evidencia disponible.', 'evidence': '26 pares pasan el filtro de edades; 17 pertenecen a canales con actividad reciente y 11 comparan categorías distintas. Reducir la diferencia máxima de 7 a 3 días deja 3 pares recientes, concentrados en Vero y PlanetaJuan.', 'implication': 'No existe base para un ranking general de categorías. Los pares se solapan y cambian al variar una regla.', 'test': 'Tratar los pares como fuentes de hipótesis. Producir bloques comparables de tres promesas sobre un destino y repetir en otro.'}, {'id': 4, 'claim': 'Algunos videos destacan dentro del canal y ofrecen hipótesis, no recetas.', 'evidence': 'Vero: peor viaje 3.64× la mediana; frente a Zanzíbar, 3.76× a 26 versus 23 días. Ramilla: vuelo 6.99× afición, a 142 versus 147 días. Luisito: comida de Cabo Verde 1.09× recorrido del país, a 56 versus 49 días.', 'implication': 'Diferencias enormes y pequeñas coexisten. La tensión real y una experiencia concreta merecen pruebas propias; no se pueden afirmar sus causas.', 'test': 'Probar dificultad real más resolución y experiencia más veredicto con recursos accesibles. Repetir y medir costo y tiempo antes de ampliar la producción.'}, {'id': 5, 'claim': 'La estabilidad de una mediana puede ser matemática; las medias son sensibles a excepciones.', 'evidence': 'Con 8 datos, quitar juntos el mayor y el menor conserva automáticamente la mediana. Quitar sólo el máximo reduce la mediana 15.6% en Misias y 46.8% en La Vida de Viaje; la media cae 27.0% en Vero. Filtrar La Vida de Viaje a 4 piezas editoriales cambia su mediana de 1,191.5 a 2,651.5.', 'implication': 'No prometer alcance típico basado en un éxito excepcional ni llamar robustez a una invariancia por construcción.', 'test': 'Reportar mediana y rango, con y sin el mayor resultado. Registrar costo y horas por video para decidir qué es sostenible.'}]
res['verified_platform_sources']=[{'url': 'https://support.google.com/youtube/answer/16391400?hl=en', 'title': 'A/B test titles & thumbnails — YouTube Help', 'consulted_on': '2026-10-06', 'supports': 'YouTube Studio de escritorio; funciones avanzadas; hasta tres variantes; resultado por tiempo de visualización; hasta dos semanas; no disponible para Shorts.'}, {'url': 'https://support.google.com/youtube/answer/9314486', 'title': 'Check your YouTube thumbnail impressions and watch time — YouTube Help', 'consulted_on': '2026-10-06', 'supports': 'Impresiones, CTR y tiempo de visualización accesibles en Analytics de contenido propio, con superficies/exclusiones.'}]
(ROOT/'investigacion/05_auditoria_cuantitativa.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
print('categorias',dict(counts));print('formatos',res['format_counts']);print('pairs',len(pairs),'recent',sum(x['recent_channel'] for x in pairs),'difftheme',sum(x['recent_channel'] and x['different_primary_categories'] for x in pairs));print('outliers',json.dumps(outliers,ensure_ascii=False));print('summaries',json.dumps([{k:s[k] for k in ['channel','age_min_days','age_max_days','spearman_age_views','median_without_max_change_pct','median_without_min_change_pct','mean_without_max_change_pct','n_editorial','median_editorial_only']} for s in summaries],ensure_ascii=False));print('recent pairs',json.dumps([p for p in pairs if p['recent_channel'] and p['different_primary_categories']],ensure_ascii=False))
