n = int(input())

cnt = 0
for i in range(1, n+1):
    s = str(i)

    res = 0
    for j in s:
        res += int(j)

    if i % res == 0:
        cnt += 1

print(cnt)
