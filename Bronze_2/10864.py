from collections import Counter

n, m = map(int, input().split())

li = []
for i in range(m):
    a, b = map(int, input().split())

    li.append(a)
    li.append(b)

for i in range(1, n+1):
    print(li.count(i))
