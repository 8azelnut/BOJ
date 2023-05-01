i = 1
while True:
    n_0 = int(input())

    if n_0 == 0:
        break

    n_1 = 3 * n_0

    if n_1 % 2 == 0:
        n_2 = n_1 // 2
    else:
        n_2 = (n_1 + 1) // 2

    n_3 = 3 * n_2
    n_4 = n_3 // 9

    if n_1 % 2 != 0:
        print(f"{i}. odd {n_4}")
    else:
        print(f"{i}. even {n_4}")

    i += 1
