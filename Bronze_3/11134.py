for i in range(int(input())):
    n, c = map(int, input().split())

    cnt = 0
    while n > 0:
        n -= c
        cnt += 1

    print(cnt)
