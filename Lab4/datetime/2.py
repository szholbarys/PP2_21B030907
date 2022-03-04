# from datetime import date, timedelta
# now = date.today()
# for i in range(1, -2,  -1):
#     print(now - timedelta(days=i))
from datetime import timedelta , date
td = date.today()

yd = td - timedelta(days=1)
print(yd) #yesterday
print(td) #today
tm = td + timedelta(days=1)
print(tm) #tommorow