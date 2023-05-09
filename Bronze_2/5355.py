t = int(input())

for i in range(t):
    s = input().split(" ")

    n = float(s[0])
    p = s[1:]

    for j in p:
        if j == "@":
            n *= 3
        elif j == "%":
            n += 5
        else:
            n -= 7

    print(format(n, ".2f"))
