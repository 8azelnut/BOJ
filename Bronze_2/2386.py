while True:
    s = input()

    if s == "#":
        break

    n = s[0]
    m = s[2:]

    cnt = 0
    for i in m:
        if i == n.upper():
            cnt += 1
        if i == n:
            cnt += 1

    print(n, cnt)
