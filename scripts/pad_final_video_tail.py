"""Fill the source's short video tail while keeping all existing speech packets."""
import json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1];work=root/'renders'
manifest=work/'concat-2.txt';lines=manifest.read_text().splitlines()
body=Path(lines[4][6:-1]);expected=32541
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(body)]))
video=next(s for s in probe['streams'] if s['codec_type']=='video');missing=expected-int(video['nb_frames'])
assert 0<missing<=6,missing
print('Padding',missing,'frames due to source video ending before audio',flush=True)
def run(args):
 subprocess.run(['ffmpeg','-nostdin','-v','error','-y']+args,check=True,cwd=root)
last=work/'last-source-frame.png'
run(['-sseof','-0.2','-i',str(body),'-an','-fps_mode','passthrough','-update','1',str(last)])
pad=work/'source-tail-hold.mp4'
run(['-loop','1','-i',str(last),'-t',str(missing/30),'-r','30','-vf','scale=in_range=full:out_range=tv:out_color_matrix=bt709,format=yuv420p','-c:v','libx264','-preset','veryfast','-crf','18','-threads','1','-profile:v','high','-level:v','4.1','-video_track_timescale','90000','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709',str(pad)])
vonly=work/'part-2-video-only.mp4'
run(['-i',str(body),'-map','0:v:0','-an','-c:v','copy',str(vonly)])
vm=work/'pad-video-concat.txt';vm.write_text(f"file '{vonly}'\nfile '{pad}'\n")
paddedv=work/'part-2-padded-video.mp4'
run(['-f','concat','-safe','0','-i',str(vm),'-an','-c:v','copy',str(paddedv)])
paddedbody=work/'part-2-body-padded.mp4'
run(['-i',str(paddedv),'-i',str(body),'-map','0:v:0','-map','1:a:0','-c','copy',str(paddedbody)])
check=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(paddedbody)]))
assert int(next(s for s in check['streams'] if s['codec_type']=='video')['nb_frames'])==expected
lines[4]=f"file '{paddedbody}'";manifest.write_text('\n'.join(lines)+'\n')
temp=root/'deliverables/FTI-SIDE-PART-2.fixed.mp4'
run(['-f','concat','-safe','0','-i',str(manifest),'-c','copy','-movflags','+faststart',str(temp)])
temp.replace(root/'deliverables/FTI-SIDE-PART-2.mp4')
print('Tail fixed; all conversation audio preserved',flush=True)
