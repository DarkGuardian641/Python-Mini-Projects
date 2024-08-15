import time
t = time.localtime()
format = time.strftime("Date is %D and Time is %H:%M:%S",t)
print(format)