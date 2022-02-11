def myrec(t):
    a = 0
    for i in t:
        a += ord(i)
    if(a > 300):
        print("It is tasty!")
    else:
        print("Oh, no!")
s = str(input())
myrec(s)


