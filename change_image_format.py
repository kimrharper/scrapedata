import os
from PIL import Image
from PIL.ImageOps import invert, grayscale
import numpy as np


path = "scraper/images/practice/"
fpath = '/'
selector = '.'

def convert_img(path, resize=False):
    img = Image.open(path)
    img = img.convert('L')
    img = img.resize((79, 65))
    img = invert(img)
    img = img.convert('1')
    img.save(path[0:-3] + 'png','png')
    os.remove(path)

for f in os.listdir(path + selector):
    if f[-3:] in ['png','bmp']:
        convert_img(path + f)
    elif f[0] != '.':
        folder = path + f + fpath
        [convert_img(folder + file) for file in os.listdir(folder + selector)]