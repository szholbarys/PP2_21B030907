import math
a1, a2 = map(int, input().split())

def func(cor):
    return math.sqrt((a1-cor[0])**2 + (a2-cor[1])**2)


n = int(input())
cor = []
for i in range(n):
    cor.append(tuple(map(int, input().split())))
    
cor.sort(key = func)
for i in cor:
    print(*i)
