c, k, p = map(int, input().split())

res = 0
for i in range(1, c+1):
    res = res + (i * k) + (p * (i ** 2))

print(res)
