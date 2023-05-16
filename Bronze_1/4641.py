while True:
    li = list(map(int, input().split()))

    if li[0] == -1:
        break

    cnt = 0
    for i in range(len(li)-1):
        if li[i] * 2 in li:
            cnt += 1

    print(cnt)
