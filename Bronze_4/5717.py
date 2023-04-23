while True:
    num1, num2 = map(int, input().split())

    if num1 == 0 and num2 == 0:
        quit()

    print(num1 + num2)
