a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

x = a * p

if c < p:
    y = b + ((p - c) * d)
else:
    y = b

print(min(x, y))
