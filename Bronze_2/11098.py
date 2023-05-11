n = int(input())

for i in range(n):
    p = int(input())

    li = {}
    for j in range(p):
        c, name = input().split()
        c = int(c)

        li[c] = name

    li = sorted(li.items(), key=lambda x: x[0], reverse=True)

    print(li[0][1])
