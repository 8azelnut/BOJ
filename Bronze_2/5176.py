k = int(input())

for i in range(k):
    p, m = map(int, input().split())

    li = []
    for j in range(p):
        li.append(int(input()))

    li = set(li)

    print(p - len(li))
