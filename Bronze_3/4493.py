t = int(input())

for i in range(t):
    n = int(input())

    p1_cnt = p2_cnt = 0

    for j in range(n):
        p1_s, p2_s = input().split()

        if (p1_s == "R" and p2_s == "P") or (p1_s == "S" and p2_s == "R") or (p1_s == "P" and p2_s == "S"):
            p2_cnt += 1
        elif (p1_s == "P" and p2_s == "R") or (p1_s == "R" and p2_s == "S") or (p1_s == "S" and p2_s == "P"):
            p1_cnt += 1

    if p1_cnt > p2_cnt:
        print("Player 1")
    elif p1_cnt < p2_cnt:
        print("Player 2")
    else:
        print("TIE")
