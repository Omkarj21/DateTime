import datetime
import pytz

now1= str(datetime.datetime.now()) # Datetime to String conversion for slice

print("Today's Date and Current Time :",datetime.datetime.now())
print("Today's Date", datetime.date.today())
print("Today's Month", datetime.date.today().month)
print("Today's Day", datetime.date.today().day)
print("Today's Year", datetime.date.today().year)
print("Current Time", str(now1[10:]))
print("Current Hour", datetime.datetime.now().hour)
print("Current Minutes", datetime.datetime.now().minute)
print("Current Seconds", datetime.datetime.now().second)
print("Current MicroSeconds", datetime.datetime.now().microsecond)



# Python strftime() - datetime to string
now2 = datetime.datetime.now()
t = now2.strftime("%H:%M:%S")
print("time:", t)
s1 = now2.strftime("%m/%b/%Y, %H:%M:%S")
s11 = now2.strftime("%m-%b-%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)
print("s11:", s11)
s2 = now2.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)


# Python strptime() - string to datetime
date_string = "21 June 2018"
date_dt = datetime.datetime.strptime(date_string,"%d %B %Y")
# date_dt1 = datetime.datetime.strptime(date_string,"%d %b %Y")
print("strptime",date_dt)
# print("strptime",date_dt1)

# Python timezone()
local = datetime.datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))


# Time functions
import time
seconds = time.time()
print("Seconds since epoch =", seconds)
local_time = time.ctime(seconds)
print("Local time:", local_time)

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result)
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)