n, m = map(int, input().split())

li = [list(input()) for i in range(n)]

for i in range(n):
    for j in range(m):
        if li[i][j] != ".":
            li[i][m-j-1] = li[i][j]

for i in range(n):
    print("".join(li[i]))
