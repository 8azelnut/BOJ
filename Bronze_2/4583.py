li = ["b", "d", "p", "q", "i", "o", "v", "w", "x"]

while True:
    s = input()

    if s == "#":
        break

    res = ""
    for i in s:
        if i not in li:
            res = "INVALID"
            break
        else:
            if i == "b":
                res += "d"
            elif i == "d":
                res += "b"
            elif i == "p":
                res += "q"
            elif i == "q":
                res += "p"
            else:
                res += i

    if res != "INVALID":
        print(res[::-1])
    else:
        print(res)
