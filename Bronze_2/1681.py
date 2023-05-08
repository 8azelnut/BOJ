n, l = map(int, input().split())

res = 1
cnt = 0
while True:
    if str(l) not in str(res):
        cnt += 1

        if cnt == n:
            print(res)
            break
        res += 1

    else:
        res += 1
