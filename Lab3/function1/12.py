def f(n):
    for i in range(len(n)):
        for j in range(n[i]):
            print("*" , end = "")
        print()


n = list(map( int , input().split()))   

f(n)