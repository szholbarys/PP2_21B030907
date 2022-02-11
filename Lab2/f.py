money = {}
m = 0
n = int(input())
for i in range (n):
    a, b = input().split()
    if a not in money:
        money[a] = int(b)
        if m < int(b):
            m = int(b)
    else:
        money[a] = money[a] + int(b)
        if m < money[a]:
            m = money[a]
s = sorted(money)
for k in s:
    if(m == money[k]):
        print(k, "is lucky!")
    else:
        print(k, "has to receive", m - money[k], "tenge")