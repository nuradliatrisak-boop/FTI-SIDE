import {Audio,Video} from '@remotion/media';
import {AbsoluteFill,CanvasImage,Sequence,staticFile,useCurrentFrame,useVideoConfig,interpolate,spring} from 'remotion';
import {CaptionTrack} from './CaptionTrack';
import pages from './data/part2-pages-v3.json';
import plan from './data/part2-plan-v3.json';
const orange='#ff8948',cream='#fff8ed',font='DejaVu Sans, Arial, sans-serif';
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'} as const;
const shadow='0 5px 20px rgba(0,0,0,.85)';
const BodyFootage=({start,enhanced=false,volume=1}:{start:number;enhanced?:boolean;volume?:number})=>{
 const {fps}=useVideoConfig();const f=useCurrentFrame();
 return <AbsoluteFill><Video src={staticFile('sources/podcast.mp4')} trimBefore={Math.round(start*fps)} muted objectFit="cover" premountFor={fps} style={{width:'100%',height:'100%'}}/><Audio src={staticFile(enhanced?'audio/podcast-part2-enhanced.m4a':'audio/podcast-normalized.m4a')} trimBefore={Math.round(start*fps)} premountFor={fps} volume={Math.min(volume,interpolate(f,[0,3],[0,volume],clamp))}/></AbsoluteFill>;
};
const CaptionRibbon=({label,text}:{label:string;text:string})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{fontFamily:font,color:cream}}><AbsoluteFill style={{background:'linear-gradient(transparent 35%,rgba(0,0,0,.75))'}}/><div style={{position:'absolute',left:95,top:65,fontSize:25,fontWeight:800,letterSpacing:3,background:'rgba(0,0,0,.6)',padding:'12px 20px',borderLeft:`7px solid ${orange}`}}>{label}</div><div style={{position:'absolute',left:105,right:105,bottom:115,fontSize:78,fontWeight:900,textShadow:shadow,whiteSpace:'pre-line',scale:.94+.06*spring({frame:f,fps,config:{damping:18}})}}>{text}</div></AbsoluteFill>;
};
export const Part2Intro=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111',fontFamily:font,color:cream}}>
  <Sequence durationInFrames={Math.round(4.2*fps)} premountFor={fps}><BodyFootage start={260}/><CaptionRibbon label="SEBELUMNYA / PART 1" text={'KENAPA IKUT\nORGANISASI?'}/></Sequence>
  <Sequence from={4*fps} durationInFrames={4*fps} premountFor={fps}><BodyFootage start={475.6}/><CaptionRibbon label="SEBELUMNYA / PART 1" text={'“TERBENTUR, TERBENTUR,\nDAN TERBENTUK.”'}/></Sequence>
  <Sequence from={8*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/opening.mp4')} trimBefore={48*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><CaptionRibbon label="EPISODE 01 • PART 2" text={'CERITANYA\nBELUM SELESAI.'}/></Sequence>
  <Sequence from={11*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/podcast.mp4')} trimBefore={1259*fps} muted premountFor={fps} style={{width:'100%',height:'100%',scale:1.18,transformOrigin:'75% 50%'}}/><CaptionRibbon label="EPISODE 01 • PART 2" text={'JADI LEBIH BERANI.'}/></Sequence>
  <Sequence from={14*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/podcast.mp4')} trimBefore={1609*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><CaptionRibbon label="EPISODE 01 • PART 2" text={'PROKER. KULIAH.\nPRIORITAS.'}/></Sequence>
  <Sequence from={17*fps} durationInFrames={3*fps} premountFor={fps}><Video src={staticFile('sources/opening.mp4')} trimBefore={46*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><AbsoluteFill style={{background:'linear-gradient(transparent,rgba(0,0,0,.75))'}}/><div style={{position:'absolute',left:100,bottom:115,textShadow:shadow}}><div style={{fontSize:32,fontWeight:800,letterSpacing:7}}>EPISODE 01 · BERTUMBUH BARENG</div><div style={{fontSize:160,fontWeight:900,letterSpacing:-8}}>FTI SIDE <span style={{color:orange}}>PART 2</span></div></div></Sequence>
  <Audio src={staticFile('audio/part2-v3-groove.wav')} premountFor={fps} volume={interpolate(f,[0,10,7.7*fps,8*fps,19.5*fps,20*fps],[0,.12,.12,.7,.7,0],clamp)}/>
  <Audio src={staticFile('audio/part2-v3-sweep.wav')} from={8*fps} premountFor={fps} volume={.23}/>
  <Audio src={staticFile('audio/part2-v3-pop.wav')} from={17*fps} premountFor={fps} volume={.25}/>
 </AbsoluteFill>;
};
export const Part2Outro=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111',fontFamily:font,color:cream}}>
  <Video src={staticFile('sources/opening.mp4')} durationInFrames={3*fps} trimBefore={48*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <Video src={staticFile('sources/podcast.mp4')} from={3*fps} durationInFrames={3*fps} trimBefore={2274*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <Video src={staticFile('sources/opening.mp4')} from={6*fps} durationInFrames={4*fps} trimBefore={46*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <AbsoluteFill style={{background:'linear-gradient(transparent 30%,rgba(0,0,0,.82))'}}/>
  <div style={{position:'absolute',left:105,right:105,bottom:100,textShadow:shadow}}><div style={{fontSize:40,fontWeight:700,letterSpacing:4}}>MAKASIH SUDAH NONTON!</div><div style={{fontSize:142,fontWeight:900,letterSpacing:-6}}>FTI <span style={{color:orange}}>SIDE</span></div><div style={{fontSize:33,fontWeight:700}}>@bemftiusakti · BEM FTI UNIVERSITAS TRISAKTI</div><div style={{fontSize:24,letterSpacing:6,marginTop:22}}>EPISODE 01 • KABINET ARKA</div></div>
  <Audio src={staticFile('audio/part2-v3-groove.wav')} trimBefore={26*fps} premountFor={fps} volume={interpolate(f,[0,10,8.5*fps,10*fps],[0,.6,.6,0],clamp)}/>
  <AbsoluteFill style={{background:'black',opacity:interpolate(f,[9.2*fps,10*fps],[0,1],clamp)}}/>
 </AbsoluteFill>;
};
export const Part2Documentation=({file,title}:{file:string;title:string})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{fontFamily:font}}><div style={{position:'absolute',left:735,top:interpolate(f,[0,.35*fps],[1050,90],clamp),width:450,height:820,background:'#11181e',border:`3px solid ${orange}`,borderRadius:15,boxShadow:'0 20px 45px rgba(0,0,0,.5)',opacity:interpolate(f,[0,6,7.8*fps,8*fps],[0,1,1,0],clamp)}}><div style={{fontSize:22,fontWeight:800,color:orange,letterSpacing:3,padding:'16px 18px'}}>DOKUMENTASI PROKER</div><CanvasImage src={staticFile(`images/${file}`)} premountFor={fps} style={{position:'absolute',left:15,top:53,width:420,height:650,objectFit:'contain'}}/><div style={{position:'absolute',left:20,right:20,top:717,color:cream,fontSize:24,fontWeight:800,whiteSpace:'pre-line',lineHeight:1.1}}>{title.replace(' • ','\n')}</div><div style={{position:'absolute',left:20,top:777,color:orange,fontSize:25,fontWeight:700}}>@bemftiusakti</div></div><Audio src={staticFile('audio/part2-v3-pop.wav')} premountFor={fps} volume={.18}/></AbsoluteFill>;
};
const Body=({start,end}:{start:number;end:number})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const t=f/fps;const q=plan.quotes.find(x=>x.start<=t&&t<x.end);
 return <AbsoluteFill style={{fontFamily:font,opacity:interpolate(t,[start,start+.2],[0,1],clamp)}}><Video src={staticFile('sources/podcast.mp4')} muted premountFor={fps} style={{width:'100%',height:'100%'}}/><Audio src={staticFile('audio/podcast-part2-enhanced.m4a')} premountFor={fps} volume={Math.min(interpolate(t,[start,start+.2],[0,1],clamp),interpolate(t,[end-.2,end],[1,0],clamp))}/><div style={{position:'absolute',left:95,top:65,fontSize:25,fontWeight:800,color:cream,textShadow:shadow}}>FTI SIDE / EP 1 • PART 2</div>{q?<div style={{position:'absolute',left:200,right:200,top:670,textAlign:'center',whiteSpace:'pre-line',fontSize:58,fontWeight:900,color:cream,textShadow:shadow,borderLeft:`6px solid ${orange}`}}>“{q.text}”</div>:<CaptionTrack pages={pages}/>}{plan.chapters.map(c=><Sequence key={c.start} from={Math.round(c.start*fps)} durationInFrames={Math.round(3.4*fps)} premountFor={fps}><div style={{position:'absolute',left:110,right:110,bottom:245,textAlign:'center',color:cream,textShadow:shadow,fontSize:70,fontWeight:900}}>{c.title}</div></Sequence>)}{plan.images.map(im=><Sequence key={im.start} from={Math.round(im.start*fps)} durationInFrames={im.duration*fps} premountFor={fps}><Part2Documentation file={im.file} title={im.name}/></Sequence>)}</AbsoluteFill>;
};
export const PartTwoV3=()=>{
 const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111'}}><Sequence durationInFrames={20*fps} premountFor={fps}><Part2Intro/></Sequence><Sequence from={Math.round(19.8*fps)} trimBefore={Math.round(1161.6*fps)} durationInFrames={712*fps} premountFor={fps}><Body start={1161.6} end={1873.6}/></Sequence><Sequence from={Math.round(731.6*fps)} trimBefore={Math.round(1907.2*fps)} durationInFrames={Math.round(372.7*fps)} premountFor={fps}><Body start={1907.2} end={2279.9}/></Sequence><Sequence from={Math.round(1104.3*fps)} durationInFrames={10*fps} premountFor={fps}><Part2Outro/></Sequence></AbsoluteFill>;
};
const storyShots=[
 {at:0,duration:3.9,start:260,file:'podcast.mp4',x:'22%',head:'SEBELUMNYA…',accent:'KENAPA IKUT ORGANISASI?',wide:false,recap:true},
 {at:3.9,duration:3.9,start:475.6,file:'podcast.mp4',x:'75%',head:'“TERBENTUR, TERBENTUR,',accent:'DAN TERBENTUK.”',wide:false,recap:true},
 {at:7.8,duration:3,start:1259.52,file:'podcast.mp4',x:'83%',head:'DULU INTROVERT.',accent:'SEKARANG?',wide:false,recap:false},
 {at:10.8,duration:6,start:1489.45,file:'podcast.mp4',x:'100%',head:'DI BALIK',accent:'SEBUAH PROKER.',wide:false,recap:false},
 {at:16.8,duration:5.5,start:2119.09,file:'podcast.mp4',x:'50%',head:'JANGAN LUPA',accent:'KOMITMEN KALIAN.',wide:true,recap:false},
 {at:22.3,duration:4.5,start:2185.46,file:'podcast.mp4',x:'83%',head:'BOLEH KURANG BENSIN…',accent:'JANGAN SAMPAI HABIS!',wide:false,recap:false},
 {at:26.8,duration:5.2,start:48,file:'opening.mp4',x:'50%',head:'LANJUTKAN CERITANYA.',accent:'FTI SIDE\nEPISODE 01 • PART 2',wide:true,recap:false},
];
const StoryClip=({shot,last}:{shot:typeof storyShots[number];last:boolean})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const duration=shot.duration*fps;const src=staticFile(`sources/${shot.file}`);
 return <AbsoluteFill style={{opacity:shot.at===0?1:interpolate(f,[0,.2*fps],[0,1],clamp),overflow:'hidden'}}><Video src={src} trimBefore={Math.round(shot.start*fps)} muted premountFor={fps} objectFit="cover" style={{width:'100%',height:'100%',objectPosition:shot.x,filter:shot.wide?'blur(25px) brightness(.5)':undefined,scale:interpolate(f,[0,duration],[1,1.04],clamp)}}/>{shot.wide?<Video src={src} trimBefore={Math.round(shot.start*fps)} muted premountFor={fps} objectFit="contain" style={{position:'absolute',left:0,top:510,width:1080,height:608}}/>:null}<Audio src={staticFile(shot.file==='opening.mp4'?'audio/opening-v3-normalized.wav':shot.recap?'audio/podcast-normalized.m4a':'audio/podcast-part2-enhanced.m4a')} trimBefore={Math.round(shot.start*fps)} premountFor={fps} volume={last?0:Math.min(interpolate(f,[0,3],[0,1],clamp),interpolate(f,[duration-3,duration],[1,0],clamp))}/><AbsoluteFill style={{background:'linear-gradient(rgba(0,0,0,.3),transparent 40%,rgba(0,0,0,.87))'}}/><div style={{position:'absolute',left:75,top:315,color:orange,fontSize:27,fontWeight:800,letterSpacing:3}}>{shot.recap?'THROWBACK • PART 1':'EPISODE 01 • PART 2'}</div><div style={{position:'absolute',left:75,right:75,bottom:320,fontWeight:900,lineHeight:1.14,fontSize:shot.recap?66:70,textShadow:shadow,whiteSpace:'pre-line',scale:.94+.06*spring({frame:f,fps,config:{damping:18}})}}><div>{shot.head}</div><div style={{color:orange,marginTop:12}}>{shot.accent}</div><div style={{marginTop:28,width:interpolate(f,[0,12],[0,150],clamp),height:7,background:orange}}/></div><Audio src={staticFile('audio/part2-v3-sweep.wav')} premountFor={fps} volume={.1}/></AbsoluteFill>;
};
export const Part2Story=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111',fontFamily:font,color:cream}}>{storyShots.map((s,i)=><Sequence key={s.at} from={Math.round(s.at*fps)} durationInFrames={Math.round((s.duration+(i<storyShots.length-1?.2:0))*fps)} premountFor={fps}><StoryClip shot={s} last={i===storyShots.length-1}/></Sequence>)}<div style={{position:'absolute',left:75,top:180,fontSize:55,fontWeight:900}}>FTI <span style={{color:orange}}>SIDE</span><div style={{fontSize:22,letterSpacing:2,marginTop:18}}>BEM FTI UNIVERSITAS TRISAKTI</div></div><Audio src={staticFile('audio/part2-v3-groove.wav')} premountFor={fps} volume={interpolate(f,[0,10,26.8*fps,27.2*fps,31*fps,32*fps],[0,.14,.14,.6,.6,0],clamp)}/><AbsoluteFill style={{background:'black',opacity:interpolate(f,[31.5*fps,32*fps],[0,1],clamp)}}/></AbsoluteFill>;
};
