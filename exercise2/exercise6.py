#import datetime
from datetime import datetime

print(datetime.now())
print(datetime.now().strftime("%Y-%m-%d %H:%M"))
print(datetime.now().strftime("%Y/%m/%d %H:%M"))

timestamp = datetime.now().timestamp()
time = datetime.fromtimestamp(timestamp)
print(time)

print(datetime.fromisoformat("2022-01-01 10:10"))

