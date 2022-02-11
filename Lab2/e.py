n = input().split()
if len(n) == 1:
    n = int(n[0])
    x = int(input())
else:
    n, x = int(n[0]), int(n[1])
xor = x
for i in range(1, n):
    xor = xor ^ (x + 2 * i)
print(xor)