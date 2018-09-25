import pandas as pd

newfile = pd.DataFrame(columns=['id','char','link'])
newfile.loc[1]= ([1,'chinese','www.google.com'])

print(newfile)