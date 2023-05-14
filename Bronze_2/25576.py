import sys

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n-1):
    k = list(map(int, sys.stdin.readline().split()))

    res = 0
    for j in range(len(li)):
        res += abs(k[j] - li[j])

    if res > 2000:
        cnt += 1

if cnt >= ((n-1) / 2):
    print("YES")
else:
    print("NO")
