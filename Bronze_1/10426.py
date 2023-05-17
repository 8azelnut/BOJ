import datetime

date, n = input().split()
yy, mm, dd = map(int, date.split("-"))

n = int(n) - 1

day = datetime.datetime(yy, mm, dd)
day = datetime.timedelta(days=n) + day

print(day.strftime("%Y-%m-%d"))
