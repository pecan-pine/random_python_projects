import os, shelve
from pathlib import Path
#change directory to test folder
os.chdir('/home/uriel/Documents/test')
#verify correct directory
#print(Path.cwd())
#open file with capitals list
capitals = open('capitals.csv')
#make file into a list
lines = capitals.readlines()
#next, break apart entries across the ',' to make small lists
for s in lines:
    lines[lines.index(s)] = s.split(',')
#create an empty dictionary then add in the entries using the above
#small lists
capital = {}
for s in lines:
    state = lines[lines.index(s)][0]
    city = lines[lines.index(s)][1]
    capital[state]= city
#print(capital['Oklahoma'])


