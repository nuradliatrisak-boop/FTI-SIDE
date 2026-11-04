"""Check revised export metadata, speech timing and unchanged Part 2."""
import json, subprocess, hashlib
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[1]
plan=json.loads((root/'docs/revision-v4/plan.json').read_text())
video=root/'deliverables/FTI-SIDE-PART-1-V4.mp4'
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
def read(p,t):
 b=subprocess.check_output(['ffmpeg','-v','error','-ss',str(t),'-i',str(p),'-t','4','-vn','-ac','1','-ar','16000','-f','f32le','-']);x=np.frombuffer(b,dtype='<f4').astype(float);return x-x.mean()
meta=probe(video);v=next(s for s in meta['streams'] if s['codec_type']=='video');a=next(s for s in meta['streams'] if s['codec_type']=='audio')
assert (v['width'],v['height'],v['codec_name'],v['nb_frames'])==(1920,1080,'h264','33972'),v
assert abs(float(meta['format']['duration'])-1132.4)<.1
assert a['channels']==2 and a['codec_name']=='aac'
checks=[]
for t in [60,200,600,750,850,1100]:
 cursor=22.4
 for start,end in plan['bodySpans']:
  if cursor<=t<cursor+end-start:source=start+t-cursor;break
  cursor+=end-start-.2
 x=read(root/'studio/public/audio/podcast-normalized.m4a',source);y=read(video,t);n=min(len(x),len(y));x=x[:n];y=y[:n];size=1<<(2*n-1).bit_length();corr=np.fft.irfft(np.fft.rfft(y,size)*np.conj(np.fft.rfft(x,size)),size);lags=np.arange(-2400,2401);scores=corr[lags%size]/(np.linalg.norm(x)*np.linalg.norm(y));k=int(np.argmax(scores));lag=float(lags[k]/16000);score=float(scores[k]);assert abs(lag)<.1 and score>.9,(t,lag,score);checks.append(dict(timeline=t,source=source,lag=lag,correlation=score));print(checks[-1],flush=True)
story=probe(root/'renders/part1-story-v4.mp4');sv=next(s for s in story['streams'] if s['codec_type']=='video');assert (sv['width'],sv['height'],sv['nb_frames'])==(1080,1920,'900')
part2=root/'deliverables/FTI-SIDE-PART-2.mp4'
h=hashlib.sha256()
with part2.open('rb') as f:
 for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
pointer=subprocess.check_output(['git','show','HEAD:deliverables/FTI-SIDE-PART-2.mp4'],cwd=root,text=True)
assert h.hexdigest() in pointer
result={'result':'passed','part1':{'duration':float(meta['format']['duration']),'frames':v['nb_frames'],'audioAlignment':checks},'story':{'duration':story['format']['duration'],'width':1080,'height':1920},'part2':{'sha256':h.hexdigest(),'matchesPreviousCommit':True}}
(root/'deliverables/PART-1-V4-QC.json').write_text(json.dumps(result,indent=2)+'\n')
