"""Original procedural instrumental ident; no samples or participant voices."""
import wave
from pathlib import Path
import numpy as np
sr=48000
duration=16
mix=np.zeros((sr*duration,2),dtype=np.float64)
rng=np.random.default_rng(2411)
def add(sound,start,level=.3,pan=0):
 i=round(start*sr); n=min(len(sound),len(mix)-i)
 if n<=0:return
 mix[i:i+n,0]+=sound[:n]*level*(1-pan*.4)
 mix[i:i+n,1]+=sound[:n]*level*(1+pan*.4)
def note(freq,dur,decay=5):
 t=np.arange(round(dur*sr))/sr
 env=np.minimum(t/.008,1)*np.exp(-decay*t)*np.minimum((dur-t)/.04,1)
 return (np.sin(2*np.pi*freq*t)+.2*np.sin(4*np.pi*freq*t))*env
for beat in range(32):
 start=beat*.5
 t=np.arange(round(.32*sr))/sr
 kick=np.sin(2*np.pi*(48*t+55*.025*(1-np.exp(-t/.025))))*np.exp(-t*17)
 add(kick,start,.28)
 if beat%2==1:
  t=np.arange(round(.16*sr))/sr
  add(rng.standard_normal(len(t))*np.exp(-t*35),start,.065)
 for eighth in [0,.25]:
  t=np.arange(round(.06*sr))/sr
  noise=rng.standard_normal(len(t)); noise=np.diff(noise,prepend=0)
  add(noise*np.exp(-t*95),start+eighth,.025,(-1 if eighth else 1)*.7)
 root=[130.8128,103.8262,155.5635,116.5409][beat//8]
 add(note(root/2,.45,6),start,.18)
 if beat%2==0:
  for semitone in [0,3,7,10]:
   add(note(root*2**(semitone/12),.65,5),start,.045,(-1 if semitone%2 else 1)*.4)
 melody=[0,7,10,12,7,3,10,7]
 add(note(root*2**(melody[beat%8]/12)*2,.23,10),start+.25,.07,(-1 if beat%2 else 1)*.5)
fade=np.minimum(np.arange(len(mix))/sr/.04,1)*np.minimum((len(mix)-np.arange(len(mix)))/sr/1.2,1)
mix*=fade[:,None]
mix=np.tanh(mix*1.15)
mix*=.78/max(np.max(np.abs(mix)),.01)
p=Path('studio/public/audio');p.mkdir(parents=True,exist_ok=True)
with wave.open(str(p/'fti-side-ident-original.wav'),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(sr);f.writeframes((mix*32767).astype('<i2').tobytes())
print('Original instrumental ident written, 16s, stereo 48kHz')
