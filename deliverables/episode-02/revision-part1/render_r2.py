"""FTI SIDE Episode 2 Part 1 revision and portrait trailer."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import edit_episode as base

MUSIC = 'episode2-indie-pop.wav'
SIGNATURE = ('drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:'
             'text=FTI SIDE / PART 1:x=95:y=65:fontsize=25:fontcolor=white:'
             'shadowcolor=black:shadowx=2:shadowy=3')
CAPTIONS = Path('captions-r2.json')
PART = 'FTI-SIDE-EP02-PART-1'
CREAM, ORANGE = base.CREAM, base.ORANGE
TITLE = base.TITLE.replace('\n',r'\N' + ORANGE)
PEOPLE = [
    ('FAJAR',0,204.10,207.75,6.41,9.61,0),
    ('FATHUR',240,207.75,209.23,158.12,161.30,296),
    ('CHIARO',1038,209.23,210.29,343.27,349.63,1132),
    ('KINAN',1184,210.29,211.27,358.73,363.06,1280),
    ('MUTI',1320,211.27,212.53,20.75,26.32,1416),
]


def tag(text, x, y, size, start, end, color=CREAM, align=7, style='Title'):
    # Colors use ASS's BGR order.
    motion = (rf'{{\an{align}\move({x},{y+26},{x},{y},0,230)\fs{size}'
              rf'\fad(125,145)\blur.35}}')
    return base.event(start,end,style,motion+color+text,3)


def sticker(text, x, y, start, end, size=88):
    anim = (rf'{{\an7\pos({x},{y})\frz3\fs{size}\bord13\shad5\fscx84\fscy84'
            r'\t(0,170,\fscx100\fscy100)\fad(80,120)\c&H00201810&\3c&H004889FF&}')
    return base.event(start,end,'Caption',anim+text,4)


def duration(path):
    return float(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0',
        '-show_entries','stream=duration','-of','csv=p=0',str(path)],text=True))


def render(out, start, end, *, dialog=True, bed=None, crop='', graphics=(), signature=False,
           captions=True, portrait=False, freeze=False, dark=False, click=None, quote_window=None):
    length=end-start
    cues=list(base.captions_for_span(json.loads(CAPTIONS.read_text()),start,end)) if dialog and captions else []
    mp4=out.with_suffix('.mp4')
    if mp4.exists() and out.with_suffix('.progress').read_text().endswith('progress=end\n'):
        return mp4, cues
    ass=out.with_suffix('.ass')
    visible=cues if quote_window is None else [cue for cue in cues if cue[1] <= quote_window[0] or cue[0] >= quote_window[1]]
    if portrait:
        hdr=base.HEADER.replace('PlayResX: 1920','PlayResX: 1080').replace('PlayResY: 1080','PlayResY: 1920')
        hdr=hdr.replace(',2,180,180,84,1',',2,58,58,390,1')
        ass.write_text(hdr+''.join([*graphics,*base.caption_events(visible)]))
    else:
        base.write_ass(ass,[*graphics,*base.caption_events(visible)])
    if portrait:
        video=f'fps=30,scale=1080:1920:flags=fast_bilinear,setsar=1,format=yuv420p'
    else:
        video=base.VIDEO
    vf=(','.join(filter(None,[crop,video,'eq=contrast=1.025:saturation=1.045',
        'drawbox=x=0:y=0:w=iw:h=ih:color=0x0b141c@0.40:t=fill' if dark else '',
        f'ass={ass}',SIGNATURE if signature else ''])))
    inputs=base.input_span('source.mp4',start,length if not freeze else .05)
    if freeze:
        vf=vf.replace(',eq=',f',tpad=stop_mode=clone:stop_duration={length},eq=',1)
    audio=[]
    mix=[]
    if dialog:
        inputs+=base.input_span('voice.wav',start,length)
        audio.append(f'[1:a]aresample=48000,asetpts=PTS-STARTPTS,afade=in:d=0.045,afade=out:st={max(0,length-.065)}:d=0.065[d]')
        mix.append('[d]')
    if bed is not None:
        at,gain=bed
        number=2 if dialog else 1
        inputs+=['-stream_loop','-1','-ss',str(at%29.5),'-i',MUSIC]
        audio.append(f'[{number}:a]atrim=duration={length},asetpts=PTS-STARTPTS,volume={gain},afade=in:d=0.07,afade=out:st={max(0,length-.12)}:d=0.12[m]')
        mix.append('[m]')
    if click is not None:
        number=1+int(dialog)+int(bed is not None)
        effect = Path('part1-v3-pop.wav')
        if not effect.exists():
            effect = Path(__file__).resolve().parents[3]/'studio/public/audio/part1-v3-pop.wav'
        inputs+=['-i',str(effect)]
        audio.append(f'[{number}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=0.13,adelay={round(click*1000)}:all=1[c]')
        mix.append('[c]')
    audio.append(''.join(mix)+f'amix=inputs={len(mix)}:duration=longest:normalize=0,alimiter=limit=0.84:level=false:latency=true[a]')
    base.ffmpeg([*inputs,'-vf',vf,'-filter_complex',';'.join(audio),'-map','0:v:0','-map','[a]',
                 '-t',str(length)],mp4)
    return mp4,cues


def chapter(at,label,heading):
    return [
        tag(label,960,688,27,at,at+3.8,ORANGE,align=8,style='Label'),
        tag(heading,960,738,63,at+.05,at+3.8,align=8),
    ]


def assemble(out,clips):
    lengths=[duration(p) for p,_ in clips]
    playlist=out.with_suffix('.ffconcat')
    playlist.write_text(''.join(f"file '{p.name}'\nduration {length:.6f}\n" for (p,_),length in zip(clips,lengths)))
    inputs=[arg for clip,_ in clips for arg in ('-i',str(clip))]
    audio=[f'[{i+1}:a]aresample=48000,apad,atrim=duration={length:.6f},asetpts=PTS-STARTPTS[a{i}]'
           for i,length in enumerate(lengths)]
    audio.append(''.join(f'[a{i}]' for i in range(len(clips)))+
                 f'concat=n={len(clips)}:v=0:a=1[a]')
    base.ffmpeg(['-f','concat','-safe','0','-i',str(playlist),*inputs,'-filter_complex',';'.join(audio),
        '-map','0:v:0','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','2',
        '-video_track_timescale','90000'],out.with_suffix('.mp4'),encode=False)
    timeline=[]
    offset=0
    for (_, cues), length in zip(clips,lengths):
        timeline.extend((offset+a,offset+min(b,length),t) for a,b,t in cues if a<length)
        offset+=length
    out.with_suffix('.srt').write_text('\n'.join(
        f'{i}\n{base.stamp(a,False)} --> {base.stamp(b,False)}\n{t}\n'
        for i,(a,b,t) in enumerate(timeline,1)))


def name_shot(dir,n):
    name,x,start,end,*_=PEOPLE[n]
    name_start=1.08 if n==0 else .06
    overlay=[tag('KENALIN DULU.',112,720,24,name_start,end-start,style='Label'),
             sticker(name,112,785,name_start,end-start)]
    width,height,y=(600,338,355) if name=='MUTI' else (704,396,354)
    return render(dir/f'name{n}',start,end,bed=(7.2+start-204.10,.075),
                  crop=f'crop={width}:{height}:{x}:{y}',graphics=overlay,click=name_start)


def body_shot(dir,n):
    start,end=[(4.93,204.10),(219,411.8),(411.8,622.8),(622.8,848.93)][n]
    graphics=[
        chapter(.20,'PART 01','Saat “gapapa” jadi kebiasaan')+
        [tag('“Gak semua hal harus diceritain' + r'\N' + ORANGE + 'ke semua orang, kan?”',
             960,665,59,153.19,156.32,align=8)],
        chapter(4.8,'PART 01','Capeknya baru terasa'),
        chapter(.28,'PART 01','Tanda kecil yang mulai terasa'),
        chapter(47.5,'PART 01','Kapan kita siap cerita?'),
    ][n]
    return render(dir/f'body{n}',start,end,signature=True,graphics=graphics,
                  quote_window=(153.19,156.32) if n==0 else None)


def main_video(dir):
    clips=[]
    for n,(point,label,zoom) in enumerate([
        (214.20,'FTI '+ORANGE+'SIDE',''),
        (37.1,'KELIHATAN GAPAPA?', 'crop=1360:764:560:180'),
        (310.7,'TETEP JALAN.', 'crop=1360:764:0:180'),
        (724.7,'KAPAN PERLU CERITA?', ''),
    ]):
        length=1.1
        content=[tag('BEM FTI UNIVERSITAS TRISAKTI',95,80,27,.02,length,style='Label')]
        content += [tag(label,104,685,161,.01,length)] if n==0 else [sticker(label,112,750,.01,length,74)]
        clips.append(render(dir/f'beat{n}',point,point+length,dialog=False,bed=(n*length,.56),crop=zoom,graphics=content,dark=True))
    clips.append(render(dir/'episode-title',214.8,217.6,dialog=False,bed=(4.4,.53),dark=True,
        graphics=[tag('EPISODE 02',108,475,35,.08,2.8,ORANGE,style='Label'),
                  tag(TITLE,105,570,92,.13,2.8)]))
    for n in range(len(PEOPLE)):
        clips.append(name_shot(dir,n))
    clips.append(render(dir/'welcome',212.53,219,bed=(15.63,.15),
        graphics=[tag('AND WELCOME TO',960,715,38,.16,4.03,align=8,style='Label'),
                  tag('FTI '+ORANGE+'SIDE!',960,776,138,.22,4.03,align=8)]))
    for n in range(4):
        clips.append(body_shot(dir,n))
    length=7.5
    cursor=(r'{\an7\move(1424,680,1006,362,0,680)\p1\bord3\shad2}'
            r'm 0 0 l 12 92 29 69 54 106 69 97 45 60 76 58{\p0}')
    pulse=(r'{\an5\pos(960,345)\p1\bord5\alpha&H30&\fscx50\fscy50'
           r'\t(0,500,\fscx200\fscy200,\alpha&HFF&)}m -45 -45 l 45 -45 45 45 -45 45 -45 -45{\p0}')
    pause=r'{\an5\pos(960,345)\p1\bord7\shad3}m -39 -54 l -14 -54 -14 54 -39 54 m 14 -54 l 39 -54 39 54 14 54{\p0}'
    clips.append(render(dir/'pause',848.88,848.88+length,dialog=False,bed=(18.4,.44),freeze=True,dark=True,click=.71,
        graphics=[base.event(.06,length,'Title',pause,4),base.event(.02,length,'Title',cursor,5),
                  base.event(.70,1.27,'Title',pulse,4),
                  tag('Penasaran selanjutnya?',960,549,54,.8,length,align=8),
                  tag('SAKSIKAN '+ORANGE+'PART 2',960,632,103,.9,length,align=8),
                  tag('Gimana menghadapi ekspektasi dan takut tertinggal?',960,784,33,1.16,length,align=8,style='Label')]))
    assemble(dir/PART,clips)


def trailer(dir):
    clips=[]
    offset=0
    for n,index in enumerate((0,4,2,3,1)):
        name,_,_,_,start,end,x = PEOPLE[index]
        text=[tag('FTI '+ORANGE+'SIDE',62,105,69,.06,end-start,style='Title'),
              tag('EPISODE 02 · PART 1',65,199,31,.08,end-start,ORANGE,style='Label'),
              sticker(name,67,1175,.15,end-start,66)]
        clips.append(render(dir/f'trailer{n}',start,end,bed=(offset,.115),portrait=True,
                            crop=f'crop=504:896:{x}:96',graphics=text))
        offset+=end-start
    length=4.1
    outro=[tag('FTI '+ORANGE+'SIDE',540,293,105,.06,length,align=8),
           tag('KITA BENERAN GAPAPA,',540,1059,65,.13,length,align=8),
           tag('ATAU UDAH KEBIASA AJA?',540,1149,63,.2,length,ORANGE,align=8),
           tag('SAKSIKAN EPISODE 02 · PART 1',540,1435,38,.32,length,align=8,style='Label')]
    clips.append(render(dir/'trailer-end',213.5,213.5+length,dialog=False,bed=(offset,.63),portrait=True,
                        crop='scale=1080:608:flags=fast_bilinear,pad=1080:1920:0:494:0x11191e',
                        graphics=outro,dark=True))
    assemble(dir/(PART+'-STORY'),clips)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('format',choices=('main','trailer'))
    selection=parser.parse_args().format
    target=Path('r2' if selection=='main' else 'story')
    target.mkdir(exist_ok=True)
    (main_video if selection=='main' else trailer)(target)
