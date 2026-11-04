"""Part 1-only caption corrections and EDL from the user's 63-point revision."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
words=json.loads((root/'docs/captions-merged.json').read_text());words=[dict(w) for w in words if w['startMs']<1161600]
audit=[]
def phrase(a,b,text,request):
 global words
 old=[w for w in words if a*1000<=(w['startMs']+w['endMs'])/2<b*1000]
 if not old:return
 words=[w for w in words if w not in old]
 parts=text.split();weights=[max(len(x.strip('.,!?')),2) for x in parts];total=sum(weights) or 1;t=a
 for i,(p,weight) in enumerate(zip(parts,weights)):
  end=b if i==len(parts)-1 else t+(b-a)*weight/total
  words.append({'text':' '+p,'startMs':round(t*1000),'endMs':round(end*1000),'timestampMs':round(t*1000),'confidence':None,'pageBreakAfter':i==len(parts)-1 and text.endswith(('.', '!', '?'))});t=end
 audit.append({'request':request,'sourceStart':a,'sourceEnd':b,'before':''.join(w['text'] for w in old),'after':text})
for w in words:
 old=w['text'];s=w['startMs']/1000
 replacements=[(r'\b(?:Puya|Pui|Pu)\b','Puy',11),(r'\bWaka BEM\b','WAKABEM',13),(r'\bIsha\b','Aisyah',17),(r'\bnyuntek-nyuntek\b','nyontek-nyontok',20),(r'\bPembara\b','Membara',27),(r'\bKabimnya\b','KABEM-nya',29),(r'\bAxeliano\b','Axellyano',30),(r'\blocker\b','loker',34),(r'\bjatahan\b','jatah',37),(r'\bJatanya\b','Jatuhnya',38),(r'\bnyurus\b','nyuruh',45),(r'\bmenjatuhnya\b','jatuhnya',47),(r'\bkesampaikan\b','kesampaian',48),(r'\bmabang-mabangnya\b','maba-mabanya',52),(r'\bPancangan\b','',53),(r'\bPendakparannya\b','Pendaftarannya',57),(r'\bTeknikan\b','Teknik',58),(r'\bPecatlor\b','pecah telor',59)]
 for pattern,value,number in replacements:
  if re.search(pattern,w['text'],re.I):w['text']=re.sub(pattern,value,w['text'],flags=re.I);audit.append({'request':number,'sourceStart':s,'before':old,'after':w['text']})
 if 13<=s<17:w['text']=re.sub(r'\bseri\b','sesi',w['text'],flags=re.I)
 if 135<=s<138:w['text']=re.sub(r'\bcepat\b','telat',w['text'],flags=re.I)
 if 46<=s<47:w['text']=re.sub(r'\btelah\b','kelas',w['text'],flags=re.I)
 if 311<=s<312:w['text']=re.sub(r'\busaha\b','usah',w['text'],flags=re.I)
 if 313<=s<315:w['text']=re.sub(r'\bnalirin\b','kenalin',w['text'],flags=re.I)
 if 338<=s<340:w['text']=re.sub(r'\bmood\b','menurut',w['text'],flags=re.I)
 if 444<=s<451:w['text']=re.sub(r'\bekstra\b','extrovert',w['text'],flags=re.I)
 if 470<=s<472:w['text']=re.sub(r'\bGita\b','gitu',w['text'],flags=re.I)
 if 474<=s<476:w['text']=re.sub(r'\bLen\b','Ler',w['text'],flags=re.I)
 if 720<=s<734:w['text']=re.sub(r'\bpagi\b','bagi',w['text'],flags=re.I)
 if 1069<=s<1071:w['text']=re.sub(r'\bgerakan\b','deg-degan',w['text'],flags=re.I)
 if 1075<=s<1079:w['text']=re.sub(r'\bbagnya\b','micnya',w['text'],flags=re.I)
 if 1110<=s<1114:w['text']=re.sub(r'\bDuan\b','26',w['text'],flags=re.I)
 if 1122<=s<1124:w['text']=re.sub(r'\bTentu\b','Betul',w['text'],flags=re.I)
 if 1115<=s<1120:w['text']=re.sub(r'\bPecat\b','Pecah',w['text'],flags=re.I)
 if 1055<=s<1058:w['text']=re.sub(r'\bPEPPER\b','PAPER',w['text'],flags=re.I)
phrase(95.11,96.72,'Siapa tuh WAKABEM-nya?',14)
phrase(97.35,98.15,'Kak Aisyah dong!',15)
phrase(206.70,207.70,'Diem-diem bae.',22)
phrase(228.68,230.12,'Takut, takut, adek takut.',23)
phrase(307.55,308.20,'',24)
phrase(405.42,406.27,'kita dari',31)
phrase(414.90,416.18,'Syukur alhamdulillah.',32)
phrase(925.93,931.25,'♪ Aku pernah di situ, di posisimu. ♪',43)
phrase(938.72,939.50,'Hal yang gue lakuin',44)
phrase(1005.63,1006.92,'Salting, salting.',46)
phrase(1068.94,1070.35,'Jujur, gue deg-degan parah.',49)
phrase(1114.20,1116.02,'',55)
phrase(1150.30,1151.40,'Angkatan Kinan',60)
# User expressly asks to leave genuinely unresolved speech uncaptained.
words=[w for w in words if w['text'].strip() and not re.search(r'\[(?:ucapan|nama) kurang jelas\]',w['text'])]
words.sort(key=lambda w:(w['startMs'],w['endMs']))
# Keep song-note symbols attached to their lyric text, never as an isolated page.
for index in range(len(words)-1,-1,-1):
 if words[index]['text'].strip()!='♪':continue
 if words[index]['startMs']<927000 and index+1<len(words):
  words[index+1]['text']=' ♪'+words[index+1]['text'];words[index+1]['startMs']=words[index]['startMs']
 elif index>0:
  words[index-1]['text']+=' ♪';words[index-1]['endMs']=words[index]['endMs'];words[index-1]['pageBreakAfter']=True
 words.pop(index)
# Ensure the comic "takut" response ends on its own subtitle page.
for w in words:
 if 229900<=w['startMs']<230120:w['pageBreakAfter']=True
pages=[];group=[]
def flush():
 if not group:return
 items=[dict(w) for w in group];items[0]['text']=' '+items[0]['text'].lstrip().lstrip('-')
 pages.append({'startMs':items[0]['startMs'],'endMs':max(items[-1]['endMs'],items[0]['startMs']+100),'words':items});group.clear()
for w in words:
 if group and (len(group)>=6 or len(''.join(x['text'] for x in group))+len(w['text'])>48 or w['startMs']-group[0]['startMs']>2800 or w['startMs']-group[-1]['endMs']>650):flush()
 group.append(w)
 if w.get('pageBreakAfter') or re.search(r'[.!?]$',w['text']):flush()
flush()
for i in range(len(pages)-1):pages[i]['endMs']=min(pages[i]['endMs'],pages[i+1]['startMs'])
for name,value in [('part1-captions-v3.json',words),('part1-pages-v3.json',pages)]:
 (root/'studio/src/data'/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
(root/'docs/revision-v3/caption-corrections.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
plan={'fps':30,'openingSeconds':22.6,'openingBumperSeconds':6,'openingTake':[32.8,49.4],'bodySpans':[[27.0,595.6],[607.1,842.0],[862.7,1161.6]],'bodyDissolveSeconds':0.2,'introDissolveSeconds':0.2,'outroSeconds':8,'images':{'aisyah':{'sourceStart':101.8,'duration':5.6},'paperMob':{'sourceStart':1089.4,'duration':8}},'quote':{'sourceStart':475.74,'duration':3.25,'text':'“Terbentur, terbentur, dan terbentuk.”'}}
plan['bodySeconds']=round(sum(e-s for s,e in plan['bodySpans'])-.2*(len(plan['bodySpans'])-1),6)
plan['durationSeconds']=round(plan['openingSeconds']+plan['bodySeconds']-plan['introDissolveSeconds']+plan['outroSeconds'],6)
(root/'docs/revision-v3/plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
print('Part 1 v3:',len(words),'words;',len(pages),'pages;',plan['durationSeconds'],'seconds. Part 2 data untouched.')
