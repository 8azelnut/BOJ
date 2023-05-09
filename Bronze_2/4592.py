while True:
    s = input().split()

    if s[0] == "0":
        break

    li = s[1:]

    res = ""
    for i in range(1, int(s[0])):
        if li[i] != li[i-1]:
            res += li[i] + " "

    print(f"{s[1]} {res}$")
