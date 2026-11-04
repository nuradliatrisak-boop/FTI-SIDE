"""Merge complete ASR, targeted checks, and confirmed name/spelling corrections."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
read=lambda p:json.loads((root/p).read_text())
rows=read('docs/transcription-turbo/segments.draft.json')
def words(rows):return [dict(w) for r in rows for w in r['words']]
w=words(rows)
def replace(begin,end,replacements):
 global w
 w=[x for x in w if not begin<=(x['start']+x['end'])/2<end]+[x for x in words(replacements) if begin<=(x['start']+x['end'])/2<end]
replace(0,27,read('docs/turbo-intro-check.json'))
repairs=read('docs/transcript-repairs.json')
replace(230,262,repairs);replace(430,480,repairs)
if (root/'docs/gap-check.json').exists():replace(845,884,read('docs/gap-check.json'))
w.sort(key=lambda x:(x['start'],x['end']))
# Proper names supplied by the user and established institutional spellings.
fixes={r'\bNadia\b':'Nadya',r'\b(?:Ghivaryel|Givaryel|Givariiel|Givariel|Gifariel|Gifarel|Givarel)\b':'Ghivariel',r'\bCahayya\b':'Cahaya',r'\bEngologi\b':'Teknologi',r'\bMasiswa\b':'Mahasiswa',r'\bOrmawah\b':'Ormawa',r'\b(?:ekspektasyi|ekspektase)\b':'ekspektasi',r'\b(?:lancart|lancor)\b':'lancar',r'\b(?:prokora|prokur|broker)\b':'proker',r'\bakademick\b':'akademik',r'\bmatkur\b':'matkul',r'\bmabah\b':'maba',r'\bmababa\b':'maba',r'\b(?:mulangkan|mengulangkan)\b':'meluangkan',r'\bbercentrama\b':'bercengkerama',r'\bbensi\b':'bensin',r'\b24h\b':'24 hours'}
corrections=[]
for x in w:
 old=x['word']
 for pattern,new in fixes.items():x['word']=re.sub(pattern,new,x['word'],flags=re.I)
 if 1640<x['start']<1700 and x['word'].strip().lower() in ['vision','design']:x['word']=' decision'
 if x['word']!=old:corrections.append({'startSeconds':x['start'],'before':old,'after':x['word'],'reason':'confirmed names, spelling or corroborated terminology'})
 # An ambiguous phrase remained inconsistent across recognition passes. Label it.
 if 444<x['start']<451 and re.search(r'bentok|teluk|telek',x['word'],re.I):
  x['word']=' [ucapan kurang jelas]' if 'bentok' in x['word'].lower() else ''
words_out=[]
for x in w:
 if not x['word'].strip():continue
 words_out.append({'text':' '+x['word'].strip(),'startMs':round(x['start']*1000),'endMs':round(max(x['end'],x['start']+.02)*1000),'timestampMs':round(x['start']*1000),'confidence':x['probability']})
(root/'docs/captions-merged.json').write_text(json.dumps(words_out,ensure_ascii=False,indent=2))
(root/'docs/transcript-corrections.json').write_text(json.dumps(corrections,ensure_ascii=False,indent=2))
print('Merged',len(words_out),'words;',len(corrections),'documented corrections')
