t = int(input())

res = ""
while t > 0:
    res += str(t % 9)
    t //= 9

print(res[::-1])
