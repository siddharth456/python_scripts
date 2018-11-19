# time and calendar module

import time
import calendar

# number of ticks since epoch
print("Number of ticks since epoch:",time.time())
print()

# the time tuple
print(time.localtime(time.time()))
print()

# current formatted time
print("the current time is:",time.asctime(time.localtime(time.time())))
print()

# get calendar of a month
print("the calendar for the month of June 2018:")
print(calendar.month(2018,6))
print()

# ctime() and sleep() methods
print("the current time is:",time.ctime())
time.sleep(10)
print("the time after 10 sec is:",time.ctime())

# ctime(180)
print("ctime(180):",time.ctime(180)) 
print()

# mktime()
tt=(2018,10,21,15,51,00,6,294,0)
m=time.mktime(tt)
print("time.mktime(tt): %f",m)
print("time.asctime(time.localtime(m))):",time.asctime(time.localtime(m)))
print("user formatted time:",time.strftime("%a %b %d %Y %H:%M:%S %Z",time.localtime(m)))

