for i in range(int(input())):
    n = int(input())

    res = 0
    for j in range(n):
        a, b, c = map(int, input().split())

        if a >= 0 or b >= 0 or c >= 0:
            res += max(a, b, c)

    print(res)
