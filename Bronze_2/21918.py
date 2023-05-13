n, m = map(int, input().split())

li = list(map(int, input().split()))

for i in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        li[b-1] = c
    elif a == 2:
        for j in range(b-1, c):
            if li[j] == 0:
                li[j] = 1
            elif li[j] == 1:
                li[j] = 0
    elif a == 3:
        for j in range(b-1, c):
            if li[j] == 1:
                li[j] = 0
    elif a == 4:
        for j in range(b-1, c):
            if li[j] == 0:
                li[j] = 1

print(*li)
