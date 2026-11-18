"""Export FTI SIDE Episode 2 from a source MP4, reviewed cues and an edit plan."""
import argparse
import json
import re
import subprocess
from pathlib import Path

FPS = 30
CREAM = r'{\c&H00EDF8FF&}'
ORANGE = r'{\c&H004889FF&}'
TITLE = 'KITA BENERAN GAPAPA,\nATAU UDAH KEBIASA AJA?'
HEADER = r"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,DejaVu Sans,46,&H00FFFFFF,&H00FFFFFF,&H3017130D,&H3017130D,-1,0,0,0,100,100,0,0,3,11,0,2,180,180,84,1
Style: Bug,DejaVu Sans,27,&H00EDF8FF,&H00EDF8FF,&H18191310,&H18191310,-1,0,0,0,100,100,2,0,3,13,0,7,103,80,71,1
Style: Title,DejaVu Sans,93,&H00EDF8FF,&H00EDF8FF,&H00211C18,&HA0211C18,-1,0,0,0,100,100,-2,0,1,0,4,7,100,100,80,1
Style: Label,DejaVu Sans,29,&H00EDF8FF,&H00EDF8FF,&H00171717,&HA0151515,-1,0,0,0,100,100,3,0,1,0,2,7,100,100,80,1
Style: Detail,DejaVu Sans,38,&H00EDF8FF,&H00EDF8FF,&H00171717,&HA0151515,-1,0,0,0,100,100,0,0,1,0,2,7,100,100,80,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
VIDEO = 'fps=30,scale=1920:1080:flags=fast_bilinear,setsar=1,format=yuv420p'
ENCODE = ['-c:v', 'libx264', '-preset', 'ultrafast', '-b:v', '5M', '-maxrate', '7M', '-bufsize', '10M', '-threads:v', '2',
          '-profile:v', 'high', '-level:v', '4.1', '-pix_fmt', 'yuv420p',
          '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
          '-video_track_timescale', '90000', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2']
WIDTH = 42


def stamp(seconds, ass=True):
    unit = 100 if ass else 1000
    n = max(0, round(seconds * unit))
    if ass:
        return f'{n//360000}:{n//6000%60:02}:{n//100%60:02}.{n%100:02}'
    return f'{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}'


def event(start, end, style, text, layer=0):
    return f'Dialogue: {layer},{stamp(start)},{stamp(end)},{style},,0,0,0,,{text}\n'


def write_ass(path, cues):
    path.write_text(HEADER + ''.join(cues), encoding='utf-8')


def ffmpeg(args, target, encode=True):
    progress = target.with_suffix('.progress')
    command = ['ffmpeg', '-hide_banner', '-nostdin', '-y', '-filter_threads', '2',
               '-filter_complex_threads', '2', '-progress', str(progress), '-nostats', *args,
               *(ENCODE if encode else []), '-movflags', '+faststart', str(target)]
    with target.with_suffix('.log').open('w') as log:
        subprocess.run(command, check=True, stdout=log, stderr=subprocess.STDOUT)


def input_span(source, start, duration):
    return ['-ss', str(start), '-t', str(duration), '-threads', '2', '-i', str(source)]


def subfilter(path):
    return f'ass={path.as_posix()}'


def captions_for_span(cues, start, end):
    for cue in cues:
        begin, finish = max(cue['start'], start), min(cue['end'], end)
        if finish-begin >= .37:
            yield begin-start, finish-start, cue['text']


def caption_events(captions):
    for begin, end, text in captions:
        safe_text = text.replace('{', '(').replace('}', ')').replace('\\', '/')
        yield event(begin, end, 'Caption', safe_text.replace('\n', r'\N'), 2)


def graphics(prefix, cfg, part, title):
    ass = prefix.with_suffix('.ass')
    length = 5.9 if title else 6.4
    source_position = cfg['title_frame'] if title else cfg['closing_frame']
    if title:
        rows = [
            event(.12, length, 'Label', r'{\pos(110,112)\fad(320,240)}FTI ' + ORANGE + 'SIDE' + CREAM + f'   /   EPISODE 02   •   PART {part}'),
            event(.30, length, 'Title', r'{\move(108,485,108,445,0,540)\fad(360,260)}' + TITLE.split('\n')[0] + r'\N' + ORANGE + TITLE.split('\n')[1]),
            event(.75, length, 'Label', r'{\pos(112,871)\fad(380,220)}BEM FTI UNIVERSITAS TRISAKTI'),
        ]
    else:
        accent = cfg['next_title']
        headline = 'LANJUT DI ' + ORANGE + 'PART 2' if part == 1 else 'MAKASIH SUDAH ' + ORANGE + 'NONTON!'
        rows = [
            event(.12, length, 'Label', r'{\pos(110,112)\fad(300,420)}FTI ' + ORANGE + 'SIDE' + CREAM + f'   /   EPISODE 02   •   PART {part}'),
            event(.38, length, 'Title', r'{\move(108,555,108,510,0,530)\fad(330,420)}' + headline),
            event(.72, length, 'Detail', r'{\pos(113,675)\fad(400,420)}' + accent),
        ]
    write_ass(ass, rows)
    vf = (f'{VIDEO},eq=brightness=-0.045:saturation=0.82,'
          'drawbox=x=0:y=0:w=iw:h=ih:color=0x0c151c@0.75:t=fill,'
          'drawbox=x=110:y=400:w=175:h=8:color=0xff8948:t=fill,'
          f'{subfilter(ass)},fade=in:d=0.21,fade=out:st={length-.28}:d=0.28')
    music_start = 0 if title else 15.9
    fade = .65 if title else 1.22
    af = (f'atrim=start={music_start}:duration={length},asetpts=PTS-STARTPTS,'
          f'volume=0.47,afade=in:d=0.24,afade=out:st={length-fade}:d={fade}')
    ffmpeg([*input_span('source.mp4', source_position, length+.03),
            '-i', 'episode2-original-pop.wav', '-map', '0:v:0', '-map', '1:a:0',
            '-vf', vf, '-af', af, '-t', str(length)], prefix.with_suffix('.mp4'))
    return length


def body(prefix, begin, end, cues, part, voice, chapter=None, gray=False, punch=''):
    captions = list(captions_for_span(cues, begin, end))
    length = end - begin
    ass = prefix.with_suffix('.ass')
    title = (r'{\pos(98,73)}FTI SIDE  ' + ORANGE + ' / ' + CREAM +
             (f'EP 02  •  PART {part}' if not gray else 'SEBELUMNYA  /  PART 1'))
    events = [event(0, length, 'Bug', title, 1), *caption_events(captions)]
    if chapter:
        at, label = chapter if isinstance(chapter, list) else (.3, chapter)
        events.append(event(at, min(at+3.8, length), 'Detail',
                            r'{\pos(100,152)\fad(240,380)}' + ORANGE + label, 1))
    write_ass(ass, events)
    grade = {'left': 'crop=1744:982:0:79,', 'right': 'crop=1744:982:176:79,', 'wide': ''}[punch or 'wide']
    vf = f'{grade}{VIDEO},eq=contrast=1.025:saturation={0 if gray else 1.035},{subfilter(ass)}'
    af = f'aresample=48000,afade=in:d=0.10,afade=out:st={max(0,length-.115)}:d=0.115'
    target = prefix.with_suffix('.mp4')
    progress = target.with_suffix('.progress')
    if not (target.exists() and progress.exists() and progress.read_text().endswith('progress=end\n')):
        ffmpeg([*input_span('source.mp4', begin, length), *input_span(voice, begin, length),
                '-map', '0:v:0', '-map', '1:a:0', '-vf', vf, '-af', af, '-t', str(length)], target)
    return length, captions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('part', type=int, choices=(1, 2))
    parser.add_argument('--preview', action='store_true')
    args = parser.parse_args()
    part = args.part
    cfg = json.loads(Path('edit-plan.json').read_text())[str(part)]
    cues = json.loads(Path('captions.json').read_text())
    edit_dir = Path(f'part{part}' + ('-preview' if args.preview else ''))
    edit_dir.mkdir(exist_ok=True)
    pieces = []
    durations = []
    timeline = []
    offset = 0

    def add(name, length, captions=()):
        nonlocal offset
        clip = name + '.mp4'
        measured = float(subprocess.check_output([
            'ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=duration',
            '-of', 'csv=p=0', str(edit_dir/clip)
        ], text=True))
        if abs(measured-length) > .15:
            raise ValueError(f'{clip} duration {measured} differs from planned duration {length}')
        pieces.append(clip)
        durations.append(measured)
        timeline.extend((offset+start, offset+min(end,measured), text) for start, end, text in captions if start < measured)
        offset += measured

    begin, end = cfg['hook']
    add('hook', *body(edit_dir/'hook', begin, end, cues, part, 'voice.wav', gray=part == 2, punch='left'))
    add('title', graphics(edit_dir/'title', cfg, part, True))
    for number, span in enumerate(cfg['spans'], 1):
        begin, end = span[:2]
        if args.preview:
            end = min(begin+15, end)
        name = f'body{number:02}'
        add(name, *body(edit_dir/name, begin, end, cues, part, 'voice.wav',
                        chapter=span[2] if len(span)>2 else None,
                        punch=span[3] if len(span)>3 else ''))
        if args.preview:
            break
    add('closing', graphics(edit_dir/'closing', cfg, part, False))
    playlist = edit_dir/'concat.txt'
    playlist.write_text(''.join(f"file '{clip}'\nduration {length:.6f}\n" for clip,length in zip(pieces,durations)))
    out = edit_dir / f'FTI-SIDE-EP02-PART-{part}'
    clip_inputs = [arg for clip in pieces for arg in ('-i', str(edit_dir/clip))]
    audio_filters = [
        f'[{i+1}:a]aresample=48000,apad,atrim=duration={length:.6f},asetpts=PTS-STARTPTS[a{i}]'
        for i,length in enumerate(durations)
    ]
    audio_filters.append(''.join(f'[a{i}]' for i in range(len(pieces))) +
                         f'concat=n={len(pieces)}:v=0:a=1,alimiter=limit=0.84:level=false:latency=true[a]')
    ffmpeg(['-f', 'concat', '-safe', '0', '-i', str(playlist), *clip_inputs,
            '-filter_complex', ';'.join(audio_filters), '-map', '0:v:0', '-map', '[a]',
            '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
            '-ac', '2', '-video_track_timescale', '90000'],
           out.with_suffix('.mp4'), encode=False)
    out.with_suffix('.srt').write_text('\n'.join(
        f'{index}\n{stamp(start,False)} --> {stamp(end,False)}\n{text}\n'
        for index,(start,end,text) in enumerate(timeline,1)), encoding='utf-8')


if __name__ == '__main__':
    main()
