n, q = map(int, input().split())

li = [0] * n

for i in range(q):
    a, b = map(int, input().split())

    for j in range(a-1, n, b):
        li[j] = 1

cnt = li.count(0)

print(cnt)
