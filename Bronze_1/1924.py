import calendar

w = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x, y = map(int, input().split())

d = calendar.weekday(2007, x, y)

print(w[d])
