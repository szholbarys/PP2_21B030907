import os

s = input()
if os.path.isfile(s):
    os.remove(s)
else:
    print("File not found!")