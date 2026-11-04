import {AbsoluteFill,Series,useVideoConfig,staticFile} from 'remotion';
import {Video,Audio} from '@remotion/media';
import {Opening} from './Opening';
import {Closing} from './Closing';
import {PartCard,NextEpisode} from './PartCard';
import {CaptionTrack} from './CaptionTrack';
import pages from './data/pages.json';

const SourceClip=({part}:{part:number})=>{
 const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#092a49'}}>
  <Video src={staticFile('sources/podcast.mp4')} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <Audio src={staticFile('audio/podcast-normalized.m4a')} premountFor={fps}/>
  <div style={{position:'absolute',left:98,top:65,width:285,height:58,background:'rgba(9,42,73,.88)',padding:'15px 18px',fontFamily:'DejaVu Sans, Arial, sans-serif',fontSize:25,fontWeight:700,color:'white'}}>FTI SIDE / {part}</div>
  <CaptionTrack pages={pages}/>
 </AbsoluteFill>;
};
export const PartOne=()=>{
 const {fps}=useVideoConfig();
 return <Series>
  <Series.Sequence name="Opening" durationInFrames={16*fps} premountFor={fps}><Opening/></Series.Sequence>
  <Series.Sequence name="Identitas Part 1" durationInFrames={4*fps} premountFor={fps}><PartCard part={1} title="Kenapa Ikut Organisasi?"/></Series.Sequence>
  <Series.Sequence name="Perkenalan dan alasan organisasi" trimBefore={3.8*fps} durationInFrames={591.8*fps} premountFor={fps}><SourceClip part={1}/></Series.Sequence>
  <Series.Sequence name="Ekspektasi dan pengalaman baru" trimBefore={607.1*fps} durationInFrames={554.5*fps} premountFor={fps}><SourceClip part={1}/></Series.Sequence>
  <Series.Sequence name="Lanjut Part 2" durationInFrames={5*fps} premountFor={fps}><NextEpisode/></Series.Sequence>
  <Series.Sequence name="Closing" durationInFrames={7*fps} premountFor={fps}><Closing/></Series.Sequence>
 </Series>;
};
export const PartTwo=()=>{
 const {fps}=useVideoConfig();
 return <Series>
  <Series.Sequence name="Opening" durationInFrames={16*fps} premountFor={fps}><Opening/></Series.Sequence>
  <Series.Sequence name="Identitas Part 2" durationInFrames={4*fps} premountFor={fps}><PartCard part={2} title="Bertumbuh, Memimpin, Mengatur Waktu"/></Series.Sequence>
  <Series.Sequence name="Perubahan diri dan kepemimpinan" trimBefore={1161.6*fps} durationInFrames={712*fps} premountFor={fps}><SourceClip part={2}/></Series.Sequence>
  <Series.Sequence name="Kesan pesan dan penutup asli" trimBefore={1907.2*fps} durationInFrames={372.7*fps} premountFor={fps}><SourceClip part={2}/></Series.Sequence>
  <Series.Sequence name="Closing" durationInFrames={7*fps} premountFor={fps}><Closing/></Series.Sequence>
 </Series>;
};
