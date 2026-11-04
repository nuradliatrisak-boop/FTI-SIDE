"""Compare encoded speech windows against the normalized source across edits."""
import json,subprocess
from pathlib import Path
import numpy as np
root=Path(__file__).resolve().parents[1]
plan=json.loads((root/'docs/edit-plan.json').read_text())
def read_audio(file,time):
 data=subprocess.check_output(['ffmpeg','-nostdin','-v','error','-ss',str(time),'-i',str(file),'-t','4','-vn','-ac','1','-ar','16000','-f','f32le','-'])
 x=np.frombuffer(data,dtype='<f4').astype(np.float64);return x-x.mean()
checks=[]
for ep in plan['episodes']:
 part=ep['part']
 for timeline in ([60,620,1100] if part==1 else [60,740,1050]):
  remaining=timeline-20
  for begin,end in ep['spans']:
   if remaining<end-begin:source=begin+remaining;break
   remaining-=end-begin
  x=read_audio(root/'studio/public/audio/podcast-normalized.m4a',source)
  y=read_audio(root/f'deliverables/FTI-SIDE-PART-{part}.mp4',timeline)
  count=min(len(x),len(y));x=x[:count];y=y[:count]
  n=1<<((2*count-1).bit_length())
  corr=np.fft.irfft(np.fft.rfft(y,n)*np.conj(np.fft.rfft(x,n)),n)
  radius=2400;lags=np.arange(-radius,radius+1)
  scores=corr[lags%n]/(np.linalg.norm(x)*np.linalg.norm(y)+1e-12)
  best=int(np.argmax(scores));lag=lags[best]/16000;score=float(scores[best])
  assert abs(lag)<.1 and score>.9,(part,timeline,lag,score)
  checks.append({'part':part,'timelineSeconds':timeline,'sourceSeconds':round(source,4),'audioLagSeconds':round(float(lag),6),'correlation':round(score,5),'result':'passed'})
  print(part,timeline,'lag',round(lag,5),'correlation',round(score,5),flush=True)
(root/'deliverables/AUDIO-ALIGNMENT-QC.json').write_text(json.dumps(checks,indent=2)+'\n')
