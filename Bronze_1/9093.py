for i in range(int(input())):
    s = list(input().split())

    li = []
    for j in s:
        li.append(j[::-1])

    print(*li)
