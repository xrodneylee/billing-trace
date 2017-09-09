from datetime import datetime, timezone, timedelta, date, time     
# local_time = datetime.now(timezone.utc).astimezone()
# print(local_time)
# print(local_time.isoformat())
# print(local_time.date())
# print(datetime.now(timezone.utc).isoformat())
# print(str(local_time.date()) + 'T' + str(local_time.hour - 2)+':00:00+08:00')
# print(time.time())
# print(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:00:00'))
tz = timezone(offset=timedelta(hours=8), name='Asia/Taipei')
# print(((datetime.now(timezone.utc).astimezone(tz) - timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)).isoformat())
# print(local_time)

def datetime_converter(date_str, time_str):
    tz = timezone(offset=timedelta(hours=8), name='Asia/Taipei')
    year, month, day = (int(item) for item in date_str.split('-'))
    hour, minutes = (int(item) for item in time_str.split(':'))
    d = date(year, month, day)
    t = time(hour, minutes, tzinfo=tz)
    return datetime.combine(d, t).replace(minute=0, second=0, microsecond=0)

qq = datetime_converter("2017-09-09", "13:00")
a = qq
b = (qq + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
print(a >= a)