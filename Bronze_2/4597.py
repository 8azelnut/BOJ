while True:
    s = input()

    if s == "#":
        break

    cnt = 0
    for i in s:
        if i == "1":
            cnt += 1

    if s[-1] == "e":
        if cnt % 2 == 0:
            s = s.replace("e", "0")
        else:
            s = s.replace("e", "1")
    else:
        if cnt % 2 == 0:
            s = s.replace("o", "1")
        else:
            s = s.replace("o", "0")

    print(s)
