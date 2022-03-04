#delete microsecond
import datetime 
time = datetime.datetime.now()
print(time.replace(microsecond = 0))