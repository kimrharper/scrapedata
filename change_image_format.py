import os
from PIL import Image

folder_list = []
for filename in os.listdir("scraper/images/tcc/."):
    if filename != '.DS_Store':
        folder_list.append(filename)

for folder in folder_list:
    path = "scraper/images/tcc/"
    fpath = folder+'/'
    for file in os.listdir(path+folder+'/.'):
        old_name = path+fpath+file
        print(old_name)
        new_image = Image.open(old_name)
        new_image.save(old_name[0:-3] + 'bmp', 'bmp')
        os.remove(old_name)