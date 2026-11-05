"""Thumbnail typography over one real frame. No image generation or face edits."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps
root=Path(__file__).resolve().parents[1]
out=root/'deliverables/thumbnails';out.mkdir(parents=True,exist_ok=True)
photo=Image.open(root/'studio/public/images/thumbnail-ep1-original-source.jpg').convert('RGB')
ORANGE='#ff8948';CREAM='#fff8ed'
def font(n):return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf',n)
def label(im,xy,text,n,fill=CREAM):ImageDraw.Draw(im).text(xy,text,font=font(n),fill=fill,stroke_width=1,stroke_fill=fill)
def pill(im,xy,text,n=30):
 d=ImageDraw.Draw(im);b=d.textbbox((0,0),text,font=font(n));w=b[2]+46;h=n+28;x,y=xy;d.rounded_rectangle((x,y,x+w,y+h),radius=h//2,fill=ORANGE);d.text((x+23,y+8),text,font=font(n),fill='#111820')
def fade(im,top=True):
 w,h=im.size;layer=Image.new('RGBA',(w,h));p=layer.load()
 for y in range(h):
  a=int(230*max(0,1-y/400)) if top else int(200*max(0,(y-(h-170))/170))
  if a:
   ImageDraw.Draw(layer).line((0,y,w,y),fill=(8,13,19,a))
 return Image.alpha_composite(im.convert('RGBA'),layer).convert('RGB')
# Horizontal: photograph stays at its original 1920x1080 size; graphics stay off faces.
h=fade(fade(photo.copy()),False)
label(h,(76,45),'FTI',56);label(h,(181,45),'SIDE',56,ORANGE)
pill(h,(1430,58),'EP 01  •  PART 1',28)
label(h,(72,142),'IKUT ORMAWA,',112)
label(h,(72,267),'IKUT PUSING?',112,ORANGE)
d=ImageDraw.Draw(h);d.rounded_rectangle((78,411,310,419),radius=4,fill=ORANGE)
label(h,(78,1005),'BEM FTI UNIVERSITAS TRISAKTI',29)
h.save(out/'FTI-SIDE-EP1-PART1-HORIZONTAL.png')
# Portrait: same complete, unretouched group frame; blur only the decorative backdrop.
bg=ImageOps.fit(photo,(1080,1920),method=Image.Resampling.LANCZOS).filter(ImageFilter.GaussianBlur(40))
v=ImageEnhance.Brightness(bg).enhance(.19)
label(v,(68,116),'FTI',102);label(v,(259,116),'SIDE',102,ORANGE)
pill(v,(72,276),'EPISODE 01  •  PART 1',36)
label(v,(67,400),'IKUT ORMAWA,',100)
label(v,(67,526),'IKUT PUSING?',104,ORANGE)
d=ImageDraw.Draw(v);d.rounded_rectangle((74,681,276,689),radius=4,fill=ORANGE)
group=photo.resize((1080,608),Image.Resampling.LANCZOS)
v.paste(group,(0,787))
d=ImageDraw.Draw(v);d.rectangle((0,780,1080,787),fill=ORANGE);d.rectangle((0,1395,1080,1402),fill=ORANGE)
label(v,(73,1510),'NADYA • GHIVARIEL',44)
label(v,(73,1574),'KINAN • CAHAYA',44)
d=ImageDraw.Draw(v);d.line((74,1696,1004,1696),fill='#4e4f4d',width=2)
label(v,(73,1750),'BEM FTI',34)
label(v,(73,1800),'UNIVERSITAS TRISAKTI',34)
v.save(out/'FTI-SIDE-EP1-PART1-VERTIKAL.png')
print('Created horizontal 1920x1080 and vertical 1080x1920 from opening source at 48 seconds. Real frame preserved.')
