demon = {}
hunter = {}
t = int(input())
for i in range(t):
    a, b = input().split()
    if b not in demon:
        demon[b] = 1
    else:
        demon[b] = demon[b] + 1
for _ in range(int(input())):
    h, s, c = input().split()
    if s not in hunter:
        hunter[s] = int(c)
    else:
        hunter[s] = hunter[s] + int(c)

sum = 0
for i in demon:
    for j in hunter:
        if i == j and demon[i] > hunter[j]:
            sum = sum + hunter[j]
        elif i == j and demon[i] <= hunter[j]:
            sum = sum + demon[i]

print("Demons left:",t - sum)
