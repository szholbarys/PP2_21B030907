# n = int(input())
# a = [w for w in range(2, n) if not w % 2]
# print(*a)

n = int(input())

def geneven(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
it = geneven(n)
print(*it, sep = ",")
