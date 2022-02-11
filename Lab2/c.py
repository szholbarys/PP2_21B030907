n = int(input())
a1 = []
for i in range(n):
    a2 = []
    for j in range(n):
        if i == j and i != 0 and j != 0:
            a2.append(i*j)
        elif i == 0:
            a2.append(j)
        elif j == 0:
            a2.append(i)
        else:
            a2.append("0")
    a1.append(a2)        
for i in range(len(a1)):
    print(*a1[i])