t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    res = 0

    li = list(map(int, input().split()))

    for j in li:
        res += j // k

    print(res)
