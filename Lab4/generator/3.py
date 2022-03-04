# n = int(input())
# a = [i for i in range(1, n) if i % 3 == 0 and i % 4 == 0]
# print(*a)
n = int(input())

def func(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
it = func(n)
print(*it)