n, m = map(int, input().split())
li = list(map(int, input().split()))

res = 0
for i in range(1, n+1):
    for j in li:
        if i % j == 0:
            res += i
            break

print(res)
