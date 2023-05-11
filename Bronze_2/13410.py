n, k = map(int, input().split())

max_v = 0
for i in range(1, k+1):
    res = str(n * i)[::-1]

    max_v = max(max_v, int(res))

print(max_v)
