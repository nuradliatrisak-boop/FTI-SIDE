"""Extract short episode previews from the completed final exports."""
import argparse,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--part',type=int,choices=[1,2],required=True);a=p.parse_args();n=a.part
file=root/f'deliverables/FTI-SIDE-PART-{n}.mp4'
end=1178.3 if n==1 else 1111.7;tail=12 if n==1 else 7
filters='[0:v:0]setpts=PTS-STARTPTS[v0];[0:a:0]asetpts=PTS-STARTPTS[a0];[1:v:0]setpts=PTS-STARTPTS[v1];[1:a:0]asetpts=PTS-STARTPTS[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]'
with (root/f'docs/preview-{n}-refresh.log').open('w') as log:
 subprocess.run(['ffmpeg','-nostdin','-hide_banner','-y','-t','110','-i',str(file),'-ss',str(end-tail),'-t',str(tail),'-i',str(file),'-filter_complex_threads','1','-filter_complex',filters,'-map','[v]','-map','[a]','-c:v','libx264','-preset','veryfast','-crf','20','-threads','2','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',str(root/f'deliverables/FTI-SIDE-PART-{n}-PREVIEW.mp4')],stdout=log,stderr=subprocess.STDOUT,check=True)
print('Updated preview',n,flush=True)
