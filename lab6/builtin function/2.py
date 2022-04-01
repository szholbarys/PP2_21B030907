def Upper(x):
    cnt = 0
    for i in x:
        if 65 <= ord(i) <= 90: # upper letters
            cnt += 1
    return cnt


def Lower(x):
    cnt = 0
    for i in x:
        if 97 <= ord(i) <= 122: # lower letters
            cnt +=1
    return cnt

s = input()
print(f"Upper cases = {Upper(s)}")
print(f"Lower cases = {Lower(s)}")