# n = int(input())
# a = [i ** 2 for i in range(1, n)]
# print(*a)
import random
import math

def generator_sqrt(n):
    for i in range(n):
        k = int(math.sqrt(i))
        if k*k==i:
            yield i
a = int(input())
n = random.randrange(1, a)
it = generator_sqrt(n)
print(*it)