n = int(input())
arr = []

for i in range(n):
    nums = list(map(int, input().split())) # or nums = input().split()
    arr.append(nums)

# print(a[0][0])

for i in range(len(arr)):
 print(arr[i])    