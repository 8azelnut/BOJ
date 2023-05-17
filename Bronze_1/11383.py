n, m = map(int, input().split())

li = [input() for i in range(n)]
res_li = [input() for i in range(n)]

flag = True
for i in range(n):
    res = ""

    for j in li[i]:
        res += j * 2

    if not res == res_li[i]:
        flag = False
        break

print("Eyfa" if flag else "Not Eyfa")
