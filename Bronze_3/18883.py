n, m = map(int, input().split())

cnt = 1
for i in range(n):
    for j in range(m):
        if cnt % m == 0:
            print(cnt, end="")
        else:
            print(cnt, end=" ")
        cnt += 1

    print()
