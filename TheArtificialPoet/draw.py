import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
index = 1 
static_hashtags="#poetry #poetsofinstagram #poem #instapic #love #instagood #photooftheday #beautiful #art #instadaily #life #amazing #instamood #instagram #motivation"

os.chdir(sys.argv[1])
for fn in os.listdir('.'):
    fn_list = fn.split('_')
    color = fn_list[0]
    pos = fn_list[1]
    base = Image.open(fn).convert('RGBA')
    #base = base_raw.filter(ImageFilter.GaussianBlur(radius=5))
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    '''
    fnt = ImageFont.truetype('SpecialElite.ttf', 30)
    d = ImageDraw.Draw(txt)
    d.text((50,300), "Out of the night that covers me,", font=fnt, fill=(0,0,0,255))
    d.text((50,340), "Black as the pit from pole to pole,", font=fnt, fill=(0,0,0,255))
    d.text((50,380), "I thank whatever gods may be", font=fnt, fill=(0,0,0,255))
    d.text((50,420), "For my unconquerable soul.,", font=fnt, fill=(0,0,0,255))

    '''
    out = Image.alpha_composite(base, txt)
    out.save('%s.png' % index)
    index = index + 1
