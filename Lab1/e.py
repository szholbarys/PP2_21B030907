a, b = map(int,input().split())
if a > 500 or b % 2 != 0:
    print("Try next time!")
else:
    s = 0
    for i in range(2, a):
        if a % i == 0:
            s += 1
    if s == 0:
        print("Good job!")
    else:
        print("Try next time!")