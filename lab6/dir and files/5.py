s = input()
l = input().split()
with open(s, "w") as fil:
    fil.write(f"n = {str(len(l))} \n[")
    for i in l:
        fil.write("%s, " %i)
    fil.write("]")