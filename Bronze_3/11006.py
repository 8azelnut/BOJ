for i in range(int(input())):
    n, m = map(int, input().split())

    leg = m * 2 - n

    print(leg, m - leg)
