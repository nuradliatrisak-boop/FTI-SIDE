import {Audio, Video} from '@remotion/media';
import {AbsoluteFill, Sequence, staticFile, useCurrentFrame, useVideoConfig, interpolate, Easing, spring} from 'remotion';

const orange = '#ff8948';
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const shots = [
  {at: 0, duration: 4, start: 34.2, src: 'opening.mp4', x: '100%', head: '24 JAM', accent: 'NGGAK CUKUP?', wide: false},
  {at: 4, duration: 4, start: 260, src: 'podcast.mp4', x: '35%', head: 'KENAPA IKUT', accent: 'ORGANISASI?', wide: false},
  {at: 8, duration: 5, start: 474.7, src: 'podcast.mp4', x: '75%', head: '“TERBENTUR,\nTERBENTUR, DAN', accent: 'TERBENTUK.”', wide: false},
  {at: 13, duration: 6.3, start: 666.8, src: 'podcast.mp4', x: '22%', head: 'PUSING?', accent: 'ADA ASIKNYA\nJUGA!', wide: false},
  {at: 19.3, duration: 4.5, start: 45, src: 'opening.mp4', x: '50%', head: 'WELCOME TO', accent: 'FTI SIDE!', wide: true},
  {at: 23.8, duration: 6.2, start: 48, src: 'opening.mp4', x: '50%', head: 'SAKSIKAN FTI SIDE', accent: 'SELENGKAPNYA!', wide: true},
];
type Shot = typeof shots[number];
const StoryShot = ({shot, last}: {shot: Shot; last: boolean}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const length = shot.duration * fps;
  const opacity = shot.at === 0 ? 1 : interpolate(f, [0, .2 * fps], [0, 1], clamp);
  const volume = last ? 0 : Math.min(interpolate(f, [0, .08 * fps], [0, 1], clamp), interpolate(f, [length - .1 * fps, length], [1, 0], clamp));
  return <AbsoluteFill style={{opacity, overflow: 'hidden'}}>
    <Video src={staticFile(`sources/${shot.src}`)} trimBefore={Math.round(shot.start * fps)} muted objectFit="cover" premountFor={fps} style={{width: '100%', height: '100%', objectPosition: shot.x, filter: shot.wide ? 'blur(28px) brightness(.55)' : undefined, scale: interpolate(f, [0, .22 * fps, length], [1.035, 1, 1.055], clamp)}}/>
    {shot.wide ? <Video src={staticFile(`sources/${shot.src}`)} trimBefore={Math.round(shot.start * fps)} muted objectFit="contain" premountFor={fps} style={{position: 'absolute', left: 0, top: 510, width: 1080, height: 608}}/> : null}
    <Audio src={staticFile(shot.src === 'opening.mp4' ? 'audio/opening-v3-normalized.wav' : 'audio/podcast-normalized.m4a')} trimBefore={Math.round(shot.start * fps)} premountFor={fps} volume={volume}/>
    <Audio src={staticFile('audio/part1-v3-sweep.wav')} premountFor={fps} volume={.10}/>
    <Audio src={staticFile('audio/part1-v3-pop.wav')} from={Math.round(.24 * fps)} premountFor={fps} volume={.12}/>
    <AbsoluteFill style={{background: 'linear-gradient(rgba(0,0,0,.25),transparent 40%,rgba(0,0,0,.85))'}}/>
    <div style={{position: 'absolute', left: 0, top: 510, width: 12, height: 608, background: orange, opacity: interpolate(f, [0, .08 * fps, .28 * fps], [0, .75, 0], clamp), translate: `0 ${interpolate(f, [0, .28 * fps], [-120, 100], clamp)}px`}}/>
    <div style={{position: 'absolute', left: 75, right: 75, bottom: 330, fontSize: shot.at === 8 ? 68 : last ? 78 : 86, lineHeight: 1.12, whiteSpace: 'pre-line', fontWeight: 900, textShadow: '0 5px 20px black'}}>
      <div style={{fontSize: shot.at === 0 ? 164 : undefined, opacity: interpolate(f, [0, .16 * fps], [0, 1], clamp), translate: `0 ${interpolate(f, [0, .35 * fps], [40, 0], {...clamp, easing: Easing.out(Easing.cubic)})}px`}}>{shot.head}</div>
      <div style={{color: orange, fontSize: shot.at === 0 ? 98 : undefined, marginTop: 7, transformOrigin: 'left center', opacity: interpolate(f, [.12 * fps, .28 * fps], [0, 1], clamp), scale: .88 + .12 * spring({frame: f - Math.round(.12 * fps), fps, config: {damping: 16, stiffness: 190}})}}>{shot.accent}</div>
      <div style={{height: 7, background: orange, marginTop: 24, width: interpolate(f, [.2 * fps, .6 * fps], [0, 160], {...clamp, easing: Easing.out(Easing.cubic)})}}/>
    </div>
  </AbsoluteFill>;
};
export const Part1StoryV3 = () => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  return <AbsoluteFill style={{background: '#111', fontFamily: 'DejaVu Sans, Arial', color: '#fff8ed'}}>
    {shots.map((shot, i) => <Sequence key={shot.at} from={Math.round(shot.at * fps)} durationInFrames={Math.round((shot.duration + (i < shots.length - 1 ? .2 : 0)) * fps)} premountFor={fps}><StoryShot shot={shot} last={i === shots.length - 1}/></Sequence>)}
    <div style={{position: 'absolute', left: 75, top: 190, fontWeight: 900, fontSize: 43, letterSpacing: 5}}>FTI <span style={{color: orange}}>SIDE</span><div style={{fontSize: 22, letterSpacing: 2, marginTop: 18}}>BEM FTI UNIVERSITAS TRISAKTI</div></div>
    <Audio src={staticFile('audio/part1-v3-groove.wav')} premountFor={fps} volume={interpolate(f, [0, .5 * fps, 23.8 * fps, 24.2 * fps, 29 * fps, 30 * fps], [0, .16, .16, .55, .55, 0], clamp)}/>
    <AbsoluteFill style={{background: 'black', opacity: interpolate(f, [29.6 * fps, 30 * fps], [0, 1], clamp)}}/>
  </AbsoluteFill>;
};
