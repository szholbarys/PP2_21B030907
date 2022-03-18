import os
s = input()
print(os.path.isfile(s))


"""s = input()
with open(s, 'r') as fil:
    f = fil.read()
if f:
    print("This path readability")
else:
    print("This path NOT readability")
    
    
with open(s, "w") as fil2:
    if fil2:
        print("This path writability")
    else:
        print("This path NOT writanility")
        
with open(s, "a") as fil3:
    if fil3:
        print("This path executability")
    else:
        print("This path NOT executability")"""