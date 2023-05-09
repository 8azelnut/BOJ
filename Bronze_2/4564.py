while True:
    s = input()

    if s == "0":
        break

    while len(s) > 1:
        res = 1

        print(s, end=" ")

        for i in s:
            res *= int(i)

        s = str(res)

    print(s)
