"""Recheck selected unclear speech windows, retaining source timestamps."""
import json
from pathlib import Path
from faster_whisper import WhisperModel
root=Path(__file__).resolve().parents[1]
ranges=[(43,49),(70,81),(83,100),(130,153),(205,211),(306,317),(333,344),(433,452),(479,485),(520,529),(625,634),(695,705),(737,746),(1480,1491),(1502,1516),(1570,1585),(1609,1625),(1684,1702),(1785,1793),(1819,1845),(1851,1869),(1913,1923),(1954,1966),(1990,2001),(2052,2066),(2172,2181),(2240,2251)]
out=root/'docs/subtitle-review';out.mkdir(exist_ok=True)
model=WhisperModel(str(root/'models/large-v3-turbo'),device='cpu',compute_type='int8',cpu_threads=4)
for begin,end in ranges:
 target=out/f'{begin}-{end}.json'
 if target.exists():continue
 segments,info=model.transcribe(str(root/'docs/podcast-mono16k.wav'),language='id',word_timestamps=True,clip_timestamps=f'{begin},{end}',condition_on_previous_text=False,initial_prompt='FTI SIDE. BEM FTI Universitas Trisakti. Nadya, Ghivariel, Kinan, Cahaya.',beam_size=5)
 rows=[]
 for x in segments:
  rows.append({'start':x.start,'end':x.end,'text':x.text,'words':[{'word':w.word,'start':w.start,'end':w.end,'probability':w.probability} for w in x.words]})
 target.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
 print(begin,end,' '.join(x['text'] for x in rows),flush=True)
