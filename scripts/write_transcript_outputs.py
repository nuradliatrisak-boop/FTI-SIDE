"""Write editable transcript and SRTs from source-relative Caption JSON and EDL."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
words=json.loads((root/'docs/captions-merged.json').read_text())
pages=json.loads((root/'studio/src/data/pages.json').read_text())
plan=json.loads((root/'docs/edit-plan.json').read_text())
def ts(ms):
 ms=round(ms);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
def srt(cues):return '\n'.join(f"{i}\n{ts(s)} --> {ts(e)}\n{t.strip()}\n" for i,(s,e,t) in enumerate(cues,1))
(root/'deliverables/TRANSKRIP-SUMBER.srt').write_text(srt([(p['startMs'],p['endMs'],''.join(x['text'] for x in p['words'])) for p in pages]))
for ep in plan['episodes']:
 cues=[];offset=20000
 for begin,end in ep['spans']:
  for p in pages:
   st=max(p['startMs'],begin*1000);en=min(p['endMs'],end*1000)
   if en>st:cues.append((offset+st-begin*1000,offset+en-begin*1000,''.join(x['text'] for x in p['words'])))
  offset+=(end-begin)*1000
 (root/f"deliverables/FTI-SIDE-PART-{ep['part']}.srt").write_text(srt(cues))
lines=[];group=[]
for w in words:
 group.append(w)
 if w['text'].strip().endswith(('.', '!', '?')) or len(group)>=40 or w['endMs']-group[0]['startMs']>15000:
  lines.append(f"[{ts(group[0]['startMs']).replace(',', '.')} – {ts(group[-1]['endMs']).replace(',', '.')}] {''.join(x['text'] for x in group).strip()}");group=[]
if group:lines.append(f"[{ts(group[0]['startMs'])}] {''.join(x['text'] for x in group).strip()}")
(root/'deliverables/TRANSKRIP-LENGKAP.txt').write_text('FTI SIDE — Transkrip sumber utuh dengan timestamp sumber\nNama dikonfirmasi: Nadya, Ghivariel, Kinan, Cahaya.\nTranskripsi otomatis dengan pemeriksaan ulang bagian tertentu; penanda ucapan kurang jelas dipertahankan.\n\n'+'\n\n'.join(lines)+'\n')
print('Transcript and SRT files written')
