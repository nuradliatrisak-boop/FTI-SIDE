"""Encode clean podcast sections from the same source captions and EDL as Remotion.
Motion graphics are rendered by Remotion; FFmpeg handles subtitle burn-in, video
encoding and final muxing without re-rendering unchanged frames in Chromium.
"""
import argparse,json,re,subprocess,uuid
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--preview',action='store_true');p.add_argument('--part',type=int,choices=[1,2]);a=p.parse_args()
out=root/'deliverables';work=root/'renders';work.mkdir(exist_ok=True)
run_id=uuid.uuid4().hex[:8]
pages=json.loads((root/'studio/src/data/pages.json').read_text())
plan=json.loads((root/'docs/edit-plan.json').read_text())
def run(args,log):
 with (root/'docs'/log).open('w') as f:
  subprocess.run(args,cwd=root,stdout=f,stderr=subprocess.STDOUT,check=True)
def stamp(seconds):
 cs=round(seconds*100);return f'{cs//360000}:{cs//6000%60:02}:{cs//100%60:02}.{cs%100:02}'
def esc(text):return text.replace('\\','\\\\').replace('{','\\{').replace('}','\\}').replace('\n',' ')
header='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,DejaVu Sans,44,&H00FFFFFF,&H00FFFFFF,&H29211405,&H29211405,-1,0,0,0,100,100,0,0,3,12,0,2,210,210,75,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
for ep in plan['episodes']:
 if a.part and ep['part']!=a.part:continue
 n=ep['part'];spans=ep['spans'];start=spans[0][0]
 if a.preview:
  remaining=90;selected=[]
  for begin,end in spans:
   length=min(end-begin,remaining)
   if length>0:selected.append([begin,begin+length]);remaining-=length
  spans=selected
 duration=round(sum(end-begin for begin,end in spans)*30)/30
 ass=work/f'part-{n}.ass';events=[]
 timeline_offset=0
 for begin,end in spans:
  for page in pages:
   st=max(page['startMs']/1000,begin);en=min(page['endMs']/1000,end)
   if en<=st:continue
   text=''
   for w in page['words']:
    value=esc(w['text'])
    if re.fullmatch(r'(FTI|SIDE|BEM|ARKA|waktu|organisasi|akademik|kepemimpinan)[.,!?]?',w['text'].strip(),re.I):value='{\\c&H0070ADFF&}'+value+'{\\c&H00FFFFFF&}'
    text+=value
   events.append(f'Dialogue: 0,{stamp(st-begin+timeline_offset)},{stamp(en-begin+timeline_offset)},Default,,0,0,0,,{{\\fad(65,0)}}{text.strip()}')
  timeline_offset+=end-begin
 ass.write_text(header+'\n'.join(events)+'\n')
 body=work/f'part-{n}-body-{run_id}.mp4'
 if a.preview:body=work/f'part-{n}-body-preview-{run_id}.mp4'
 print('ENCODING',n,'duration',duration,flush=True)
 vf=f"fps=30,subtitles=filename='{ass.relative_to(root)}',drawbox=x=98:y=65:w=285:h=58:color=0x092a49@0.88:t=fill,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='FTI SIDE  /  {n}':x=116:y=81:fontsize=25:fontcolor=white"
 count=len(spans)
 filters=[]
 filters.append('[0:v:0]split='+str(count)+''.join(f'[vs{i}]' for i in range(count)))
 filters.append('[1:a:0]asplit='+str(count)+''.join(f'[as{i}]' for i in range(count)))
 for i,(begin,end) in enumerate(spans):
  filters.append(f'[vs{i}]tpad=stop_mode=clone:stop_duration=0.2,trim=start={begin-start}:end={end-start},setpts=PTS-STARTPTS[v{i}]')
  filters.append(f'[as{i}]atrim=start={begin-start}:end={end-start},asetpts=PTS-STARTPTS[a{i}]')
 filters.append(''.join(f'[v{i}][a{i}]' for i in range(count))+f'concat=n={count}:v=1:a=1[bodyv][bodya]')
 filters.append('[bodyv]'+vf+'[vout]')
 run(['ffmpeg','-nostdin','-hide_banner','-nostats','-progress',str(work/f'part-{n}-progress.txt'),'-y','-ss',str(start),'-i','studio/public/sources/podcast.mp4','-ss',str(start),'-i','studio/public/audio/podcast-normalized.m4a','-filter_complex_threads','2','-filter_complex',';'.join(filters),'-map','[vout]','-map','[bodya]','-t',str(duration),'-c:v','libx264','-preset','veryfast','-crf','18','-threads','3','-pix_fmt','yuv420p','-video_track_timescale','90000','-profile:v','high','-level:v','4.1','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-movflags','+faststart',str(body)],f'body-{n}'+('-preview' if a.preview else '')+'-encode.log')
 # Normalize graphics to the same color range, timebase, and stereo audio as the body.
 specs=[('FTI-SIDE-OPENING-PREVIEW',16), (f'PART-{n}-CARD',4), ('FTI-SIDE-CLOSING',7)]
 if n==1:specs.append(('NEXT-EPISODE',5))
 for name,seconds in specs:
  target=work/(name+'-normalized.mp4')
  if target.exists():continue
  source=out/(name+'.mp4')
  probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(source)]))
  has_audio=any(x['codec_type']=='audio' for x in probe['streams'])
  args=['ffmpeg','-nostdin','-hide_banner','-y','-i',str(source)]
  if not has_audio:args+=['-f','lavfi','-i','anullsrc=r=48000:cl=stereo']
  args+=['-map','0:v:0','-map',('0:a:0' if has_audio else '1:a:0'),'-t',str(seconds),'-vf','scale=in_range=full:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709,format=yuv420p','-r','30','-c:v','libx264','-crf','16','-preset','veryfast','-threads','2','-profile:v','high','-level:v','4.1','-video_track_timescale','90000','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','256k','-ar','48000','-ac','2',str(target)]
  run(args,name+'-normalize.log')
 files=[work/'FTI-SIDE-OPENING-PREVIEW-normalized.mp4',work/f'PART-{n}-CARD-normalized.mp4',body]
 lengths=[16,4,duration]
 if n==1:
  files.append(work/'NEXT-EPISODE-normalized.mp4');lengths.append(5)
 files.append(work/'FTI-SIDE-CLOSING-normalized.mp4');lengths.append(7)
 manifest=work/f'concat-{n}.txt';manifest.write_text(''.join("file '"+str(f)+"'\nduration "+str(seconds)+"\n" for f,seconds in zip(files,lengths)))
 target=out/(f'FTI-SIDE-PART-{n}'+('-PREVIEW' if a.preview else '')+'.mp4')
 run(['ffmpeg','-nostdin','-hide_banner','-y','-f','concat','-safe','0','-i',str(manifest),'-c','copy','-movflags','+faststart',str(target)],f'part-{n}'+('-preview' if a.preview else '')+'-mux.log')
 print('EXPORTED',target,flush=True)
