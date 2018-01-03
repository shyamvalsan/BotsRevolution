import os, sys
from PIL import Image
size = 800, 600
os.chdir(sys.argv[1])
for fn in os.listdir('.'):
    print fn
    outfile = os.path.splitext(fn)[0] + "_resized"
    im = Image.open(fn)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save('../ResizedPhotos/'+outfile+".png")
