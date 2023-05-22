while True:
    s = input()

    if s == "0":
        break

    cnt = 0
    while True:
        if s == s[::-1]:
            print(cnt)
            break
        else:
            tmp = len(s)
            cnt += 1

            s = int(s) + 1
            s = str(s).zfill(tmp)
