li = [chr(i) for i in range(65, 91)]

while True:
    s = input().upper()

    if s == "#":
        break

    s = set(s)

    cnt = 0
    for i in s:
        if i in li:
            cnt += 1

    print(cnt)
