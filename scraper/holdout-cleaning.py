import os
import pandas as pd
import shutil

path = "images/nov-11-dataset/ch_hold_out"
split = ['character_classification', 'script_classification']
temp = "images/temp/"
fpath = '/'
selector = '.'

# shutil.move(temp+f+".png", path+f)
# os.rename(filename, filename[7:])


# HOLD OUT FOR CHARACTERS
old_l =[]
new_l = []

for f in os.listdir(path + fpath + 'character_classification' + selector):
    old_l.append(f)

hold_out = pd.DataFrame(data=None,index=None, columns=['old_fn','new_fn'])
hold_out['old_fn'] = old_l
hold_out =hold_out.sample(frac=1).reset_index()
del hold_out['index']
ind = hold_out.index
new_l = ['char_'+'{:03}'.format(i)+'.png' for i in ind]
hold_out['new_fn'] = new_l


# HOLD OUT FOR SCRIPT
old_l =[]
new_l = []

for f in os.listdir(path + fpath + 'script_classification' + selector):
    for g in os.listdir(path + fpath + 'script_classification' + fpath + f + selector):
        if len(g)>8:
            old_l.append(f+fpath+g)
hold_out2 = pd.DataFrame(data=None,index=None, columns=['old_fn','new_fn'])
hold_out2['old_fn'] = old_l
hold_out2 =hold_out2.sample(frac=1).reset_index()
del hold_out2['index']
ind = hold_out2.index
new_l = ['script_'+'{:03}'.format(i)+'.png' for i in ind]
hold_out2['new_fn'] = new_l


root = path + fpath + 'character_classification' + fpath
for i in range(len(hold_out['old_fn'])):
    os.rename(root+hold_out['old_fn'][i], root+hold_out['new_fn'][i])

root = path + fpath + 'script_classification' + fpath
for i in range(len(hold_out2['old_fn'])):
    os.rename(root+hold_out2['old_fn'][i], root+hold_out2['new_fn'][i])


hold_out.to_csv('char_hold_out.csv')
hold_out2.to_csv('script_hold_out.csv')