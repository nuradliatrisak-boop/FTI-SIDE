import {AbsoluteFill,interpolate,useCurrentFrame} from 'remotion';
export const PartCard=({part,title}:{part:number;title:string})=>{
 const f=useCurrentFrame();
 return <AbsoluteFill style={{background:'#092a49',color:'#fff5e5',fontFamily:'Arial, sans-serif',padding:'150px 145px',justifyContent:'center'}}>
  <div style={{fontSize:34,color:'#ff8a46',letterSpacing:6,fontWeight:700}}>FTI SIDE / PART {part}</div>
  <div style={{fontSize:100,fontWeight:800,lineHeight:1.15,maxWidth:1500,marginTop:50,opacity:interpolate(f,[0,12],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}}>{title}</div>
  <div style={{width:180,height:7,background:'#ff8a46',marginTop:55}}/>
  <div style={{fontSize:29,letterSpacing:3,marginTop:45}}>BEM FTI UNIVERSITAS TRISAKTI</div>
 </AbsoluteFill>;
};
export const NextEpisode=()=> <AbsoluteFill style={{background:'#092a49',color:'#fff5e5',fontFamily:'Arial, sans-serif',padding:'160px 145px',justifyContent:'center'}}>
 <div style={{fontSize:33,color:'#ff8a46',letterSpacing:6}}>LANJUT DI PART 2</div>
 <div style={{fontSize:100,fontWeight:800,lineHeight:1.2,marginTop:45}}>Bertumbuh. Memimpin.<br/>Mengatur waktu.</div>
 <div style={{fontSize:35,marginTop:55}}>Masih banyak cerita yang belum selesai.</div>
</AbsoluteFill>;
