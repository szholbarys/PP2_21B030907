s = map(str, input().split())
for i in s:
    if len(i) >= 3:
        print(i, end = ' ')
    else:
        continue