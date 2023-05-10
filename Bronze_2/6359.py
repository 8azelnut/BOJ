t = int(input())

for i in range(t):
    n = int(input())

    li = [0] * (n + 1)

    for j in range(1, n+1):
        for k in range(j, n+1, j):
            if li[k] == 0:
                li[k] = 1
            else:
                li[k] = 0

    print(li.count(1))
