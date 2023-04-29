res = 0
for i in range(3):
    yut1, yut2, yut3, yut4 = map(int, input().split())

    res = yut1 + yut2 + yut3 + yut4

    if res == 4:
        print("E")
    elif res == 3:
        print("A")
    elif res == 2:
        print("B")
    elif res == 1:
        print("C")
    else:
        print("D")
