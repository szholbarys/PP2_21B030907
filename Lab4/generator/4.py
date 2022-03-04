# a = int(input())
# b = int(input())
# a = [i for i in range(a, b) if not i % 2]
# print(a)
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
        
a, b = map(int, input().split())
g = squares(a, b)
print(*g)