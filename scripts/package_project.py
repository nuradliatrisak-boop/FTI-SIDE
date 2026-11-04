"""Create a source project archive; original footage and models stay separate."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]
target=root/'deliverables/FTI-SIDE-REMOTION-PROJECT.zip'
with ZipFile(target,'w',compression=ZIP_DEFLATED,compresslevel=6) as z:
 for folder in ['studio/src','scripts']:
  for p in (root/folder).rglob('*'):
   if p.is_file() and '__pycache__' not in p.parts:z.write(p,p.relative_to(root))
 for name in ['package.json','package-lock.json','tsconfig.json','remotion.config.ts','eslint.config.mjs','.gitignore','README.md']:
  p=root/'studio'/name
  if p.exists():z.write(p,p.relative_to(root))
 for p in (root/'docs').glob('*'):
  if p.is_file() and p.suffix in ['.md','.txt','.csv'] and p.stat().st_size<2_000_000:z.write(p,p.relative_to(root))
 for name in ['edit-plan.json','podcast.metadata.json','opening.metadata.json','transcript-corrections.json','whisper-model-verification.json','whisper-large-model-verification.json','subtitle-review-corrections.json','subtitle-formatting-corrections.json']:
  p=root/'docs'/name
  if p.exists():z.write(p,p.relative_to(root))
 for p in (root/'docs/subtitle-review').glob('*.json'):
  z.write(p,p.relative_to(root))
 for name in ['captions-merged.json','pages.json','QC-REPORT.json']:
  p=root/'revisions/v1'/name
  if p.exists():z.write(p,p.relative_to(root))
 p=root/'studio/public/audio/fti-side-ident-original.wav';z.write(p,p.relative_to(root))
 for folder in ['docs/revision-v3','studio/public/images']:
  for p in (root/folder).rglob('*'):
   if p.is_file() and p.suffix not in ['.log','.wav']:z.write(p,p.relative_to(root))
 for p in (root/'studio/public/audio').glob('*v3*.wav'):z.write(p,p.relative_to(root))
 for p in (root/'deliverables').glob('*'):
  if p.is_file() and p.suffix in ['.srt','.txt','.csv','.md','.json']:z.write(p,p.relative_to(root))
print(target,target.stat().st_size,'bytes')
