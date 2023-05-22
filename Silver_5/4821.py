while True:
    t = int(input())

    if t == 0:
        break

    li = list(input().split(","))

    tmp = []
    for i in range(len(li)):
        if "-" in li[i]:
            a, b = map(int, li[i].split("-"))

            if a <= b:
                if a <= t:
                    if b <= t:
                        for j in range(a, b+1):
                            tmp.append(j)
                    else:
                        for j in range(a, t+1):
                            tmp.append(j)
        else:
            if int(li[i]) <= t:
                tmp.append(int(li[i]))

    print(len(set(tmp)))
