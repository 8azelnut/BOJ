while True:
    num1, num2 = map(int, input().split())

    if num1 == num2 == 0:
        break

    print(f"{num1 // num2} {num1 % num2} / {num2}")
