from itertools import permutations

def f(a):
    p = permutations(a)
    for i in p:
        for j in i:
            print(j , end = "")
        print()

a = str(input())          

print(f(a))