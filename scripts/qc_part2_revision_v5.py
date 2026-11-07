"""Verify Part 2 timing, picture/audio formats and preservation of approved Part 1."""
from pathlib import Path
import json,subprocess,hashlib
import numpy as np
r=Path(__file__).resolve().parents[1];plan=json.load(open(r/'docs/part2-revision-v5/plan.json'))
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]))
def audio(p,t):
 b=subprocess.check_output(['ffmpeg','-v','error','-ss',str(t),'-i',str(p),'-t','4','-vn','-ac','1','-ar','16000','-f','f32le','-']);x=np.frombuffer(b,dtype='<f4').astype(float);return x-x.mean()
video=r/'deliverables/FTI-SIDE-PART-2-V5.mp4';m=probe(video);v=next(x for x in m['streams'] if x['codec_type']=='video');a=next(x for x in m['streams'] if x['codec_type']=='audio')
assert (v['width'],v['height'],v['nb_frames'],v['codec_name'],a['codec_name'],a['channels'])==(1920,1080,str(plan['frames']),'h264','aac',2)
assert abs(float(m['format']['duration'])-plan['durationSeconds'])<.1
checks=[]
for t in [60,300,520,760,1000,1080]:
 source=1161.6+t-19.8 if t<731.6 else 1907.2+t-731.6
 x=audio(r/'studio/public/audio/podcast-part2-enhanced.m4a',source);y=audio(video,t);n=min(len(x),len(y));x=x[:n];y=y[:n];size=1<<(2*n-1).bit_length();corr=np.fft.irfft(np.fft.rfft(y,size)*np.conj(np.fft.rfft(x,size)),size);lags=np.arange(-2400,2401);scores=corr[lags%size]/(np.linalg.norm(x)*np.linalg.norm(y));k=int(np.argmax(scores));lag=float(lags[k]/16000);score=float(scores[k]);assert abs(lag)<.1 and score>.90,(t,lag,score);checks.append(dict(timeline=t,source=source,lag=lag,correlation=score));print(checks[-1],flush=True)
story_file=r/'renders/part2-story-v5.mp4'
expected_story_frames=810
story=probe(story_file);sv=next(x for x in story['streams'] if x['codec_type']=='video');assert(sv['width'],sv['height'],sv['nb_frames'])==(1080,1920,str(expected_story_frames))
h=hashlib.sha256()
with (r/'deliverables/FTI-SIDE-PART-1.mp4').open('rb') as f:
 for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
assert h.hexdigest() in subprocess.check_output(['git','show','HEAD:deliverables/FTI-SIDE-PART-1.mp4'],cwd=r,text=True)
report={'result':'passed','part2':{'durationSeconds':float(m['format']['duration']),'frames':int(v['nb_frames']),'size':[1920,1080],'audioAlignment':checks},'story':{'durationSeconds':float(story['format']['duration']),'frames':expected_story_frames,'size':[1080,1920]},'part1Preserved':{'sha256':h.hexdigest(),'matchesPreviousCommit':True}}
(r/'deliverables/PART-2-V5-QC.json').write_text(json.dumps(report,indent=2)+'\n')
