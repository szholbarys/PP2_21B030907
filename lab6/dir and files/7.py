path1 = r"C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab6\dir and files\practice1.txt"
with open(path1, "r") as readd:
    read = readd.read()
    
path2 = r"C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab6\dir and files\practice2.txt"
with open(path2, "w") as write:
    for i in read:
        write.write(i)