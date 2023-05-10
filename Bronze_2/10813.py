n, m = map(int, input().split())
li = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())

    li[i-1], li[j-1] = li[j-1], li[i-1]

print(*li)
