a = list(map(int, input().split()))
pos = len(a) - 1

for i in range(len(a) - 2, -1, -1):
    if i + a[i] >= pos:
        pos = i
if pos == 0:
    print(1)
else:
    print(0)                