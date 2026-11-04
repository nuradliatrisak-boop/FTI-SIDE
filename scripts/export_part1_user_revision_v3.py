"""Export user's Part 1 revision with corrected captions, image inserts and dissolves."""
import argparse,json,re,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1];work=root/'renders/revision-v3';work.mkdir(parents=True,exist_ok=True)
plan=json.loads((root/'docs/revision-v3/plan.json').read_text());pages=json.loads((root/'studio/src/data/part1-pages-v3.json').read_text())
p=argparse.ArgumentParser();p.add_argument('--body-only',action='store_true');p.add_argument('--preview',action='store_true');a=p.parse_args()
def run(args,name):
 with (root/'docs/revision-v3'/name).open('w') as f:subprocess.run(args,cwd=root,stdout=f,stderr=subprocess.STDOUT,check=True)
def ts(s):
 n=round(s*100);return f'{n//360000}:{n//6000%60:02}:{n//100%60:02}.{n%100:02}'
def esc(s):return s.replace('\\','\\\\').replace('{','\\{').replace('}','\\}').replace('\n',' ')
def bodytime(source):
 total=0
 for i,(s,e) in enumerate(plan['bodySpans']):
  if s<=source<=e:return total+source-s
  total+=e-s-plan['bodyDissolveSeconds']
 raise ValueError(source)
header='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,DejaVu Sans,44,&H00FFFFFF,&H00FFFFFF,&H29211405,&H29211405,-1,0,0,0,100,100,0,0,3,12,0,2,210,210,75,1
Style: Quote,DejaVu Sans,64,&H00FFFFFF,&H00FFFFFF,&H00101010,&H90101010,-1,0,0,0,100,100,0,0,1,3,3,5,150,150,0,1
Style: Title,DejaVu Sans,70,&H00FFFFFF,&H00FFFFFF,&H00101010,&H90101010,-1,0,0,0,100,100,0,0,1,3,3,5,100,100,0,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
events=[];srt=[(6.12,7.16,'Halo guys!'),(7.4,8.3,'Pernah gak sih kalian'),(8.3,9.6,'24 jam itu'),(9.6,11.16,'enggak cukup buat kita semua?'),(11.52,13.34,'So, di sini kita akan kupas tuntas.'),(14.56,15.88,'Perkenalin, gue Nadya.'),(15.88,16.8,'Ghivariel.'),(16.8,17.7,'Kinan.'),(17.7,18.9,'Cahaya.'),(18.9,21.75,'And welcome to FTI SIDE!')]
for begin,end in plan['bodySpans']:
 offset=bodytime(begin)
 for page in pages:
  st=max(page['startMs']/1000,begin);en=min(page['endMs']/1000,end)
  if en<=st or (475.74<=st<479):continue
  text=''.join(w['text'] for w in page['words']).strip()
  if not text:continue
  v=esc(text)
  if '♪' in text:v='{\\i1}'+v+'{\\i0}'
  events.append(f'Dialogue: 0,{ts(offset+st-begin)},{ts(offset+en-begin)},Default,,0,0,0,,{{\\fad(65,0)}}{v}')
  srt.append((plan['openingSeconds']-.2+offset+st-begin,plan['openingSeconds']-.2+offset+en-begin,text))
