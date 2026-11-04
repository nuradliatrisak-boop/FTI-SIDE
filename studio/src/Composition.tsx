import {AbsoluteFill, Composition, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

export const OpeningDesign = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const settle = spring({frame: f - 10, fps, config: {damping: 15, stiffness: 95}});
  return <AbsoluteFill style={{background: '#092a49', color: '#fff6e7', fontFamily: 'Arial, sans-serif', overflow: 'hidden'}}>
    <AbsoluteFill style={{background: 'radial-gradient(ellipse at 85% 90%, #215f8f 0%, transparent 65%)'}} />
    <div style={{position: 'absolute', width: 690, height: 690, border: '100px solid #ff8a46', borderRadius: '50%', right: -180, top: -200, scale: interpolate(f, [0, 60, 300], [0.2, 1, 1.12], {extrapolateRight:'clamp'}), rotate: `${f * 0.12}deg`}} />
    <div style={{position:'absolute', left:140, top:115, display:'flex', gap:18, alignItems:'center', fontSize:26, letterSpacing:5, fontWeight:700}}><span style={{width:14,height:14,borderRadius:'50%',background:'#ff8a46'}}/> BEM FTI UNIVERSITAS TRISAKTI</div>
    <div style={{position:'absolute',left:128,top:250, fontSize:250, fontWeight:900, letterSpacing:-16,lineHeight:0.95,translate:`${(1-settle)*-1050}px 0px`,rotate:`${(1-settle)*-9}deg`}}>FTI <span style={{color:'#ff8a46'}}>SIDE</span></div>
    <div style={{position:'absolute',left:143, top:540, width:interpolate(f,[45,85],[0,1300],{extrapolateLeft:'clamp',extrapolateRight:'clamp'}),height:7,background:'#ff8a46'}}/>
    <div style={{position:'absolute',left:145,top:610,fontSize:53,fontWeight:600,letterSpacing:1,opacity:interpolate(f,[65,90],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'}),translate:`0px ${interpolate(f,[65,95],[35,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}px`}}>Percakapan. Perspektif. Koneksi.</div>
    <div style={{position:'absolute',left:145,bottom:120,fontSize:25,letterSpacing:6,color:'#8db7d7'}}>PODCAST / FAKULTAS TEKNOLOGI INDUSTRI</div>
    <div style={{position:'absolute',right:155,bottom:150,width:135,height:135,rotate:`${interpolate(f,[0,300],[-25,65])}deg`}}><div style={{position:'absolute',left:55,width:25,height:135,background:'#ff8a46'}}/><div style={{position:'absolute',top:55,width:135,height:25,background:'#ff8a46'}}/></div>
    <AbsoluteFill style={{background:'#ff8a46',translate:`${interpolate(f,[0,10,22], [0,0,2100],{extrapolateRight:'clamp'})}px 0px`}} />
    <AbsoluteFill style={{background:'#092a49',opacity:interpolate(f,[280,300],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}} />
  </AbsoluteFill>;
};

export const MyComposition = () => <Composition id="FTI-SIDE-Opening-Design" component={OpeningDesign} width={1920} height={1080} fps={30} durationInFrames={300}/>;
