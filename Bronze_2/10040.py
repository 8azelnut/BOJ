n, m = map(int, input().split())
li = [0] * n

a = [int(input()) for i in range(n)]
b = [int(input()) for i in range(m)]

for i in range(m):
    for j in range(n):
        if a[j] <= b[i]:
            li[j] += 1
            break

print(li.index(max(li)) + 1)
