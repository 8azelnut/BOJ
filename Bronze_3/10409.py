n, t = map(int, input().split())
li = list(map(int, input().split()))

cnt = 0
res = 0
for i in range(n):
    if res + li[i] <= t:
        res += li[i]
        cnt += 1
    else:
        break

print(cnt)
