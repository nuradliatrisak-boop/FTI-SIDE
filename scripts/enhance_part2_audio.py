"""Make a separate level-balanced dialog master; preserve the source time axis."""
from pathlib import Path
import subprocess
r=Path(__file__).resolve().parents[1]
filters='highpass=f=70,equalizer=f=2700:t=q:w=1:g=1.5,acompressor=threshold=0.12:ratio=2:attack=10:release=200:makeup=1.2,dynaudnorm=f=400:g=15:p=0.9:m=2:r=0.13:n=false:c=true,loudnorm=I=-16:TP=-1.5:LRA=8:print_format=json'
subprocess.run(['ffmpeg','-nostdin','-hide_banner','-y','-i',str(r/'studio/public/audio/podcast-normalized.m4a'),'-af',filters,'-c:a','aac','-b:a','256k','-ar','48000','-ac','2',str(r/'studio/public/audio/podcast-part2-enhanced.m4a')],check=True)
