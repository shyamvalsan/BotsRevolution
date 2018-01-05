import subprocess
import random, os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

cmd20 = "awk -F\"|\" '$11 == 20{print}' ../poem_db.csv | sort -R | head -n 1"
cmd40 = "awk -F\"|\" '$11 == 40{print}' ../poem_db.csv | sort -R | head -n 1"

os.chdir(sys.argv[1])
for fn in os.listdir('.'):
 fnr = random.choice([x for x in os.listdir('.')])
 fnr_list = fnr.split('_')
 color = fnr_list[0]
 if color == "w":
    clr = (255,255,255,255)
 elif color == "b":
    clr = (0,0,0,255)
 else:
    print "Incorrect filename"
 pos = fnr_list[1]
 if pos == "top":
    pos1,pos2,pos3,pos4,cmd=(50,100),(50,140),(50,180),(50,220),cmd40
 elif pos == "bottom":
    pos1,pos2,pos3,pos4,cmd=(50,400),(50,440),(50,480),(50,520),cmd40
 elif pos == "middle":
    pos1,pos2,pos3,pos4,cmd=(50,300),(50,340),(50,380),(50,420),cmd40
 elif pos == "topl":
    pos1,pos2,pos3,pos4,cmd=(50,100),(50,140),(50,180),(50,220),cmd20
 elif pos == "topr":
    pos1,pos2,pos3,pos4,cmd=(320,100),(320,140),(320,180),(320,220),cmd20
 elif pos == "bottoml":
    pos1,pos2,pos3,pos4,cmd=(50,360),(50,400),(50,440),(50,480),cmd20
 elif pos == "bottomr":
    pos1,pos2,pos3,pos4,cmd=(320,360),(320,400),(320,440),(320,480),cmd20
 else:
    print "Incorrect filename"

 row = subprocess.check_output(cmd, shell=True)
 index = row.split('|')[0]
 author_name = row.split('|')[1]
 author_bio = row.split('|')[2]
 poem_type = row.split('|')[3]
 poem_context = row.split('|')[4]
 poem_line1 = row.split('|')[5]
 poem_line2 = row.split('|')[6]
 poem_line3 = row.split('|')[7]
 poem_line4 = row.split('|')[8]
 poem_specific_hashtags = row.split('|')[9]

 base = Image.open(fnr).convert('RGBA')
 txt = Image.new('RGBA', base.size, (255,255,255,0))
 fnt = ImageFont.truetype('../SpecialElite.ttf', 30)
 d = ImageDraw.Draw(txt)
 d.text(pos1, poem_line1, font=fnt, fill=clr)
 d.text(pos2, poem_line2, font=fnt, fill=clr)
 d.text(pos3, poem_line3, font=fnt, fill=clr)
 d.text(pos4, poem_line4, font=fnt, fill=clr)
 out = Image.alpha_composite(base, txt)
 rand = random.randint(1,9999)
 out.save('../ReadyToPost/%s_%s_%d.png' % (index,author_name,rand))
# im = Image.open('%s_%s.png' % (index,author_name))
# im.save('../ReadyToPost/%s_%s.jpg' % (index,author_name))
# os.remove('%s_%s.png' % (index,author_name))

 caption = "\n" + poem_type + " by " + author_name + "\n" + author_bio + "\n" + poem_context + "\n" + poem_specific_hashtags 
 text_file = open('../ReadyToPost/%s_%s.txt' % (index,author_name), 'wb')
 text_file.write(caption)
 text_file.close()

