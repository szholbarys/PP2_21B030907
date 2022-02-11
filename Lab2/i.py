n = int(input())
discs = []
discs2 = []
cnt = 0
for i in range(n):
    l = list(map(str, input().split()))
    if l[0] == '1':
        discs.append(l[1])
    elif l[0] == '2':
        discs2.append(discs[0 + cnt])
        cnt += 1
print(*discs2)           