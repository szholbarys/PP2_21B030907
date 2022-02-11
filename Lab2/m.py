date = input()
dates = []
while date != '0':
    date = date.split()
    date[2], date[0] = date[0], date[2]
    dates.append(date)
    date = input()
dates.sort()
for i in range(len(dates)):
    dates[i][0], dates[i][2] = dates[i][2], dates[i][0]
for i in dates:
    print(*i)