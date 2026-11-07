"""Export corrected Part 2 with throwback, quote cards, real documentation and smooth cuts."""
import argparse,json,subprocess
from pathlib import Path
r=Path(__file__).resolve().parents[1];work=r/'renders/part2-revision-v5';work.mkdir(exist_ok=True,parents=True)
plan=json.load(open(r/'docs/part2-revision-v5/plan.json'));pages=json.load(open(r/'studio/src/data/part2-pages-v5.json'))
p=argparse.ArgumentParser();p.add_argument('--preview',action='store_true');a=p.parse_args()
def bt(t):
 off=0
 for s,e in plan['bodySpans']:
  if s<=t<=e:return off+t-s
  off+=e-s-.2
 raise ValueError(t)
def ass_stamp(t):
 n=round(t*100);return f'{n//360000}:{n//6000%60:02}:{n//100%60:02}.{n%100:02}'
def srt_stamp(t):
 n=round(t*1000);return f'{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}'
header='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,DejaVu Sans,44,&H00FFFFFF,&H00FFFFFF,&H29211405,&H29211405,-1,0,0,0,100,100,0,0,3,12,0,2,210,210,75,1
Style: Quote,DejaVu Sans,60,&H00EDF8FF,&H00EDF8FF,&H00101010,&H90101010,-1,0,0,0,100,100,0,0,1,3,3,5,180,180,0,1
Style: Title,DejaVu Sans,70,&H00EDF8FF,&H00EDF8FF,&H00101010,&H90101010,-1,0,0,0,100,100,0,0,1,3,3,5,100,100,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
events=[];srt=[(.7,4.45,'Tujuannya untuk ikut organisasi itu apa?'),(4.7,7.95,'Pokoknya kita ini terbentur, terbentur, dan terbentuk.')]
for begin,end in plan['bodySpans']:
 for page in pages:
  st=max(page['startMs']/1000,begin);en=min(page['endMs']/1000,end)
  if en<=st:continue
  text=''.join(w['text'] for w in page['words']).strip()
  srt.append((19.8+bt(st),19.8+bt(en),text))
  intervals=[(st,en)]
  for q in plan['quotes']:
   nxt=[]
   for x,y in intervals:
    if y<=q['start'] or x>=q['end']:nxt.append((x,y));continue
    if x<q['start']:nxt.append((x,q['start']))
    if y>q['end']:nxt.append((q['end'],y))
   intervals=nxt
  for x,y in intervals:
   text=''.join(w['text'] for w in page['words'] if w['startMs']/1000<y and w['endMs']/1000>x).strip()
   if text:events.append(f'Dialogue: 0,{ass_stamp(bt(x))},{ass_stamp(bt(y))},Default,,0,0,0,,{{\\fad(65,0)}}{text}')
for q in plan['quotes']:
 parts=q['text'].split('\n');parts[-1]='{\\c&H004889FF&}'+parts[-1]+'{\\c&H00EDF8FF&}';text='“'+'\\N'.join(parts)+'”'
 events.append(f'Dialogue: 1,{ass_stamp(bt(q["start"]))},{ass_stamp(bt(q["end"]))},Quote,,0,0,0,,{{\\pos(960,755)\\fad(130,120)\\fscx94\\fscy94\\t(0,220,\\fscx100\\fscy100)}}{text}')
for c in plan['chapters']:
 st=bt(c['start']);title=c['title'].rsplit(' ',1);colored=title[0]+' {\\c&H004889FF&}'+title[1];events.append(f'Dialogue: 1,{ass_stamp(st)},{ass_stamp(st+3.4)},Title,,0,0,0,,{{\\pos(960,735)\\fad(150,300)\\fs25\\c&H004889FF&}}EPISODE 01 / PART 2\\N{{\\fs70\\c&H00EDF8FF&}}{colored}')
ass=work/'part2-v5.ass';ass.write_text(header+'\n'.join(events)+'\n')
srt.sort();(r/'deliverables/FTI-SIDE-PART-2.srt').write_text('\n'.join(f'{i}\n{srt_stamp(st)} --> {srt_stamp(en)}\n{text}\n' for i,(st,en,text) in enumerate(srt,1)))
(r/'deliverables/TRANSKRIP-PART-2-V5.txt').write_text('FTI SIDE — Episode 1 Part 2, timestamp video final\n\n'+'\n'.join(f'[{srt_stamp(st)}] {text}' for st,en,text in srt))
if a.preview:
 font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
 filters=f"[0:v]scale=in_range=full:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709,fps=30,format=yuv420p,settb=AVTB[iv];[1:v]setpts=PTS-STARTPTS,fps=30,format=yuv420p,settb=AVTB,subtitles=filename='{ass.relative_to(r)}',drawtext=fontfile={font}:text='FTI SIDE / EP 1 • PART 2':x=95:y=65:fontsize=25:fontcolor=0xfff8ed:shadowcolor=black:shadowx=2:shadowy=3[bv];[iv][bv]xfade=transition=fade:duration=0.2:offset=19.8[v];[2:a]asetpts=PTS-STARTPTS[ba];[0:a][ba]acrossfade=d=0.2:c1=tri:c2=tri[au]"
 cmd=['ffmpeg','-nostdin','-hide_banner','-y','-i','renders/part2-intro-v5.mp4','-ss','1161.6','-t','90.2','-i','studio/public/sources/podcast.mp4','-ss','1161.6','-t','90.2','-i','studio/public/audio/podcast-part2-enhanced.m4a','-filter_complex_threads','2','-filter_complex',filters,'-map','[v]','-map','[au]','-t','110','-c:v','libx264','-preset','veryfast','-crf','18','-threads','3','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-ar','48000','-movflags','+faststart',str(r/'deliverables/FTI-SIDE-PART-2-V5-PREVIEW.mp4')]
 with (work/'preview-export.log').open('w') as log:subprocess.run(cmd,cwd=r,stdout=log,stderr=subprocess.STDOUT,check=True)
 print('PREVIEW EXPORTED',flush=True)
 raise SystemExit(0)
