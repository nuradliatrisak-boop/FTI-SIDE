"""Original 126-BPM funk/pop instrumental, ducked under real participant speech."""
from pathlib import Path
import numpy as np,wave
sr=48000;dur=36;beat=60/126;rng=np.random.default_rng(1262026);mix=np.zeros((round(dur*sr),2),np.float64)
def add(x,start,gain=1,pan=0):
 at=round(start*sr);n=min(len(x),len(mix)-at)
 if at<0 or n<=0:return
 mix[at:at+n,0]+=x[:n]*gain*(1-.35*pan);mix[at:at+n,1]+=x[:n]*gain*(1+.35*pan)
def tone(freq,length,kind='pluck'):
 t=np.arange(round(length*sr))/sr
 if kind=='bass':x=np.sin(2*np.pi*freq*t)+.30*np.sin(4*np.pi*freq*t)+.12*np.sin(6*np.pi*freq*t);env=(1-np.exp(-t*170))*np.exp(-t*5)*np.minimum((length-t)/.025,1)
 elif kind=='brass':x=np.sin(2*np.pi*freq*t)+.36*np.sin(4*np.pi*freq*t)+.12*np.sin(6*np.pi*freq*t);env=(1-np.exp(-t*90))*np.exp(-t*5)*np.minimum((length-t)/.05,1)
 else:x=np.sin(2*np.pi*freq*t)+.25*np.sin(2*np.pi*freq*2.003*t);env=np.minimum(t/.004,1)*np.exp(-t*12)*np.minimum((length-t)/.03,1)
 return x*env
for b in range(int(dur/beat)):
 start=b*beat;bar=b//4;root=[65.4064,51.9131,58.2705,65.4064][bar%4]
 if b%4 in [0,2] or (bar%2 and b%4==3):
  t=np.arange(round(.30*sr))/sr;x=np.sin(2*np.pi*(46*t+60*.022*(1-np.exp(-t/.022))))*np.exp(-t*20);x+=rng.standard_normal(len(t))*.035*np.exp(-t*150);add(x,start,.38)
 if b%4 in [1,3]:
  t=np.arange(round(.20*sr))/sr;noise=rng.standard_normal(len(t));hi=np.diff(noise,prepend=0);x=hi*np.exp(-t*33)*.35+np.sin(2*np.pi*185*t)*np.exp(-t*24)*.22;add(x,start,.16)
  for delay in [0,.012,.025]:add(rng.standard_normal(round(.045*sr))*np.exp(-np.arange(round(.045*sr))/sr*65),start+delay,.035,delay*16-.2)
 for k in [0,.5]:
  t=np.arange(round(.05*sr))/sr;noise=rng.standard_normal(len(t));add(np.diff(noise,prepend=0)*np.exp(-t*110),start+k*beat,.022,(-.7 if k else .7))
 if b%4 in [0,2,3]:add(tone(root*(2 if b%4==3 else 1),.27,'bass'),start,.24)
 if b%4==1:add(tone(root,.18,'bass'),start+.5*beat,.22)
 if b%4 in [0,3]:
  for semitone in [0,3,7,10]:add(tone(root*4*2**(semitone/12),.27,'brass'),start+.25*beat,.037,(-.6 if semitone%2 else .6))
 if b%2==0:
  add(tone(root*4*2**([0,7,10,12][(b//2)%4]/12),.23),start+.5*beat,.075,(-.5 if b%4 else .5))
# Short fills, risers and reverse splashes reinforce cuts without meme-like effects.
for start in [5.45,13.8,17.8,21.7,29.5,34.7]:
 n=round(.38*sr);t=np.arange(n)/sr;noise=rng.standard_normal(n);x=np.diff(noise,prepend=0)*np.sin(np.pi*t/.38)**2*.045;add(x,start,.4)
for b in [11,27,43,59]:
 for k in range(4):add(tone(260+80*k,.075),b*beat+k*beat/4,.045,(-.4 if k%2 else .4))
fade=np.minimum(np.arange(len(mix))/sr/.015,1)*np.minimum((len(mix)-np.arange(len(mix)))/sr/.7,1)
mix=np.tanh(mix*.95)*fade[:,None];mix*=.86/max(abs(mix).max(),1e-9)
out=Path('studio/public/audio');out.mkdir(exist_ok=True,parents=True)
def write(name,arr):
 with wave.open(str(out/name),'wb') as f:f.setnchannels(2);f.setsampwidth(2);f.setframerate(sr);f.writeframes((arr*32767).astype('<i2').tobytes())
write('part1-v3-groove.wav',mix)
# Original short transition accents, no samples and no imitated voices.
n=round(.28*sr);t=np.arange(n)/sr;pop=(np.sin(2*np.pi*(780*t-900*t*t))*np.exp(-t*32)+rng.standard_normal(n)*np.exp(-t*95)*.13)*.3
write('part1-v3-pop.wav',np.stack([pop,pop],1))
n=round(.65*sr);t=np.arange(n)/sr;sweep=rng.standard_normal(n);sweep=np.diff(sweep,prepend=0)*np.sin(np.pi*t/.65)**2*.08
write('part1-v3-sweep.wav',np.stack([sweep,sweep*.9],1))
x=np.zeros(round(1.1*sr))
for i,freq in enumerate([523.25,659.25,783.99]):
 y=tone(freq,.4);at=round(i*.18*sr);x[at:at+len(y)]+=.1*y
write('part1-v3-three-notes.wav',np.stack([x,x],1))
print('New original groove and 3 short SFX generated')
