t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    if n < 12 or m < 4:
        n = -1
    else:
        n = 11 * m + 4

    print(n)
