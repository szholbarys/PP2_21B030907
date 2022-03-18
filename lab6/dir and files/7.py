path1 = "D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab6\Dir and files\practice\copy1.txt"
with open(path1, "r") as readd:
    read = readd.read()
    
path2 = "D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab6\Dir and files\practice\copy2.txt"
with open(path2, "w") as write:
    for i in read:
        write.write(i)