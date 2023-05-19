n, m = map(int, input().split())

li = [input().split() for i in range(n)]
tmp = [input().split() for i in range(m)]

for i in range(m):
    cnt = 0

    for j in range(n):
        if (tmp[i][0] == "-" or tmp[i][0] == li[j][0]) and (tmp[i][1] == "-" or tmp[i][1] == li[j][1]) and (tmp[i][2] == "-" or tmp[i][2] == li[j][2]):
            cnt += 1

    print(cnt)
