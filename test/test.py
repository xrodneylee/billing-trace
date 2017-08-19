from datetime import datetime, timezone                                
local_time = datetime.now(timezone.utc).astimezone()
# print(local_time)
# print(local_time.isoformat())
# print(local_time.date())
print(str(local_time.date()) + 'T' + str(local_time.hour - 2)+':00:00+08:00')
# print(local_time)