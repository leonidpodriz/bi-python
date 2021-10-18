import datetime
import time

start = datetime.datetime.now()
print(f'Program started at {start.timestamp()}')
# time.sleep(3)
end = datetime.datetime.now()

delta = start - end

print(int(delta.total_seconds()))

print(start + datetime.timedelta(30))

datetime_in_string = '2021-11-17 21:49:11'
new_date = datetime.datetime.strptime(datetime_in_string, '%Y-%m-%d %H:%M:%S')
print(type(datetime_in_string), datetime_in_string)
print(type(new_date), new_date)
