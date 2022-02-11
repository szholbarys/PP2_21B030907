n = int(input())
a1 = []
if n % 2 == 0:
    for i in range(n):
        a2 = []
        for j in range(n):
            if i == j or i > j:
                a2.append("#")
            else:
                a2.append(".")   
        a1.append(a2)
if n % 2 == 1:
    for i in range(n):
        a2 = []
        for j in range(n):
            if i + j == n - 1 or i + j > n - 1:
                a2.append("#")
            else:
                a2.append(".")   
        a1.append(a2)
for i in range(len(a1)):
    print(*a1[i],sep = "")
    