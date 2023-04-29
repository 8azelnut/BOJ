num = int(input())

res = 0
for i in range(num):
    d1, d2, d3 = map(int, input().split())

    if d1 == d2 == d3:
        res = max(res, 10000 + d1 * 1000)
    elif d1 == d2 or d1 == d3:
        res = max(res, 1000 + d1 * 100)
    elif d2 == d3:
        res = max(res, 1000 + d2 * 100)
    else:
        res = max(res, 100 * max(d1, d2, d3))

print(res)
