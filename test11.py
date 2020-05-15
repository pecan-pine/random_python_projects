import os, shelve
from pathlib import Path
os.chdir('/home/uriel/Documents')
shelfFile = shelve.open('mydata')
cats = ['Lucy','Tuna','Captain']
shelfFile['cats'] = cats
shelfFile.close()