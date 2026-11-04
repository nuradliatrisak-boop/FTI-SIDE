"""Join ASR-split written words without inventing speech or moving timestamps."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'docs/captions-merged.json'
original=json.loads(p.read_text());out=[];changes=[]
for item in original:
 w=dict(item);text=w['text'].strip()
 previous=out[-1]['text'].rstrip() if out else ''
 if out and previous.strip().lower()=='or' and re.fullmatch(r'mawah[.,!?]?',text,re.I):
  old=out[-1]['text'];out[-1]['text']=' Ormawa'+(text[-1] if text[-1] in '.,!?' else '');out[-1]['endMs']=max(out[-1]['endMs'],w['endMs']);changes.append({'startMs':out[-1]['startMs'],'before':old+' '+text,'after':out[-1]['text'],'reason':'consistent spelling of Ormawa'});continue
 is_suffix=bool(re.match(r'^-[\w]',text))
 is_decimal=bool(re.match(r'^\.\d',text)) and bool(re.search(r'\d$',previous))
 is_abbreviation=bool(re.match(r'^\.[A-Z](?:\.|$)',text)) and bool(re.search(r'[A-Z]$',previous))
 if out and (is_suffix or is_decimal or is_abbreviation) and previous and not previous.endswith((',', '!', '?')):
  old=out[-1]['text'];out[-1]['text']=previous+text;out[-1]['endMs']=max(out[-1]['endMs'],w['endMs'])
  changes.append({'startMs':out[-1]['startMs'],'before':old+' '+text,'after':out[-1]['text'],'reason':'written-word/number formatting only'})
 else:out.append(w)
p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(root/'docs/subtitle-formatting-corrections.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
print('Formatting corrections:',len(changes),'words retained:',len(out))
