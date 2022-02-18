def f(s):
    t = ""

    for i in s:
        t = i + t

    if t == s:
        return True
    else:
        return False

s = input()

if f(s) == True:
    print("Palindrome")
else:
    print("Not Palindrome")