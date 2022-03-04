#14
def prime(list):
    cnt = 0
    list1 = []
    for i in range(len(list)):
        cnt = 0
        for j in range(1 ,list[i]):
            if list[i] % j == 0:
                cnt += 1
        if cnt == 1:
            list1.append(list[i])
    return list1
n = input().split()
x = 0
list = []
for i in range(len(n)):
    list.append(int(n[i]))
print(*(prime(list)))



def f(list):
    for i in list:
        list1.append(i)
    return list1
s = input().split()
list = []
list1 = []
for i in range(len(s)):
    list.append(s[i])
list.reverse()
print(*(f(list)))



import math
k = math.pi
def f(r):
    v = 4 * (k) * r * r * r / 3 
    return v
r = int(input())
print(f(r))



def Pali(s):
    t = ""
    for i in s:
        t = i + t
    if t == s:
        return True
    else:
        return False
s = input()
if Pali(s) == True:
    print("Palindrome")
else:
    print("Not Palindrome")

# from 14 import *