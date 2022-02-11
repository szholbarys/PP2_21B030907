d=1
arr=[]
while d!=0: 
    s=int(input())
    if s!=0: 
        arr.append(s)
    d=s
    
if len(arr)%2==0:
    for i in range(len(arr)//2):
        print(arr[i]+arr[len(arr)-1-i], end=" ")
elif len(arr)%2==1:
    for i in range(len(arr)//2):
        print(arr[i]+arr[len(arr)-1-i],end=" ")
    print(arr[len(arr)//2])
