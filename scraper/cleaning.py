import os
import shutil
from PIL import Image
from PIL.ImageOps import invert, grayscale
import numpy as np


path = "images/ch_train/"
temp = "images/temp/"
fpath = '/'
selector = '.'

print(os.path)

i=0

sc = []
small_chars = []

# move rootimages into subfolder and find folders with less than 10 images:
for f in os.listdir(path + selector):
    if f[0] != '.':
        shutil.move(temp+f+".png", path+f)
        total = len(os.listdir(path+f+fpath+selector))
        print(total)
        if total < 10:
            sc.append(f)
            small_chars.append(path+f+fpath)

for i in small_chars:
    shutil.move(i, "images/unused/")