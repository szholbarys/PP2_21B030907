n = int(input())
for i in range (n):
    a = str(input())
    if(a[len(a) - 10 : len(a)] == "@gmail.com"):
        print(a[0: len(a) - 10])