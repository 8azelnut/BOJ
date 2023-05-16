r, c, zr, zc = map(int, input().split())

li = []
for i in range(r):
    s = input()

    res = ""
    for j in s:
        res += j * zc

    for j in range(zr):
        li.append(res)

print(*li)
