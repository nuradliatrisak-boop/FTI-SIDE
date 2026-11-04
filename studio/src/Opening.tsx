import {Audio, Video} from '@remotion/media';
import {AbsoluteFill, Sequence, staticFile, useCurrentFrame, useVideoConfig, interpolate, spring} from 'remotion';

const navy='#092a49', orange='#ff8a46', cream='#fff5e5';
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'} as const;
const Base=({children}:{children:React.ReactNode})=><AbsoluteFill style={{background:navy,color:cream,fontFamily:'Arial, sans-serif',overflow:'hidden'}}>{children}</AbsoluteFill>;
export const KineticHook=()=>{
 const f=useCurrentFrame(); const {fps}=useVideoConfig();
 return <Base>
  <div style={{position:'absolute',left:140,top:115,fontSize:27,letterSpacing:5}}>BEM FTI UNIVERSITAS TRISAKTI</div>
  <div style={{position:'absolute',left:130,top:230,fontSize:250,fontWeight:900,lineHeight:.92,letterSpacing:-15,translate:`${interpolate(f,[0,13],[-1300,0],clamp)}px 0px`}}>FTI</div>
  <div style={{position:'absolute',right:145,top:470,fontSize:260,fontWeight:900,lineHeight:.92,color:orange,letterSpacing:-15,translate:`${interpolate(f,[10,28],[1300,0],clamp)}px 0px`}}>SIDE</div>
  <div style={{position:'absolute',right:220,top:250,width:220,height:220,border:`30px solid ${orange}`,borderRadius:'50%',scale:spring({frame:f-14,fps,config:{damping:12}})}}/>
  <div style={{position:'absolute',left:140,bottom:120,fontSize:34,letterSpacing:8}}>PODCAST / FTI</div>
 </Base>;
};
export const Question=()=>{
 const f=useCurrentFrame(); const {fps}=useVideoConfig();
 return <Base>
  <AbsoluteFill style={{background:orange,color:navy,padding:'130px 140px',justifyContent:'center'}}>
   <div style={{fontSize:220,fontWeight:900,letterSpacing:-13,lineHeight:1,scale:spring({frame:f,fps,config:{damping:13}})}}>24 JAM.</div>
   <div style={{fontSize:94,fontWeight:900,marginTop:35,translate:`${interpolate(f,[10,24],[1400,0],clamp)}px 0px`}}>MASIH KURANG?</div>
   <div style={{position:'absolute',right:145,top:140,fontSize:35,fontWeight:700,letterSpacing:6}}>FTI SIDE /</div>
  </AbsoluteFill>
 </Base>;
};
export const TitleReveal=()=>{
 const f=useCurrentFrame(); const {fps}=useVideoConfig();
 return <Base>
  <div style={{position:'absolute',right:-220,top:-240,width:800,height:800,border:`100px solid ${orange}`,borderRadius:'50%',scale:interpolate(f,[0,90],[.8,1.05],clamp)}}/>
  <div style={{position:'absolute',left:140,top:155,fontSize:32,letterSpacing:7}}>BEM FTI UNIVERSITAS TRISAKTI</div>
  <div style={{position:'absolute',left:130,top:350,fontSize:245,fontWeight:900,letterSpacing:-15,lineHeight:1,scale:spring({frame:f,fps,config:{damping:18}})}}>FTI <span style={{color:orange}}>SIDE</span></div>
  <div style={{position:'absolute',left:145,top:660,width:1450,height:7,background:orange,scale:interpolate(f,[4,25],[0,1],clamp),transformOrigin:'left'}}/>
  <div style={{position:'absolute',left:145,top:735,fontSize:47,letterSpacing:3,opacity:interpolate(f,[15,32],[0,1],clamp)}}>SISI LAIN CERITA FTI.</div>
  <div style={{position:'absolute',left:145,bottom:100,fontSize:25,letterSpacing:5}}>FAKULTAS TEKNOLOGI INDUSTRI / UNIVERSITAS TRISAKTI</div>
 </Base>;
};
export const Opening=()=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();
 return <Base>
  <Sequence name="Kinetic FTI SIDE" durationInFrames={2*fps} premountFor={fps}><KineticHook/></Sequence>
  <Sequence name="Montage kiri" from={2*fps} durationInFrames={2*fps} premountFor={fps}>
   <Video src={staticFile('sources/opening.mp4')} trimBefore={40*fps} muted premountFor={fps} style={{width:'100%',height:'100%',scale:1.65,transformOrigin:'30% 50%'}}/>
   <div style={{position:'absolute',left:130,bottom:125,padding:'16px 28px',background:orange,color:navy,fontSize:73,fontWeight:900,rotate:'-3deg'}}>CERITA.</div>
  </Sequence>
  <Sequence name="Montage kanan" from={4*fps} durationInFrames={2*fps} premountFor={fps}>
   <Video src={staticFile('sources/opening.mp4')} trimBefore={49*fps} muted premountFor={fps} style={{width:'100%',height:'100%',scale:1.5,transformOrigin:'76% 48%'}}/>
   <div style={{position:'absolute',right:130,bottom:125,padding:'16px 28px',background:cream,color:navy,fontSize:73,fontWeight:900,rotate:'3deg'}}>PERSPEKTIF.</div>
  </Sequence>
  <Sequence name="Split peserta" from={6*fps} durationInFrames={2*fps} premountFor={fps}>
   <div style={{position:'absolute',inset:'0 50% 0 0',overflow:'hidden',borderRight:`12px solid ${orange}`}}><Video src={staticFile('sources/opening.mp4')} trimBefore={34*fps} muted premountFor={fps} style={{height:'100%',width:1920,maxWidth:'none',position:'absolute',left:-110,scale:1.15}}/></div>
   <div style={{position:'absolute',inset:'0 0 0 50%',overflow:'hidden'}}><Video src={staticFile('sources/opening.mp4')} trimBefore={46*fps} muted premountFor={fps} style={{height:'100%',width:1920,maxWidth:'none',position:'absolute',left:-880,scale:1.15}}/></div>
   <div style={{position:'absolute',left:130,top:110,fontSize:28,fontWeight:700,background:navy,padding:'15px 24px',letterSpacing:5}}>FTI SIDE / ON AIR</div>
  </Sequence>
  <Sequence name="Pertanyaan utama" from={8*fps} durationInFrames={2*fps} premountFor={fps}><Question/></Sequence>
  <Sequence name="Reaksi bersama" from={10*fps} durationInFrames={3*fps} premountFor={fps}>
   <Video src={staticFile('sources/opening.mp4')} trimBefore={48*fps} muted premountFor={fps} style={{width:'100%',height:'100%'}}/>
   <AbsoluteFill style={{background:'linear-gradient(transparent 50%, rgba(9,42,73,.85))'}}/>
   <div style={{position:'absolute',left:130,bottom:120,fontSize:110,fontWeight:900,letterSpacing:-4}}>LET’S TALK<span style={{color:orange}}>.</span></div>
  </Sequence>
  <Sequence name="Identitas utama" from={13*fps} durationInFrames={3*fps} premountFor={fps}><TitleReveal/></Sequence>
  <Audio src={staticFile('audio/fti-side-ident-original.wav')} premountFor={fps} volume={interpolate(f,[0,10,14*fps,16*fps],[0,.65,.65,0],clamp)}/>
 </Base>;
};