args=['ffmpeg','-nostdin','-hide_banner','-nostats','-y']
for s,e in plan['bodySpans']:args+=['-ss',str(s),'-t',str(e-s),'-i','studio/public/sources/podcast.mp4','-ss',str(s),'-t',str(e-s),'-i','studio/public/audio/podcast-part2-enhanced.m4a']
args+=['-i','renders/part2-intro-v5.mp4','-i','renders/part2-outro-v5.mp4']
for im in plan['images']:args+=['-itsoffset',str(bt(im['start'])),'-loop','1','-framerate','30','-t',str(im['duration']),'-i','studio/public/images/'+im['file']]
args+=['-i','studio/public/audio/part2-v5-pop.wav','-i','studio/public/audio/part2-v5-groove.wav']
f=[]
for i,(s,e) in enumerate(plan['bodySpans']):
 f.append(f'[{2*i}:v]tpad=stop_mode=clone:stop_duration=0.2,trim=duration={e-s},setpts=PTS-STARTPTS,fps=30,format=yuv420p,settb=AVTB[v{i}]')
 f.append(f'[{2*i+1}:a]atrim=duration={e-s},asetpts=PTS-STARTPTS[a{i}]')
f+=['[v0][v1]xfade=transition=fade:duration=0.2:offset=711.8,format=yuv420p[vbody]','[a0][a1]acrossfade=d=0.2:c1=tri:c2=tri[abody]']
last='vbody';font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
for i,im in enumerate(plan['images']):
 st=bt(im['start']);en=st+im['duration'];titles=im['name'].split(' • ')
 extra=f",drawtext=fontfile={font}:text='{titles[1]}':x=20:y=714:fontsize=22:fontcolor=0xff8948" if len(titles)>1 else ''
 f.append(f"[{6+i}:v]scale=420:650:force_original_aspect_ratio=decrease,pad=450:780:(ow-iw)/2:16:color=0x11181e,drawbox=x=0:y=0:w=450:h=780:color=0xff8948:t=3,drawtext=fontfile={font}:text='{titles[0]}':x=20:y=680:fontsize=27:fontcolor=0xff8948{extra},drawtext=fontfile={font}:text='@bemftiusakti':x=20:y=748:fontsize=25:fontcolor=0xfff8ed,format=rgba,fade=t=in:st={st}:d=0.16:alpha=1,fade=t=out:st={en-.2}:d=0.2:alpha=1[card{i}]")
 f.append(f"[{last}][card{i}]overlay=x=735:y='90+960*pow(1-min(max((t-{st})/0.35,0),1),3)':enable='between(t,{st},{en})':eof_action=pass[vi{i}]");last=f'vi{i}'
f.append(f"[{last}]subtitles=filename='{ass.relative_to(r)}',drawtext=fontfile={font}:text='FTI SIDE / EP 1 • PART 2':x=95:y=65:fontsize=25:fontcolor=0xfff8ed:shadowcolor=black:shadowx=2:shadowy=3[vout]")
f+=['[9:a]asplit=3[p0][p1][p2]']
for i,im in enumerate(plan['images']):f.append(f'[p{i}]volume=0.18,adelay={round(bt(im["start"])*1000)}|{round(bt(im["start"])*1000)}[sfx{i}]')
f.append("[10:a]atrim=start=24.01:end=29.4,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.18,volume='0.16+0.39*min(max((t-1.25)/0.3,0),1)':eval=frame,adelay=1079110|1079110[cue]")
f+=['[abody][sfx0][sfx1][sfx2][cue]amix=inputs=5:duration=first:normalize=0[aout]','[4:v]scale=in_range=full:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709,fps=30,format=yuv420p,settb=AVTB[intro]','[vout]fps=30,settb=AVTB[body]','[intro][body]xfade=transition=fade:duration=0.2:offset=19.8,format=yuv420p[mainv]','[4:a][aout]acrossfade=d=0.2:c1=tri:c2=tri[maina]','[5:v]scale=in_range=full:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709,fps=30,format=yuv420p,settb=AVTB[outro]','[mainv][maina][outro][5:a]concat=n=2:v=1:a=1[finalv][finala]']
f.append('[finala]alimiter=limit=0.89:level=false:latency=true[limiteda]')
duration=110 if a.preview else plan['durationSeconds'];target=r/'deliverables'/('FTI-SIDE-PART-2-V5-PREVIEW.mp4' if a.preview else 'FTI-SIDE-PART-2-V5.mp4')
args+=['-filter_complex_threads','2','-filter_complex',';'.join(f),'-map','[finalv]','-map','[limiteda]','-t',str(duration),'-c:v','libx264','-preset','veryfast','-crf','18','-threads','3','-pix_fmt','yuv420p','-profile:v','high','-level:v','4.1','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-video_track_timescale','90000','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-movflags','+faststart','-progress',str(work/'export-progress.txt'),str(target)]
print('Export Part 2',duration,'seconds',flush=True)
with (work/('preview-export.log' if a.preview else 'final-export.log')).open('w') as log:subprocess.run(args,cwd=r,stdout=log,stderr=subprocess.STDOUT,check=True)
print('EXPORTED',target,flush=True)
