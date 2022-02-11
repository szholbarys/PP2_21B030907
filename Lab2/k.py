a = input()
s = list(set(a.split()))

s.sort()
print(len(s))
for i in s:
    if i.isalpha():
        print(i)
    else:
        print(i[:-1])
