di1 = {}
for _ in range(int(input())):
    a = str(input())
    s1,s2,s3 = 0,0,0
    for t in a:
        if 'a' <= t and t <= 'z':
            s1 = 1
        elif 'A' <= t and t <= 'Z':
            s2 = 1
        elif '0' <= t and t <= '9':
            s3 = 1
    if s1 + s2 + s3 == 3:
        di1[a] = a
print(len(di1))
t = sorted(di1)
for i in t:
    print(i)