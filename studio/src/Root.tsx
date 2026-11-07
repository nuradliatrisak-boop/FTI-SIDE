import {Part1StoryV3} from './Part1StoryV3';
import {PartOneV3,OpeningPart1V3,PauseOutroPart1V3,AisyahInsert,PaperMobInsert} from "./Part1RevisionV3";
import {PartTwoV3,Part2Intro,Part2Outro,Part2Story} from "./Part2RevisionV3";
import {PartCard,NextEpisode} from "./PartCard";
import {Closing} from "./Closing";
import {Composition} from "remotion";
import {Opening,KineticHook,Question,TitleReveal} from "./Opening";
import { MyComposition } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <MyComposition />
      <Composition id="Part2-Intro-V3" component={Part2Intro} width={1920} height={1080} fps={30} durationInFrames={600}/>
      <Composition id="Part2-Outro-V3" component={Part2Outro} width={1920} height={1080} fps={30} durationInFrames={300}/>
      <Composition id="Part2-Story-V3" component={Part2Story} width={1080} height={1920} fps={30} durationInFrames={960}/>
      <Composition id="Part1-Instagram-Story-V3" component={Part1StoryV3} width={1080} height={1920} fps={30} durationInFrames={900}/>
      <Composition id="Part1-Opening-V3" component={OpeningPart1V3} width={1920} height={1080} fps={30} durationInFrames={678}/>
      <Composition id="Part1-Pause-Outro-V3" component={PauseOutroPart1V3} width={1920} height={1080} fps={30} durationInFrames={240}/>
      <Composition id="Part1-Aisyah-Insert" component={AisyahInsert} width={1920} height={1080} fps={30} durationInFrames={45}/>
      <Composition id="Part1-Paper-Mob-Insert" component={PaperMobInsert} width={1920} height={1080} fps={30} durationInFrames={150}/>
      <Composition id="FTI-SIDE-PART-1" component={PartOneV3} width={1920} height={1080} fps={30} durationInFrames={33972}/>
      <Composition id="FTI-SIDE-PART-2" component={PartTwoV3} width={1920} height={1080} fps={30} durationInFrames={33429}/>
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
