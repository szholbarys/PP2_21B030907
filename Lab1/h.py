n = str(input())
k = str(input())
s = 0
r = 0
t = 0
for i in range(0, len(n)):
    if k == n[i]:
        t += 1
        r = i;
for i in range(0, len(n)):
    if k == n[i]:
        s = i;
        break
        
if t == 1:
    print(r)
elif t > 1:
    print(s, r)