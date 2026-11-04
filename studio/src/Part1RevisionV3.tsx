import {Audio,Video} from '@remotion/media';
import {AbsoluteFill,CanvasImage,Sequence,interpolate,spring,staticFile,useCurrentFrame,useVideoConfig} from 'remotion';
import {CaptionTrack} from './CaptionTrack';
import pages from './data/part1-pages-v3.json';
const orange='#ff8948',cream='#fff8ed';
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'} as const;
const font='DejaVu Sans, Arial, sans-serif';
const shadow='0 5px 22px rgba(0,0,0,.8)';
const Cursor=({size=90}:{size?:number})=><svg width={size} height={size} viewBox="0 0 100 100"><path d="M12 7 L78 55 L50 61 L68 89 L52 98 L34 68 L16 88 Z" fill="white" stroke="#101820" strokeWidth="5"/></svg>;
const Sticker=({children}:{children:React.ReactNode})=><div style={{display:'inline-block',padding:'12px 23px',background:orange,color:'#101820',fontWeight:900,rotate:'-3deg',boxShadow:'8px 8px 0 rgba(0,0,0,.4)'}}>{children}</div>;
const Bumper=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111',fontFamily:font,color:cream,overflow:'hidden'}}>
  <Video src={staticFile('sources/opening.mp4')} durationInFrames={1.5*fps} trimBefore={48*fps} muted premountFor={fps} objectFit="cover" style={{width:'100%',height:'100%'}}/>
  <Video src={staticFile('sources/opening.mp4')} from={1.5*fps} durationInFrames={1.5*fps} trimBefore={40*fps} muted premountFor={fps} style={{width:'100%',height:'100%',scale:1.25,transformOrigin:'20% 55%'}}/>
  <Video src={staticFile('sources/opening.mp4')} from={3*fps} durationInFrames={1.5*fps} trimBefore={49*fps} muted premountFor={fps} style={{width:'100%',height:'100%',scale:1.25,transformOrigin:'85% 55%'}}/>
  <Video src={staticFile('sources/opening.mp4')} from={4.5*fps} durationInFrames={1.5*fps} trimBefore={35*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <AbsoluteFill style={{background:'linear-gradient(rgba(0,0,0,.3),transparent 40%,rgba(0,0,0,.5))'}}/>
  <div style={{position:'absolute',left:95,top:80,fontSize:26,letterSpacing:5,fontWeight:700}}>BEM FTI UNIVERSITAS TRISAKTI</div>
  {f<45?<div style={{position:'absolute',left:105,bottom:110,fontSize:190,fontWeight:900,letterSpacing:-12,lineHeight:.95,scale:spring({frame:f,fps,config:{damping:13,stiffness:130}}),textShadow:shadow}}>FTI <span style={{color:orange}}>SIDE</span><div style={{width:interpolate(f,[6,25],[0,1150],clamp),height:12,background:orange,marginTop:20}}/></div>:f<90?<div style={{position:'absolute',left:110,bottom:130,fontSize:80,translate:`${interpolate(f,[45,54],[-1200,0],clamp)}px 0px`}}><Sticker>CERITA KAMPUS.</Sticker></div>:f<135?<div style={{position:'absolute',right:110,bottom:130,fontSize:80,translate:`${interpolate(f,[90,99],[1200,0],clamp)}px 0px`}}><Sticker>TANPA FILTER.</Sticker></div>:<div style={{position:'absolute',left:105,bottom:100,textShadow:shadow,scale:spring({frame:f-135,fps,config:{damping:14}})}}><div style={{fontSize:150,fontWeight:900,letterSpacing:-7}}>24 JAM.</div><div style={{fontSize:76,fontWeight:800,color:orange}}>MASIH KURANG?</div></div>}
 </AbsoluteFill>;
};
const NewTake=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const t=f/fps;
 const person=t>=41.36&&t<42.68?'NADYA':t>=42.68&&t<43.60?'GHIVARIEL':t>=43.60&&t<44.50?'KINAN':t>=44.50&&t<45.70?'CAHAYA':null;
 const start=person==='NADYA'?41.36:person==='GHIVARIEL'?42.68:person==='KINAN'?43.60:44.50;
 const zoom=person?1.62:1;const cx=person==='NADYA'?1650:person==='GHIVARIEL'?590:person==='KINAN'?1340:280;
 const tx=person?Math.max(1920*(1-zoom),Math.min(0,960-cx*zoom)):0;const ty=person?-310:0;
 const pop=spring({frame:(t-start)*fps,fps,config:{damping:16,stiffness:190}});
 const subtitle=t>=32.92&&t<33.96?'Halo guys!':t>=34.20&&t<35.10?'Pernah gak sih kalian':t>=35.10&&t<36.40?'24 jam itu':t>=36.40&&t<37.96?'enggak cukup buat kita semua?':t>=38.32&&t<40.14?'So, di sini kita akan kupas tuntas.':t>=41.36&&t<42?'Perkenalin, gue':null;
 return <AbsoluteFill style={{background:'#111',overflow:'hidden',fontFamily:font,color:cream}}>
  <Video src={staticFile('sources/opening.mp4')} muted premountFor={fps} style={{width:'100%',height:'100%',transformOrigin:'0 0',translate:`${tx}px ${ty}px`,scale:zoom}}/>
  <Audio src={staticFile('audio/opening-v3-normalized.wav')} premountFor={fps}/>
  {person?<div style={{position:'absolute',left:person==='CAHAYA'?1100:110,bottom:170,fontSize:person==='GHIVARIEL'?76:100,fontWeight:900,textShadow:shadow,scale:pop,rotate:person==='CAHAYA'?'3deg':'-3deg'}}><div style={{fontSize:24,letterSpacing:6,marginBottom:14}}>KENALIN DULU.</div><Sticker>{person}</Sticker></div>:null}
  {subtitle?<div style={{position:'absolute',left:200,right:200,bottom:75,textAlign:'center',fontSize:43,fontWeight:700,textShadow:shadow}}><span style={{background:'rgba(0,0,0,.70)',padding:'10px 22px',borderRadius:7}}>{subtitle}</span></div>:null}
  {t>=45.7&&t<48.55?<div style={{position:'absolute',left:100,right:100,bottom:130,textAlign:'center',fontWeight:900,textShadow:shadow,scale:spring({frame:(t-45.7)*fps,fps,config:{damping:13}})}}><div style={{fontSize:42,letterSpacing:8}}>AND WELCOME TO</div><div style={{fontSize:155,letterSpacing:-8}}>FTI <span style={{color:orange}}>SIDE!</span></div></div>:null}
 </AbsoluteFill>;
};
export const OpeningPart1V3=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill>
  <Sequence name="Montage pembuka baru" durationInFrames={6*fps} premountFor={fps}><Bumper/></Sequence>
  <Sequence name="Take opening baru + perkenalan" from={6*fps} trimBefore={32.8*fps} durationInFrames={16.6*fps} premountFor={fps}><NewTake/></Sequence>
  <Audio src={staticFile('audio/part1-v3-groove.wav')} durationInFrames={22.6*fps} premountFor={fps} volume={interpolate(f,[0,8,5.6*fps,6*fps,18.5*fps,19*fps,21.8*fps,22.6*fps],[0,.8,.8,.10,.10,.20,.20,0],clamp)}/>
  <Audio src={staticFile('audio/part1-v3-pop.wav')} from={14.56*fps} premountFor={fps} volume={.22}/>
  <Audio src={staticFile('audio/part1-v3-pop.wav')} from={15.48*fps} premountFor={fps} volume={.22}/>
  <Audio src={staticFile('audio/part1-v3-pop.wav')} from={16.4*fps} premountFor={fps} volume={.22}/>
  <Audio src={staticFile('audio/part1-v3-pop.wav')} from={17.3*fps} premountFor={fps} volume={.22}/>
  <Audio src={staticFile('audio/part1-v3-sweep.wav')} from={21.8*fps} premountFor={fps} volume={.28}/>
 </AbsoluteFill>;
};
export const AisyahInsert=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const p=spring({frame:f,fps,config:{damping:15,stiffness:120}});
 return <AbsoluteFill style={{fontFamily:font,color:cream}}><div style={{position:'absolute',left:730,top:interpolate(f,[0,15],[850,125],clamp),width:460,rotate:'-2deg',opacity:interpolate(f,[0,5,150,168],[0,1,1,0],clamp),scale:.88+.12*p,background:cream,padding:14,boxShadow:'0 20px 55px rgba(0,0,0,.5)'}}><div style={{height:555,overflow:'hidden',position:'relative'}}><CanvasImage src={staticFile('images/aisyah-original.jpg')} premountFor={fps} style={{position:'absolute',width:828,height:1026,left:-220,top:-310}}/></div><div style={{color:'#151515',fontSize:39,fontWeight:900,padding:'14px 10px 0'}}>KAK AISYAH</div><div style={{color:'#333',fontSize:23,padding:'4px 10px 12px'}}>WAKABEM · Wakil Ketua BEM</div></div><Audio src={staticFile('audio/part1-v3-pop.wav')} premountFor={fps} volume={.3}/></AbsoluteFill>;
};
export const PaperMobInsert=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const x=interpolate(f,[0,12],[1350,690],clamp);
 return <AbsoluteFill style={{fontFamily:font,color:cream}}><div style={{position:'absolute',left:x,top:100,width:540,rotate:'2deg',opacity:interpolate(f,[0,7,222,240],[0,1,1,0],clamp),filter:'drop-shadow(0 20px 32px rgba(0,0,0,.6))'}}><CanvasImage src={staticFile('images/paper-mob-instagram.jpg')} premountFor={fps} style={{width:540,borderRadius:16}}/><div style={{marginTop:12,fontSize:31,fontWeight:800,textShadow:shadow}}>@bemftiusakti<br/>@pkkmbftitrisakti</div></div><div style={{position:'absolute',left:interpolate(f,[18,36],[1470,1110],clamp),top:interpolate(f,[18,36],[900,590],clamp),scale:interpolate(f,[36,41,47],[1,.82,1],clamp)}}><Cursor/></div>{f>=38&&f<58?<div style={{position:'absolute',left:1110-(f-38)*3,top:590-(f-38)*3,width:(f-38)*6,height:(f-38)*6,border:`6px solid ${orange}`,borderRadius:'50%',opacity:1-(f-38)/20}}/>:null}<Audio src={staticFile('audio/part1-v3-pop.wav')} from={1.2*fps} premountFor={fps} volume={.3}/></AbsoluteFill>;
};
const Quote=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <div style={{position:'absolute',left:180,right:180,bottom:200,textAlign:'center',fontFamily:font,fontSize:66,fontWeight:900,color:cream,textShadow:shadow,scale:spring({frame:f,fps,config:{damping:18}})}}>“Terbentur, terbentur,<br/>dan <span style={{color:orange}}>terbentuk.</span>”</div>;
};
export const PodcastPart1V3=({sourceStart,sourceEnd}:{sourceStart:number;sourceEnd:number})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const t=f/fps;
 const fadeIn=interpolate(t,[sourceStart,sourceStart+.2],[0,1],clamp);const gain=Math.min(fadeIn,interpolate(t,[sourceEnd-.2,sourceEnd],[1,0],clamp));
 return <AbsoluteFill style={{background:'transparent',opacity:fadeIn,fontFamily:font}}>
  <Video src={staticFile('sources/podcast.mp4')} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
  <Audio src={staticFile('audio/podcast-normalized.m4a')} premountFor={fps} volume={gain}/>
  <div style={{position:'absolute',left:95,top:65,color:cream,fontSize:25,fontWeight:800,textShadow:shadow}}>FTI SIDE / PART 1</div>
  {t<30.3?<div style={{position:'absolute',left:110,right:110,bottom:235,textAlign:'center',color:cream,textShadow:shadow,opacity:interpolate(t,[27,27.2,29.8,30.3],[0,1,1,0],clamp)}}><div style={{fontSize:26,letterSpacing:8,color:orange}}>PART 01</div><div style={{fontSize:78,fontWeight:900}}>Kenapa Ikut Organisasi?</div></div>:null}
  {t<475.74||t>=479?<CaptionTrack pages={pages}/>:null}
  <Sequence name="Kak Aisyah" from={101.8*fps} durationInFrames={5.6*fps} premountFor={fps}><AisyahInsert/></Sequence>
  <Sequence name="Paper mob di Instagram" from={1089.4*fps} durationInFrames={8*fps} premountFor={fps}><PaperMobInsert/></Sequence>
  <Sequence name="Kutipan" from={475.74*fps} durationInFrames={Math.round(3.25*fps)} premountFor={fps}><Quote/></Sequence>
  <Audio name="Aksen tiga nada" src={staticFile('audio/part1-v3-three-notes.wav')} from={787*fps} premountFor={fps} volume={.13}/>
 </AbsoluteFill>;
};
export const PauseOutroPart1V3=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <AbsoluteFill style={{fontFamily:font,color:cream,overflow:'hidden'}}>
  <CanvasImage src={staticFile('images/part1-v3-pause-frame.jpg')} premountFor={fps} style={{width:'100%',height:'100%',scale:interpolate(f,[0,8*fps],[1,1.035],clamp)}}/>
  <AbsoluteFill style={{background:'linear-gradient(transparent,rgba(0,0,0,.72))'}}/>
  <div style={{position:'absolute',left:850,top:260,width:220,height:160,background:'rgba(0,0,0,.38)',borderRadius:32,display:'flex',justifyContent:'center',alignItems:'center',gap:25,scale:interpolate(f,[0,12,18],[1,.88,1],clamp)}}><div style={{width:24,height:90,background:cream}}/><div style={{width:24,height:90,background:cream}}/></div>
  <div style={{position:'absolute',left:interpolate(f,[0,12],[1480,995],clamp),top:interpolate(f,[0,12],[700,350],clamp)}}><Cursor size={100}/></div>
  <div style={{position:'absolute',left:140,right:140,top:500,textAlign:'center',textShadow:shadow,opacity:interpolate(f,[18,30],[0,1],clamp)}}><div style={{fontSize:58,fontWeight:700}}>Penasaran selanjutnya?</div><div style={{fontSize:105,fontWeight:900,marginTop:20}}>SAKSIKAN <span style={{color:orange}}>PART 2</span></div><div style={{fontSize:32,marginTop:40}}>FTI SIDE · BEM FTI UNIVERSITAS TRISAKTI</div></div>
  <Audio src={staticFile('audio/part1-v3-groove.wav')} trimBefore={28*fps} premountFor={fps} volume={interpolate(f,[0,.3*fps,6.5*fps,8*fps],[0,.55,.55,0],clamp)}/>
  <Audio src={staticFile('audio/part1-v3-pop.wav')} from={.4*fps} premountFor={fps} volume={.4}/>
 </AbsoluteFill>;
};
export const PartOneV3=()=>{
 const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#111'}}>
  <Sequence name="Opening baru" durationInFrames={22.6*fps} premountFor={fps}><OpeningPart1V3/></Sequence>
  <Sequence name="Pembicaraan awal" from={22.4*fps} trimBefore={27*fps} durationInFrames={568.6*fps} premountFor={fps}><PodcastPart1V3 sourceStart={27} sourceEnd={595.6}/></Sequence>
  <Sequence name="Ekspektasi organisasi" from={590.8*fps} trimBefore={607.1*fps} durationInFrames={234.9*fps} premountFor={fps}><PodcastPart1V3 sourceStart={607.1} sourceEnd={842}/></Sequence>
  <Sequence name="Pengalaman dan cerita" from={825.5*fps} trimBefore={862.7*fps} durationInFrames={298.9*fps} premountFor={fps}><PodcastPart1V3 sourceStart={862.7} sourceEnd={1161.6}/></Sequence>
  <Sequence name="Pause ke Part 2" from={1124.4*fps} durationInFrames={8*fps} premountFor={fps}><PauseOutroPart1V3/></Sequence>
 </AbsoluteFill>;
};
