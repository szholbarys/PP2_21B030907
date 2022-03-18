s = input()
with open(s, "r") as fil:
    f = fil.read()
    
cnt = f.count("\n")
print(f"Numder of lines = {cnt+1}")