quote_start=bodytime(475.74)
events.append(f'Dialogue: 1,{ts(quote_start)},{ts(quote_start+3.25)},Quote,,0,0,0,,{{\\pos(960,735)\\fad(140,180)\\fscx90\\fscy90\\t(0,220,\\fscx100\\fscy100)}}“Terbentur, terbentur,\\Ndan {{\\c&H004889FF&}}terbentuk.{{\\c&H00FFFFFF&}}”')
events.append('Dialogue: 1,0:00:00.00,0:00:03.20,Title,,0,0,0,,{\\pos(960,740)\\fad(180,350)}{\\fs26\\c&H004889FF&}PART 01\\N{\\fs70\\c&H00FFFFFF&}Kenapa Ikut Organisasi?')
ass=work/'part1-v3.ass';ass.write_text(header+'\n'.join(events)+'\n')
srt.append((22.4+quote_start,22.4+quote_start+3.25,'“Terbentur, terbentur, dan terbentuk.”'))
srt.sort()
# Editable SRT, with timeline offsets matching the final composition.
def srtstamp(s):
 ms=round(s*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(root/'deliverables/FTI-SIDE-PART-1.srt').write_text('\n'.join(f'{i}\n{srtstamp(s)} --> {srtstamp(e)}\n{text}\n' for i,(s,e,text) in enumerate(srt,1)))
as_=bodytime(plan['images']['aisyah']['sourceStart']);ps=bodytime(plan['images']['paperMob']['sourceStart']);qd=plan['images']['aisyah']['duration']
args=['ffmpeg','-nostdin','-hide_banner','-nostats','-y']
for begin,end in plan['bodySpans']:
 args+=['-ss',str(begin),'-t',str(end-begin),'-i','studio/public/sources/podcast.mp4','-ss',str(begin),'-t',str(end-begin),'-i','studio/public/audio/podcast-normalized.m4a']
args+=['-itsoffset',str(as_),'-loop','1','-framerate','30','-t',str(qd),'-i','studio/public/images/aisyah-original.jpg','-itsoffset',str(ps),'-loop','1','-framerate','30','-t','8','-i','studio/public/images/paper-mob-instagram.jpg','-i','studio/public/audio/part1-v3-pop.wav','-i','studio/public/audio/part1-v3-three-notes.wav','-i','renders/part1-opening-v3.mp4','-i','renders/part1-outro-v3.mp4','-itsoffset',str(ps+.6),'-loop','1','-framerate','30','-t','2.2','-i','studio/public/images/click-cursor.png']
f=[]
for i,(begin,end) in enumerate(plan['bodySpans']):
 length=end-begin
 f.append(f'[{i*2}:v]trim=duration={length},setpts=PTS-STARTPTS,fps=30,format=yuv420p,settb=AVTB[v{i}]')
 f.append(f'[{i*2+1}:a]atrim=duration={length},asetpts=PTS-STARTPTS[a{i}]')
first=plan['bodySpans'][0][1]-plan['bodySpans'][0][0]-.2
second=first+plan['bodySpans'][1][1]-plan['bodySpans'][1][0]-.2
f += [f'[v0][v1]xfade=transition=fade:duration=0.2:offset={first},format=yuv420p[vx]',f'[vx][v2]xfade=transition=fade:duration=0.2:offset={second},format=yuv420p[vb]','[a0][a1]acrossfade=d=0.2:c1=tri:c2=tri[ax]','[ax][a2]acrossfade=d=0.2:c1=tri:c2=tri[ab]']
f.append(f"[6:v]scale=828:1026,crop=460:555:220:310,pad=488:690:14:14:color=0xfff8ed,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='KAK AISYAH':x=24:y=585:fontsize=38:fontcolor=0x151515,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='WAKABEM - Wakil Ketua BEM':x=24:y=637:fontsize=22:fontcolor=0x333333,format=rgba,fade=t=in:st={as_}:d=0.16:alpha=1,fade=t=out:st={as_+qd-.2}:d=0.2:alpha=1[photo]")
f.append(f"[vb][photo]overlay=x=730:y='125+650*pow(1-min(max((t-{as_})/.35,0),1),3)':enable='between(t,{as_},{as_+qd})':eof_action=pass[vphoto]")
f.append(f"[7:v]scale=540:-1,pad=560:730:10:10:color=0x0c1014,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='@bemftiusakti':x=18:y=615:fontsize=29:fontcolor=white,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='@pkkmbftitrisakti':x=18:y=661:fontsize=29:fontcolor=white,format=rgba,fade=t=in:st={ps}:d=0.18:alpha=1,fade=t=out:st={ps+7.8}:d=0.2:alpha=1[post]")
f.append(f"[vphoto][post]overlay=x='690+620*pow(1-min(max((t-{ps})/.3,0),1),3)':y=100:enable='between(t,{ps},{ps+8})':eof_action=pass[vpost]")
f.append(f"[12:v]format=rgba,fade=t=in:st={ps+.6}:d=0.10:alpha=1,fade=t=out:st={ps+2.5}:d=0.2:alpha=1[cursor]")
f.append(f"[vpost][cursor]overlay=x='1470-360*min(max((t-{ps+.6})/.6,0),1)':y='900-310*min(max((t-{ps+.6})/.6,0),1)':enable='between(t,{ps+.6},{ps+2.8})':eof_action=pass[vclick]")
f.append(f"[vclick]subtitles=filename='{ass.relative_to(root)}',drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='FTI SIDE / PART 1':x=95:y=65:fontsize=25:fontcolor=white:shadowcolor=black:shadowx=2:shadowy=3[vout]")
f += ['[8:a]asplit=2[p0][p1]',f'[p0]volume=.30,adelay={round(as_*1000)}|{round(as_*1000)}[pop0]',f'[p1]volume=.3,adelay={round((ps+1.2)*1000)}|{round((ps+1.2)*1000)}[pop1]',f'[9:a]volume=.13,adelay={round(bodytime(787)*1000)}|{round(bodytime(787)*1000)}[notes]','[ab][pop0][pop1][notes]amix=inputs=4:duration=first:normalize=0[aout]']
f += ['[10:v]scale=in_range=full:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709,fps=30,format=yuv420p,settb=AVTB[op]','[vout]settb=AVTB[bt]','[op][bt]xfade=transition=fade:duration=0.2:offset=22.4,format=yuv420p[mainv]','[10:a][aout]acrossfade=d=0.2:c1=tri:c2=tri[maina]','[11:v]scale=in_range=full:out_range=tv:in_color_matrix=bt601:out_color_matrix=bt709,fps=30,format=yuv420p,settb=AVTB[ending]','[mainv][maina][ending][11:a]concat=n=2:v=1:a=1[finalv][finala]']
duration=120 if a.preview else plan['durationSeconds']
target=root/'deliverables'/('FTI-SIDE-PART-1-V3-PREVIEW.mp4' if a.preview else 'FTI-SIDE-PART-1-V3.mp4')
args+=['-filter_complex_threads','2','-filter_complex',';'.join(f),'-map','[finalv]','-map','[finala]','-t',str(duration),'-c:v','libx264','-preset','veryfast','-crf','18','-threads','3','-pix_fmt','yuv420p','-profile:v','high','-level:v','4.1','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-video_track_timescale','90000','-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-movflags','+faststart','-progress',str(work/'body-progress.txt'),str(target)]
print('Rendering Part 1',duration,'seconds',flush=True)
run(args,'preview-export.log' if a.preview else 'final-export.log')
print('EXPORTED',target,flush=True)
