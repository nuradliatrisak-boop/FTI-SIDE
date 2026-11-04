"""Build source-relative Caption pages and episode ASS from the reviewed ASR draft."""
import json,re,argparse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('captions');p.add_argument('--output',default='studio/src/data');a=p.parse_args()
words=json.loads(Path(a.captions).read_text())
replacements={r'\bNadia\b':'Nadya',r'\bGifariel\b':'Ghivariel',r'\bGivarel\b':'Ghivariel',r'\bGifarel\b':'Ghivariel',r'\bGivariel\b':'Ghivariel',r'\bGivarial\b':'Ghivariel',r'\bGifarial\b':'Ghivariel'}
for w in words:
 for pattern,value in replacements.items():w['text']=re.sub(pattern,value,w['text'],flags=re.I)
 if w['text'] and not w['text'].startswith(' '):w['text']=' '+w['text']
pages=[];current=[]
def flush():
 if not current:return
 items=[dict(x) for x in current]
 if items[0]['text'].lstrip().startswith('-'):items[0]['text']=' '+items[0]['text'].lstrip().lstrip('-')
 pages.append({'startMs':items[0]['startMs'],'endMs':max(items[-1]['endMs'],items[0]['startMs']+150),'words':items})
 current.clear()
for w in words:
 if w['endMs']<=w['startMs']:continue
 if current and (len(current)>=6 or len(''.join(x['text'] for x in current))+len(w['text'])>48 or w['startMs']-current[0]['startMs']>2800 or w['startMs']-current[-1]['endMs']>650):flush()
 current.append(w)
 if re.search(r'[.!?]$',w['text']):flush()
flush()
# End pages before the next starts: prevent competing subtitle events.
for i in range(len(pages)-1):pages[i]['endMs']=min(pages[i]['endMs'],pages[i+1]['startMs'])
root=Path(a.output);root.mkdir(parents=True,exist_ok=True)
(root/'captions.json').write_text(json.dumps(words,ensure_ascii=False,indent=2))
(root/'pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2))
print(len(words),'words;',len(pages),'pages')
