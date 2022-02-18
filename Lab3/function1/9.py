import math

k = math.pi

def f(r):
    v = 4 * (k) * r * r * r / 3 

    return v

r = int(input())

print(f(r))