t = input()

cnt = 0
res = 1
while True:
    if len(t) == 1:
        print(cnt)
        break

    for i in t:
        res *= int(i)

    cnt += 1
    t = str(res)
    res = 1
