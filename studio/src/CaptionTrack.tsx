import type {Caption} from '@remotion/captions';
import {interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
export type CaptionPage={startMs:number;endMs:number;words:Caption[]};
export const CaptionTrack=({pages}:{pages:CaptionPage[]})=>{
 const f=useCurrentFrame();const {fps}=useVideoConfig();const time=f/fps*1000;
 let lo=0,hi=pages.length-1,found:CaptionPage|undefined;
 while(lo<=hi){const mid=(lo+hi)>>1;const page=pages[mid];if(time<page.startMs)hi=mid-1;else if(time>=page.endMs)lo=mid+1;else{found=page;break;}}
 if(!found)return null;
 return <div style={{position:'absolute',left:210,right:210,bottom:75,textAlign:'center',fontFamily:'Arial, sans-serif',fontWeight:600,fontSize:46,lineHeight:1.3,opacity:interpolate(time,[found.startMs,found.startMs+65],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}}>
  <span style={{display:'inline-block',background:'rgba(5,20,33,.84)',padding:'12px 24px',borderRadius:8,color:'#fff',maxWidth:'100%'}}>{found.words.map((w,i)=><span key={i} style={{color:/^(FTI|SIDE|BEM|ARKA|waktu|organisasi|akademik|kepemimpinan)[.,!?]?$/i.test(w.text.trim())?'#ffad70':'#fff'}}>{w.text}</span>)}</span>
 </div>;
};
