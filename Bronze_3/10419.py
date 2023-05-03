for i in range(int(input())):
    d = int(input())

    max_value = 0
    while (max_value + 1) + (max_value + 1) ** 2 <= d:
        max_value += 1

    print(max_value)
