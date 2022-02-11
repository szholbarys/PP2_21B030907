a = input()
l = list(map(int, input().split()))
l.sort()
print(l[len(l) - 2] * l[len(l) - 1]) 
