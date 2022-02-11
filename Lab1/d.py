n = int(input())
z = str(input())
if(z == 'k'):
    b = int(input())
    print(round(n/1024, b))
elif(z == 'b'):
    print(n * 1024)