import {AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {Audio} from '@remotion/media';
import {staticFile} from 'remotion';
export const Closing=()=>{
 const f=useCurrentFrame(); const {fps}=useVideoConfig();
 return <AbsoluteFill style={{background:'#092a49',color:'#fff5e5',fontFamily:'Arial, sans-serif',padding:'155px 145px',justifyContent:'center',opacity:interpolate(f,[0,15,6*fps,7*fps],[0,1,1,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}}>
  <div style={{fontSize:31,letterSpacing:6}}>TERIMA KASIH SUDAH MENONTON</div>
  <div style={{fontSize:200,fontWeight:900,letterSpacing:-12,marginTop:45,lineHeight:1}}>FTI <span style={{color:'#ff8a46'}}>SIDE</span></div>
  <div style={{height:6,width:1350,background:'#ff8a46',marginTop:60,marginBottom:40}}/>
  <div style={{fontSize:43,letterSpacing:1}}>BEM FTI UNIVERSITAS TRISAKTI</div>
  <div style={{fontSize:29,color:'#9ac4e3',letterSpacing:5,marginTop:25}}>KABINET ARKA</div>
  <Audio src={staticFile('audio/fti-side-ident-original.wav')} trimBefore={8*fps} durationInFrames={7*fps} premountFor={fps} volume={interpolate(f,[0,15,5*fps,7*fps],[0,.4,.4,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}/>
 </AbsoluteFill>;
};
