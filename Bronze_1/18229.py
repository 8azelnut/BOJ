n, m, k = map(int, input().split())

tmp = [0] * n

li = [list(map(int, input().split())) for i in range(n)]

for i in range(m):  # 5
    for j in range(n):  # 4
        tmp[j] += li[j][i]

        if tmp[j] >= k:
            print(j+1, i+1)
            quit()
