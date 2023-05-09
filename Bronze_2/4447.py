n = int(input())

for i in range(n):
    s = input()
    c = s.lower()

    g_cnt = b_cnt = 0
    for j in c:
        if j == "g":
            g_cnt += 1
        elif j == "b":
            b_cnt += 1

    if g_cnt > b_cnt:
        print(f"{s} is GOOD")
    elif g_cnt < b_cnt:
        print(f"{s} is A BADDY")
    else:
        print(f"{s} is NEUTRAL")
