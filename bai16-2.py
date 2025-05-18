import time
t = time.localtime()
print(t)
time_string = time.strftime("%m/%d/%y, %H:%M:%S ", t)
print(time_string)
print(type(time_string))