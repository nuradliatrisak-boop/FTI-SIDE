import {RewindButton,ForwardBridge} from './Part2PlaybackV5';
import {Audio,Video} from '@remotion/media';
import {AbsoluteFill,CanvasImage,Sequence,staticFile,useCurrentFrame,useVideoConfig,interpolate,spring} from 'remotion';
import {CaptionTrack} from './CaptionTrack';
import pages from './data/part2-pages-v5.json';
import plan from './data/part2-plan-v5.json';
const orange='#ff8948',cream='#fff8ed',font='DejaVu Sans, Arial, sans-serif';
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'} as const;
const shadow='0 5px 20px rgba(0,0,0,.85)';
const BodyFootage=({start,enhanced=false,volume=1,gray=false}:{start:number;enhanced?:boolean;volume?:number;gray?:boolean})=>{
 const {fps}=useVideoConfig();const f=useCurrentFrame();
 return <AbsoluteFill><Video src={staticFile('sources/podcast.mp4')} trimBefore={Math.round(start*fps)} muted objectFit="cover" premountFor={fps} style={{width:'100%',height:'100%',filter:gray?'grayscale(1)':undefined}}/><Audio src={staticFile(enhanced?'audio/podcast-part2-enhanced.m4a':'audio/podcast-normalized.m4a')} trimBefore={Math.round(start*fps)} premountFor={fps} volume={Math.min(volume,interpolate(f,[0,3],[0,volume],clamp))}/></AbsoluteFill>;
};
const CaptionRibbon=({label,text}:{label:string;text:string})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{fontFamily:font,color:cream}}><AbsoluteFill style={{background:'linear-gradient(transparent 35%,rgba(0,0,0,.75))'}}/><div style={{position:'absolute',left:95,top:65,fontSize:25,fontWeight:800,letterSpacing:3,background:'rgba(0,0,0,.6)',padding:'12px 20px',borderLeft:`7px solid ${orange}`}}>{label}</div><div style={{position:'absolute',left:105,right:105,bottom:115,fontSize:78,fontWeight:900,textShadow:shadow,whiteSpace:'pre-line',scale:.94+.06*spring({frame:f,fps,config:{damping:18}})}}>{text.split('\n').map((line,i,all)=><div key={i} style={{color:i===all.length-1?orange:cream}}>{line}</div>)}</div></AbsoluteFill>;
};
export const Part2Intro=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111',fontFamily:font,color:cream}}>
  <Video src={staticFile('video/part2-rewind-v5.mp4')} durationInFrames={Math.round(.6*fps)} muted premountFor={fps} style={{width:'100%',height:'100%',filter:'grayscale(1)'}}/>
  <Sequence from={Math.round(.6*fps)} durationInFrames={4*fps} premountFor={fps}><BodyFootage start={260} gray/><CaptionRibbon label="SEBELUMNYA / PART 1" text={'KENAPA IKUT\nORGANISASI?'}/></Sequence>
  <Sequence from={Math.round(4.6*fps)} durationInFrames={Math.round(3.4*fps)} premountFor={fps}><BodyFootage start={475.74} gray/><CaptionRibbon label="SEBELUMNYA / PART 1" text={'“TERBENTUR, TERBENTUR,\nDAN TERBENTUK.”'}/></Sequence>
  <Sequence from={8*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/podcast.mp4')} trimBefore={1225*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><CaptionRibbon label="LANJUT CERITANYA / PART 2" text={'DARI IKUT\nORGANISASI…'}/></Sequence>
  <Sequence from={11*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/podcast.mp4')} trimBefore={1527*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><CaptionRibbon label="EPISODE 01 • PART 2" text={'KE\nTANGGUNG JAWAB.'}/></Sequence>
  <Sequence from={14*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/podcast.mp4')} trimBefore={2119*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><CaptionRibbon label="EPISODE 01 • PART 2" text={'DAN CARA\nBAGI WAKTU.'}/></Sequence>
  <Sequence from={17*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/opening.mp4')} trimBefore={47*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><AbsoluteFill style={{background:'linear-gradient(transparent,rgba(0,0,0,.75))'}}/><div style={{position:'absolute',left:100,bottom:115,textShadow:shadow,scale:.94+.06*spring({frame:f-17*fps,fps,config:{damping:18}})}}><div style={{fontSize:32,fontWeight:800,letterSpacing:6}}>EPISODE 01 · BERTUMBUH <span style={{color:orange}}>BARENG</span></div><div style={{fontSize:160,fontWeight:900,letterSpacing:-8}}>FTI SIDE <span style={{color:orange}}>PART 2</span></div></div></Sequence>
  <Sequence durationInFrames={8*fps} premountFor={fps}><RewindButton/></Sequence>
  <Sequence from={8*fps} durationInFrames={Math.round(.6*fps)} premountFor={fps}><ForwardBridge/></Sequence>
  <Sequence from={Math.round(16.5*fps)} durationInFrames={Math.round(.7*fps)} premountFor={fps}><ForwardBridge/></Sequence>
  <Audio src={staticFile('audio/part2-v5-groove.wav')} premountFor={fps} volume={interpolate(f,[0,10,7.7*fps,8.1*fps,19.5*fps,20*fps],[0,.12,.12,.72,.72,0],clamp)}/>
  <Audio src={staticFile('audio/part2-v5-rewind.wav')} premountFor={fps} volume={.7}/>
  <Audio src={staticFile('audio/part2-v5-sweep.wav')} from={8*fps} premountFor={fps} volume={.25}/>
  <Audio src={staticFile('audio/part2-v5-sweep.wav')} from={Math.round(16.5*fps)} premountFor={fps} volume={.3}/>
 </AbsoluteFill>;
};
export const Part2Outro=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111',fontFamily:font,color:cream}}>
  <Video src={staticFile('sources/opening.mp4')} durationInFrames={Math.round(2.7*fps)} trimBefore={Math.round(47.2*fps)} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <Video src={staticFile('sources/podcast.mp4')} from={Math.round(2.7*fps)} durationInFrames={Math.round(2.5*fps)} trimBefore={Math.round(2274.5*fps)} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <Video src={staticFile('sources/podcast.mp4')} from={Math.round(5.2*fps)} durationInFrames={Math.round(2.3*fps)} trimBefore={Math.round(478.7*fps)} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <Video src={staticFile('sources/opening.mp4')} from={Math.round(7.5*fps)} durationInFrames={Math.round(2.5*fps)} trimBefore={48*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <AbsoluteFill style={{background:'linear-gradient(transparent 30%,rgba(0,0,0,.82))'}}/>
  <div style={{position:'absolute',left:105,right:105,bottom:100,textShadow:shadow,opacity:interpolate(f,[6,15],[0,1],clamp),translate:`0 ${interpolate(f,[0,18],[50,0],clamp)}px`}}><div style={{fontSize:38,fontWeight:800,letterSpacing:3}}>MAKASIH SUDAH <span style={{color:orange}}>NONTON!</span></div><div style={{fontSize:150,fontWeight:900,letterSpacing:-6}}>FTI <span style={{color:orange}}>SIDE</span></div><div style={{fontSize:33,fontWeight:700}}>@bemftiusakti</div><div style={{height:8,width:interpolate(f,[10,25],[0,270],clamp),background:orange,marginTop:25}}/></div>
  <Audio src={staticFile('audio/part2-v5-groove.wav')} trimBefore={Math.round(29.4*fps)} premountFor={fps} volume={interpolate(f,[0,8.8*fps,10*fps],[.55,.55,0],clamp)}/>
  <Audio src={staticFile('audio/part2-v5-pop.wav')} from={Math.round(2.7*fps)} premountFor={fps} volume={.15}/>
  <AbsoluteFill style={{background:'black',opacity:interpolate(f,[9.3*fps,10*fps],[0,1],clamp)}}/>
 </AbsoluteFill>;
};
export const Part2Documentation=({file,title}:{file:string;title:string})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{fontFamily:font}}><div style={{position:'absolute',left:735,top:interpolate(f,[0,.35*fps],[1050,90],clamp),width:450,height:780,background:'#11181e',border:`3px solid ${orange}`,borderRadius:15,boxShadow:'0 20px 45px rgba(0,0,0,.5)',opacity:interpolate(f,[0,6,4.3*fps,4.5*fps],[0,1,1,0],clamp)}}><CanvasImage src={staticFile(`images/${file}`)} premountFor={fps} style={{position:'absolute',left:15,top:16,width:420,height:650,objectFit:'contain'}}/><div style={{position:'absolute',left:20,right:20,top:680,color:orange,fontSize:24,fontWeight:800,whiteSpace:'pre-line',lineHeight:1.1}}>{title.replace(' • ','\n')}</div><div style={{position:'absolute',left:20,top:746,color:cream,fontSize:25,fontWeight:700}}>@bemftiusakti</div></div><Audio src={staticFile('audio/part2-v5-pop.wav')} premountFor={fps} volume={.18}/></AbsoluteFill>;
};
const Body=({start,end}:{start:number;end:number})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const t=f/fps;const q=plan.quotes.find(x=>x.start<=t&&t<x.end);
 return <AbsoluteFill style={{fontFamily:font,opacity:interpolate(t,[start,start+.2],[0,1],clamp)}}><Video src={staticFile('sources/podcast.mp4')} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><Audio src={staticFile('audio/podcast-part2-enhanced.m4a')} premountFor={fps} volume={Math.min(interpolate(t,[start,start+.2],[0,1],clamp),interpolate(t,[end-.2,end],[1,0],clamp))}/><div style={{position:'absolute',left:95,top:65,fontSize:25,fontWeight:800,color:cream,textShadow:shadow}}>FTI SIDE / EP 1 • PART 2</div>{q?<div style={{position:'absolute',left:200,right:200,top:670,textAlign:'center',whiteSpace:'pre-line',fontSize:58,fontWeight:900,color:cream,textShadow:shadow,borderLeft:`6px solid ${orange}`}}>{q.text.split('\n').map((line,i,all)=><div key={i} style={{color:i===all.length-1?orange:cream}}>{i===0?'“':''}{line}{i===all.length-1?'”':''}</div>)}</div>:<CaptionTrack pages={pages}/>}{plan.chapters.map(c=><Sequence key={c.start} from={Math.round(c.start*fps)} durationInFrames={Math.round(3.4*fps)} premountFor={fps}><div style={{position:'absolute',left:110,right:110,bottom:245,textAlign:'center',color:cream,textShadow:shadow,fontSize:70,fontWeight:900}}>{c.title.split(' ').slice(0,-1).join(' ')} <span style={{color:orange}}>{c.title.split(' ').slice(-1)[0]}</span></div></Sequence>)}{plan.images.map(im=><Sequence key={im.start} from={Math.round(im.start*fps)} durationInFrames={im.duration*fps} premountFor={fps}><Part2Documentation file={im.file} title={im.name}/></Sequence>)}</AbsoluteFill>;
};
const EndMusicCue=()=>{const f=useCurrentFrame();const {fps}=useVideoConfig();return <Audio src={staticFile('audio/part2-v5-groove.wav')} trimBefore={Math.round(24.01*fps)} premountFor={fps} volume={interpolate(f,[0,6,38,48],[0,.16,.16,.55],clamp)}/>;};
export const PartTwoV3=()=>{
 const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111'}}><Sequence durationInFrames={20*fps} premountFor={fps}><Part2Intro/></Sequence><Sequence from={Math.round(19.8*fps)} trimBefore={Math.round(1161.6*fps)} durationInFrames={712*fps} premountFor={fps}><Body start={1161.6} end={1873.6}/></Sequence><Sequence from={Math.round(731.6*fps)} trimBefore={Math.round(1907.2*fps)} durationInFrames={Math.round(372.7*fps)} premountFor={fps}><Body start={1907.2} end={2279.9}/></Sequence><Sequence from={Math.round(1104.3*fps)} durationInFrames={10*fps} premountFor={fps}><Part2Outro/></Sequence><Sequence from={Math.round(1098.91*fps)} durationInFrames={Math.round(5.39*fps)} premountFor={fps}><EndMusicCue/></Sequence></AbsoluteFill>;
};
const storyShots=[
 {at:.6,duration:4,start:260,file:'podcast.mp4',x:'22%',head:'KENAPA IKUT',accent:'ORGANISASI?',wide:false,recap:true,bridge:false},
 {at:4.6,duration:.6,start:1225.11,file:'podcast.mp4',x:'0%',head:'',accent:'',wide:false,recap:false,bridge:true},
 {at:5.2,duration:4,start:1225.71,file:'podcast.mp4',x:'0%',head:'JADI LEBIH',accent:'SERIUS & TEGAS.',wide:false,recap:false,bridge:false},
 {at:9.2,duration:5,start:1928.58,file:'podcast.mp4',x:'100%',head:'CONFIDENT AJA.',accent:'JUST ALL OUT!',wide:false,recap:false,bridge:false},
 {at:14.2,duration:5.5,start:2119.09,file:'podcast.mp4',x:'22%',head:'JANGAN LUPA',accent:'KOMITMEN KALIAN.',wide:false,recap:false,bridge:false},
 {at:19.7,duration:4.5,start:2185.46,file:'podcast.mp4',x:'83%',head:'BOLEH KURANG BENSIN…',accent:'JANGAN SAMPAI HABIS!',wide:false,recap:false,bridge:false},
 {at:24.2,duration:2.8,start:47.2,file:'opening.mp4',x:'50%',head:'FTI SIDE',accent:'PART 2',wide:true,recap:false,bridge:false},
];
const StoryClip=({shot,last}:{shot:typeof storyShots[number];last:boolean})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const duration=shot.duration*fps;const src=staticFile(`sources/${shot.file}`);
 return <AbsoluteFill style={{opacity:shot.recap?1:interpolate(f,[0,.16*fps],[0,1],clamp),overflow:'hidden'}}>
  <Video src={src} trimBefore={Math.round(shot.start*fps)} muted premountFor={fps} objectFit="cover" style={{width:'100%',height:'100%',objectPosition:shot.x,filter:shot.recap?'grayscale(1)':shot.wide?'blur(25px) brightness(.5)':undefined,scale:shot.wide?1:interpolate(f,[0,duration],[1,1.04],clamp)}}/>
  {shot.wide?<Video src={src} trimBefore={Math.round(shot.start*fps)} muted premountFor={fps} objectFit="contain" style={{position:'absolute',left:0,top:510,width:1080,height:608}}/>:null}
  <Audio src={staticFile(shot.file==='opening.mp4'?'audio/opening-v3-normalized.wav':shot.recap?'audio/podcast-normalized.m4a':'audio/podcast-part2-enhanced.m4a')} trimBefore={Math.round(shot.start*fps)} premountFor={fps} volume={shot.bridge?0:Math.min(interpolate(f,[0,2],[0,last?.6:1],clamp),interpolate(f,[duration-2,duration],[last?.6:1,0],clamp))}/>
  <AbsoluteFill style={{background:'linear-gradient(rgba(0,0,0,.3),transparent 40%,rgba(0,0,0,.87))'}}/>
  {!last&&!shot.bridge?<div style={{position:'absolute',left:75,top:315,color:orange,fontSize:27,fontWeight:800,letterSpacing:3}}>{shot.recap?'PART 1':'EPISODE 01 • PART 2'}</div>:null}
  {!shot.bridge?<div style={{position:'absolute',left:75,right:75,bottom:320,fontWeight:900,lineHeight:1.14,fontSize:last?108:shot.recap?76:70,textShadow:shadow,whiteSpace:'pre-line',opacity:last?interpolate(f,[7,15],[0,1],clamp):1,scale:.94+.06*spring({frame:last?f-7:f,fps,config:{damping:18}})}}><div>{shot.head}</div><div style={{color:orange,marginTop:12}}>{shot.accent}</div><div style={{marginTop:28,width:interpolate(f,[0,12],[0,150],clamp),height:7,background:orange}}/></div>:null}
  <Audio src={staticFile('audio/part2-v5-sweep.wav')} premountFor={fps} volume={.09}/>
 </AbsoluteFill>;
};
export const Part2Story=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111',fontFamily:font,color:cream}}>
  <Video src={staticFile('video/part2-rewind-v5.mp4')} durationInFrames={Math.round(.6*fps)} muted objectFit="cover" premountFor={fps} style={{width:'100%',height:'100%',filter:'grayscale(1)'}}/>
  {storyShots.map((s,i)=><Sequence key={s.at} from={Math.round(s.at*fps)} durationInFrames={Math.round((s.duration+(i<storyShots.length-1&&!s.bridge?.16:0))*fps)} premountFor={fps}><StoryClip shot={s} last={i===storyShots.length-1}/></Sequence>)}
  {f<24.2*fps?<div style={{position:'absolute',left:75,top:180,fontSize:55,fontWeight:900}}>FTI <span style={{color:orange}}>SIDE</span><div style={{fontSize:22,letterSpacing:2,marginTop:18}}>BEM FTI UNIVERSITAS TRISAKTI</div></div>:null}
  <Sequence durationInFrames={Math.round(4.6*fps)} premountFor={fps}><RewindButton portrait duration={4.6}/></Sequence>
  <Sequence from={Math.round(4.6*fps)} durationInFrames={Math.round(.6*fps)} premountFor={fps}><ForwardBridge portrait/></Sequence>
  <Sequence from={Math.round(24.2*fps)} durationInFrames={Math.round(.35*fps)} premountFor={fps}><ForwardBridge portrait/></Sequence>
  <Audio src={staticFile('audio/part2-v5-rewind.wav')} premountFor={fps} volume={.7}/>
  <Audio src={staticFile('audio/part2-v5-groove.wav')} premountFor={fps} volume={interpolate(f,[0,6,24.2*fps,24.6*fps,26.2*fps,27*fps],[0,.14,.14,.42,.42,0],clamp)}/>
  <AbsoluteFill style={{background:'black',opacity:interpolate(f,[26.6*fps,27*fps],[0,1],clamp)}}/>
 </AbsoluteFill>;
};
