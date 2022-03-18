import os 

s = input()

isFile = os.path.exists(s) 
if isFile:
    with open(s, "r") as f:
        ff = f.readline()
    print(os.path.basename(s))
    print(f"direcroty portion = {ff}")
else:
    print("Not found")