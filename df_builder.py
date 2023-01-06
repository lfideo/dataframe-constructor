import os
import shutil
import glob
import pandas as pd
import numpy as np

# prints current directory
print(os.getcwd())

# changes current directory
os.chdir('/Users/lfideo/Downloads')

# lists files in cwd
# os.listdir()
for file in os.listdir():
    if file.find('data')==0 and len(file)<=20:        
        shutil.move(file, "/Users/lfideo/Desktop/***/crm/data")

# change the cwd
os.chdir("/Users/lfideo/Desktop/***/crm/data")   

# define the path
path = os.getcwd()
file_list = glob.glob(path + '/*.csv')     

li = []
for file in file_list:
    df = pd.read_csv(file, dtype='object', index_col=None, header=0)
    li.append(df)

crm = pd.concat(li, axis=0, ignore_index=True)