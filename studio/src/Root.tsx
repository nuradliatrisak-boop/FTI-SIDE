import {PartOne,PartTwo} from "./Episodes";
import {PartCard,NextEpisode} from "./PartCard";
import {Closing} from "./Closing";
import {Composition} from "remotion";
import {Opening,KineticHook,Question,TitleReveal} from "./Opening";
import { MyComposition } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <MyComposition />
      <Composition id="FTI-SIDE-PART-1" component={PartOne} width={1920} height={1080} fps={30} durationInFrames={35349}/>
      <Composition id="FTI-SIDE-PART-2" component={PartTwo} width={1920} height={1080} fps={30} durationInFrames={33351}/>
      <Composition id="Part-1-Card" component={PartCard} width={1920} height={1080} fps={30} durationInFrames={120} defaultProps={{part:1,title:"Kenapa Ikut Organisasi?"}}/>
      <Composition id="Part-2-Card" component={PartCard} width={1920} height={1080} fps={30} durationInFrames={120} defaultProps={{part:2,title:"Bertumbuh, Memimpin, Mengatur Waktu"}}/>
      <Composition id="Next-Episode" component={NextEpisode} width={1920} height={1080} fps={30} durationInFrames={150}/>
      <Composition id="FTI-SIDE-Closing" component={Closing} width={1920} height={1080} fps={30} durationInFrames={210}/>
      <Composition id="FTI-SIDE-Opening" component={Opening} width={1920} height={1080} fps={30} durationInFrames={480}/>
      <Composition id="KineticHook" component={KineticHook} width={1920} height={1080} fps={30} durationInFrames={60}/>
      <Composition id="Question" component={Question} width={1920} height={1080} fps={30} durationInFrames={60}/>
      <Composition id="TitleReveal" component={TitleReveal} width={1920} height={1080} fps={30} durationInFrames={90}/>
    </>
  );
};
