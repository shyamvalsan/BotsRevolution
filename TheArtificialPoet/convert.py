import os
from PIL import Image

os.chdir('ReadyToPost/')
for fn in os.listdir('.'):
   im = Image.open(fn)
   im = im.convert("RGB")
   fn_list = fn.split('_')
   index = fn_list[0]
   author = fn_list[1]
   im.save('%s_%s.jpg' % (index,author))
