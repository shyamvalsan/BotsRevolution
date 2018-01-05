from PIL import Image, ImageDraw, ImageFont, ImageFilter
# get an image and blur it
base = Image.open('RenamedPhotos/b_middle_DSC09926_resized.png').convert('RGBA')
#base = base_raw.filter(ImageFilter.GaussianBlur(radius=5))

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('SpecialElite.ttf', 30)
# get a drawing context
d = ImageDraw.Draw(txt)

l1=(50,300)
# add text
d.text(l1, "Out of the dasdad,", font=fnt, fill=(0,0,0,255))
d.text((50,340), "Black as the pit from pole to pole,", font=fnt, fill=(0,0,0,255))
d.text((50,380), "I thank whatever gods may be", font=fnt, fill=(0,0,0,255))
d.text((50,420), "For my unconquerable soul.,", font=fnt, fill=(0,0,0,255))
#d.text((50,480), "1234567891234567891234567891234567891234", font=fnt, fill=(0,0,0,255))
#d.text((50,520), "1234567891234567891234567891234567891234", font=fnt, fill=(0,0,0,255))
#d.text((200,200), "World", font=fnt, fill=(0,0,0,255))

# create composite
out = Image.alpha_composite(base, txt)

# save image
out.save('poem1.png')
