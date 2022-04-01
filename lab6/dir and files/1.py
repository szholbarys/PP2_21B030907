import os

s = input()
with open(s, "r") as fil:
    f = fil.read()
#print(dir(f))    
if os.path.isDir(f):
    print('it is true Dir')
elif os.path.isFile(f):
    print('it is true File')
else:
    print('its false Path')    