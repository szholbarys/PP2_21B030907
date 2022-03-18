def f(x):
    return all(x)

t = tuple(input().split())
print(f(t))
"""
def f1(x):
    for i in x:
        if i == 0 or i == "False":
            return False
    return True
"""