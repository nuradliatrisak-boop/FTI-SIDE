"""Apply traceable spelling corrections; mark unresolved recognition explicitly."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
words=json.loads((root/'revisions/v1/captions-merged.json').read_text());changes=[]
fixes={
 'Campuradu':'Campuraduk','Campurado':'Campuraduk','menganggut':'mengganggu','kegetan':'kegiatan','Sofar':'so far','realitainya':'realitanya','realitinya':'realitanya','realitnya':'realitanya',
 'efektasi':'ekspektasi','hampiri':'hampir','Ternyatnya':'Ternyata','setiapa':'setiap','belaja':'belajar',
 'Sangkat':'Sangat','menyenangan':'menyenangkan','jujure':'jujur','lombah':'lomba','prioritosin':'prioritasin',
 'alhamdulllah':'alhamdulillah','Alhamdulilah':'Alhamdulillah','pihat':'pihak','Merek':'Mereka',
 'istirat':'istirahat','organisasasi':'organisasi','penasara':'penasaran','dimannya':'di mana',
 'Kanadya':'Kak Nadya','Kanadia':'Kak Nadya','menggivariel':'Ghivariel','mabak':'maba',
 'BEMFTI':'BEM FTI','WKBM':'Waka BEM','WKBN':'Waka BEM'
}
for w in words:
 old=w['text']
 for before,after in fixes.items():w['text']=re.sub(r'\b'+re.escape(before)+r'\b',after,w['text'],flags=re.I)
 if 1609000<=w['startMs']<1625000:w['text']=re.sub(r'\bseri\b','Sari',w['text'],flags=re.I)
 if 1684000<=w['startMs']<1702000:w['text']=re.sub(r'\brelator\b','realita',w['text'],flags=re.I)
 if 1788000<=w['startMs']<1793000:
  w['text']=re.sub(r'\bpro\b','proker',w['text'],flags=re.I)
  w['text']=re.sub(r'\bkadang\b','dan',w['text'],flags=re.I)
 if 1819000<=w['startMs']<1845000:w['text']=re.sub(r'\bmerasa\b','nguras',w['text'],flags=re.I)
 if 1819000<=w['startMs']<1869000:
  for before,after in [('istirahatan','istirahat'),('butut','butuh'),('butu','butuh'),('misakan','misalkan'),('terlep','terlelap')]:w['text']=re.sub(r'\b'+before+r'\b',after,w['text'],flags=re.I)
 if 1913000<=w['startMs']<1923000:
  w['text']=re.sub(r'\bMabani\b','maba nih',w['text'],flags=re.I)
  w['text']=re.sub(r'\bangkat\b','angkatan',w['text'],flags=re.I)
 if 1990000<=w['startMs']<2001000:w['text']=re.sub(r'\bWatchmen\b','which mean',w['text'],flags=re.I)
 if 2173000<=w['startMs']<2177000:w['text']=re.sub(r'\bAdept?\b','kadep',w['text'],flags=re.I)
 if 479000<=w['startMs']<485000:w['text']=re.sub(r'\b(terbentang|terbentar)\b','terbentak',w['text'],flags=re.I)
 if old!=w['text']:changes.append({'startMs':w['startMs'],'endMs':w['endMs'],'before':old,'after':w['text'],'basis':'spelling, confirmed names, established institution term or spot re-transcription'})
# Avoid assigning an unconfirmed name or meaningless ASR phrase to a speaker.
for begin,end,label in [(73540,75480,'[ucapan kurang jelas]'),(97350,98030,'[nama kurang jelas]')]:
 selected=[w for w in words if begin<=(w['startMs']+w['endMs'])/2<end]
 if not selected:continue
 old=''.join(w['text'] for w in selected)
 words=[w for w in words if w not in selected]
 words.append({'text':' '+label,'startMs':min(w['startMs'] for w in selected),'endMs':max(w['endMs'] for w in selected),'timestampMs':min(w['startMs'] for w in selected),'confidence':None})
 changes.append({'startMs':begin,'endMs':end,'before':old,'after':label,'basis':'remains unresolved after repeated recognition; no substitute words invented'})
# A high-confidence local pass recovered the previously missing follow/like/subscribe sign-off.
recovered=[]
for row in json.loads((root/'docs/subtitle-review/2240-2251.json').read_text()):
 for w in row['words']:
  if 2244.3<=w['start'] and w['end']<=2250.03:
   recovered.append({'text':w['word'],'startMs':round(w['start']*1000),'endMs':round(w['end']*1000),'timestampMs':round(w['start']*1000),'confidence':w['probability']})
words.extend(recovered)
changes.append({'startMs':2244300,'endMs':2250030,'before':'[ASR gap]','after':''.join(w['text'] for w in recovered),'basis':'recovered word-timed speech in targeted source re-transcription'})
words.sort(key=lambda w:(w['startMs'],w['endMs']))
(root/'docs/captions-merged.json').write_text(json.dumps(words,ensure_ascii=False,indent=2)+'\n')
(root/'docs/subtitle-review-corrections.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
print(len(changes),'documented spelling/unclear-speech corrections')
