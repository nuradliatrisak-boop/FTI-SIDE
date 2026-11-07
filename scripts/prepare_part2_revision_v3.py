"""User-directed Part 2 caption corrections, event insert plan, and quote timings."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1];docs=root/'docs/part2-revision-v3';docs.mkdir(exist_ok=True,parents=True)
words=[dict(w) for w in json.load(open(root/'docs/captions-merged.json')) if w['startMs']>=1161600]
audit=[]
def phrase(a,b,text,request):
 global words
 old=[w for w in words if a*1000<=(w['startMs']+w['endMs'])/2<b*1000]
 assert old,(a,b)
 words=[w for w in words if w not in old];parts=text.split();total=sum(max(len(x),2) for x in parts) or 1;t=a
 for i,p in enumerate(parts):
  end=b if i==len(parts)-1 else t+(b-a)*max(len(p),2)/total
  words.append(dict(text=' '+p,startMs=round(t*1000),endMs=round(end*1000),timestampMs=round(t*1000),confidence=None,pageBreakAfter=i==len(parts)-1 and text.endswith(('.', '!', '?'))));t=end
 audit.append(dict(request=request,sourceStart=a,sourceEnd=b,before=''.join(w['text'] for w in old),after=text))
rules=[('Puyak','Puya',3),('ngamil','ngambil',4),('Apulia','Kak Puya',5),('Seju','Setuju',6),('Suju','Setuju',6),('Ghifariel','Ghivariel',7),('Pempek','Fun fact',8),('belajian','belajar',11),('estafrolasin','astaghfirullahalazim',13),('FTA','FTI',16),('Kapuya','Kak Puya',19),('eksksursi','ekskursi',20),('hektik','hectic',21),('241','24',22),('gox','goks',24),('Kegang','Keganggu',26),('praktiknya','praktikumnya',27),('RK-A','proker A',28),('ketuapelaksana','ketua pelaksana',28),('nyerima','nerima',29),('Kapuia','Kak Puya',30),('puyong','puyeng',33),('Gidang','Kinan','35a'),('threw','through',41),('DC','',42),('setengahnya','seenggaknya',45),('BM','BEM',46),('nenggu','nunggu',47),('ngobrolan','obrolan',49)]
for w in words:
 for old,new,n in rules:
  if re.search(r'\b'+re.escape(old)+r'\b',w['text'],re.I):
   before=w['text'];w['text']=re.sub(r'\b'+re.escape(old)+r'\b',new,w['text'],flags=re.I);audit.append(dict(request=n,sourceStart=w['startMs']/1000,before=before,after=w['text']))
 s=w['startMs']/1000
 for a,b,old,new,n in [(1379,1382,'AP','apa',10),(1489,1491,'Dekan','Deg-degan',14),(1549,1552,'ayah','ayo',18),(1570,1581,'studio','studi',20),(1808,1810,'kah','Akankah',31),(1829,1831,'Cok','',34),(1909,1910,'kan','gak',37),(1941,1945,'dapetnya','dapetin',39),(1960,1963,'vlog','flop',40),(2203,2206,'doang','dong',48),(2216,2218,'begini','segini',50)]:
  if a<=s<b and re.search(r'\b'+old+r'\b',w['text'],re.I):
   before=w['text'];w['text']=re.sub(r'\b'+old+r'\b',new,w['text'],flags=re.I);audit.append(dict(request=n,sourceStart=s,before=before,after=w['text']))
phrase(1327.83,1329.45,'Jadi gitu sih kalau dari gue.',9)
phrase(1459.04,1460,'',12)
phrase(1510.21,1511.55,'',15)
phrase(1814.13,1814.43,'asbun',32)
phrase(1863.99,1866.31,'Berarti Kinan udah ready ya jadi ketua pelaksana.','35b')
phrase(1932.44,1933.50,'Just all out.',38)
phrase(2019.56,2021.58,'Kalian bisa sharing-sharing di situ',43)
phrase(2052.28,2053.04,'tata krama',44)
words=[w for w in words if w['text'].strip(' .,') and not re.search(r'\[(?:ucapan|nama) kurang jelas\]',w['text'])]
words.sort(key=lambda w:w['startMs']);pages=[];group=[]
def flush():
 if not group:return
 x=[dict(w) for w in group];x[0]['text']=' '+x[0]['text'].lstrip();pages.append(dict(startMs=x[0]['startMs'],endMs=max(x[-1]['endMs'],x[0]['startMs']+100),words=x));group.clear()
for w in words:
 if group and (len(group)>=6 or len(''.join(x['text'] for x in group))+len(w['text'])>48 or w['startMs']-group[0]['startMs']>2800 or w['startMs']-group[-1]['endMs']>650):flush()
 group.append(w)
 if w.get('pageBreakAfter') or re.search(r'[.!?]$',w['text']):flush()
flush()
for i in range(len(pages)-1):pages[i]['endMs']=min(pages[i]['endMs'],pages[i+1]['startMs'])
for name,obj in [('part2-captions-v3.json',words),('part2-pages-v3.json',pages)]: (root/'studio/src/data'/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
(docs/'caption-corrections.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
quotes=[
 {'start':1245.22,'end':1251.38,'text':'Itulah positifnya kalian berorganisasi,\nkarena kalian dikelilingi\noleh orang-orang yang positif.'},
 {'start':1439.51,'end':1441.95,'text':'Akademik number one.\nKarena kalian kuliah untuk belajar.'},
 {'start':1928.58,'end':1933.50,'text':'Kalian harus confident aja sih\napa yang kalian punya.\nJust all out.'},
 {'start':2048.62,'end':2053.04,'text':'Harus bertanggung jawab,\nterus juga tetap jaga tata krama.'},
 {'start':2119.09,'end':2124.55,'text':'Jangan lupa dengan komitmen\nkalian di organisasi.'},
 {'start':2132.82,'end':2136.26,'text':'Dan di situlah\ntime management kita diuji.'},
 {'start':2151.94,'end':2155.36,'text':'Jangan cepat menyerah\nsama progres-progres kalian.'},
 {'start':2155.62,'end':2157.08,'text':'Jangan cepat puas.'},
 {'start':2157.08,'end':2159.02,'text':'Ikhlas sama hasil\napa yang kalian dapat.'},
 {'start':2185.46,'end':2189.92,'text':'Boleh kurang bensin,\ntapi jangan sampai habis bensin.'},
]
plan={'fps':30,'introSeconds':20,'outroSeconds':10,'dissolveSeconds':.2,'bodySpans':[[1161.6,1873.6],[1907.2,2279.9]],'bodyStart':19.8,'bodySeconds':1084.5,'durationSeconds':1114.3,'frames':33429,'images':[{'name':'FTI IMPACT','file':'part2-fti-impact.jpg','start':1521.1,'duration':8},{'name':'STUDI EKSKURSI • SARI ROTI','file':'part2-sari-roti.jpg','start':1609.4,'duration':8},{'name':'UPGRADING • SKILL ACHIEVEMENT','file':'part2-upgrading.jpg','start':1645.4,'duration':8}],'quotes':quotes,'chapters':[{'start':1161.6,'title':'Bertumbuh lewat Ormawa'},{'start':1466,'title':'Di Balik Sebuah Proker'},{'start':1907.2,'title':'Pesan untuk yang Mau Mulai'}]}
(docs/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print(len(words),'words',len(pages),'pages',len(audit),'corrections; duration',plan['durationSeconds'])

(root/'studio/src/data/part2-plan-v3.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
