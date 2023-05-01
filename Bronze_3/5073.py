while True:
    num1, num2, num3 = map(int, input().split())

    if num1 == num2 == num3 == 0:
        break

    max_value = max(num1, num2, num3)
    res = (num1 + num2 + num3) - max_value

    if max_value < res and num1 == num2 == num3:
        print("Equilateral")
    elif max_value < res and (num1 == num2) or (num1 == num3) or (num2 == num3):
        print("Isosceles")
    elif max_value < res and num1 != num2 != num3:
        print("Scalene")
    else:
        print("Invalid")
