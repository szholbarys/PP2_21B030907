n = list(map(int, input().split()))

list = []

def f(n):

    for i in range(len(n)):
        if n[i] not in list:
            list.append(n[i])

    return list

print(*(f(n)))