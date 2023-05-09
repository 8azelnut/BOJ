while True:
    n = input()

    if n == "0":
        break

    while True:
        res = 0

        if len(n) == 1:
            print(n)
            break
        else:
            for i in n:
                res += int(i)

            n = str(res)
