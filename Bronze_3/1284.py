while True:
    n = input()

    if n == "0":
        break

    cnt = 2
    for i in n:
        if i == "0":
            cnt += 4
        elif i == "1":
            cnt += 2
        else:
            cnt += 3

    if 10 <= int(n) < 100:
        cnt += 1
    elif 100 <= int(n) < 1000:
        cnt += 2
    elif 1000 <= int(n) < 10000:
        cnt += 3

    print(cnt)
