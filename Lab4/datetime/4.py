#calculate the difference between two time
# import datetime
# ct = datetime.datetime.now().time()
# print(ct)
# at = datetime.time(21, 34, 23)
# print(at)
# diff = datetime.timedelta(hours=(at.hour - ct.hour), minutes=(at.minute - ct.minute), seconds=(at.second - ct.second))
# print(diff)
from datetime import datetime, time
def diff_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(diff_seconds(date2, date1)))
print()