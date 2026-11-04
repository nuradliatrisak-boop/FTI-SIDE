"""Inspect actual exported MP4s and decode all video/audio, then write a report."""
import argparse,hashlib,json,subprocess,fcntl
from pathlib import Path
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--part',type=int,choices=[1,2]);args=parser.parse_args()
report_file=root/'deliverables/QC-REPORT.json'
outputs=[]
for part,seconds,frames in [(1,1178.3,35349),(2,1111.7,33351)]:
 if args.part and part!=args.part:continue
 file=root/f'deliverables/FTI-SIDE-PART-{part}.mp4'
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(file)]))
 video=next(x for x in probe['streams'] if x['codec_type']=='video')
 audio=next(x for x in probe['streams'] if x['codec_type']=='audio')
 assert video['codec_name']=='h264' and (video['width'],video['height'])==(1920,1080)
 assert video['r_frame_rate']=='30/1' and video['pix_fmt']=='yuv420p'
 assert audio['codec_name']=='aac' and audio['channels']==2 and audio['sample_rate']=='48000'
 assert abs(float(probe['format']['duration'])-seconds)<.12,(file,probe['format']['duration'],seconds)
 assert int(video['nb_frames'])==frames,(file,video['nb_frames'],frames)
 with (root/f'docs/final-{part}-decode.log').open('w') as log:
  subprocess.run(['ffmpeg','-nostdin','-v','error','-xerror','-threads','1','-i',str(file),'-map','0:v:0','-map','0:a:0','-f','null','-'],stdout=log,stderr=subprocess.STDOUT,check=True)
 outputs=[r for r in outputs if r['file']!=str(file)]
 outputs.append({'file':str(file),'sizeBytes':file.stat().st_size,'durationSeconds':float(probe['format']['duration']),'videoFrames':int(video['nb_frames']),'width':1920,'height':1080,'videoCodec':'h264','fps':30,'pixelFormat':video['pix_fmt'],'audioCodec':'aac','audioChannels':2,'audioSampleRate':48000,'fullAudioVideoDecode':'passed','sha256':hashlib.file_digest(file.open('rb'),'sha256').hexdigest()})
 print('VERIFIED',file.name,flush=True)
 with (root/'docs/qc-report.lock').open('a') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX)
  previous=json.loads(report_file.read_text())['outputs'] if report_file.exists() else []
  merged={r['file']:r for r in previous}
  merged.update({r['file']:r for r in outputs})
  payload={'outputs':list(merged.values()),'subtitleLanguageReview':'ASR with 27 targeted re-transcriptions and documented spelling/name/formatting corrections; full human linguistic review not performed','unclearSpeechMarkers':['[ucapan kurang jelas]','[nama kurang jelas]']}
  temporary=report_file.with_suffix('.tmp')
  temporary.write_text(json.dumps(payload,indent=2)+'\n')
  temporary.replace(report_file)
  fcntl.flock(lock,fcntl.LOCK_UN)
