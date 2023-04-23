num1 = int(input())
num2 = int(input())
num3 = int(input())

result = num1 + num2 + num3

if num1 == 60 and num2 == 60 and num3 == 60:
    print("Equilateral")
elif result == 180 and num1 == num2 or num1 == num3 or num2 == num3:
    print("Isosceles")
elif result == 180 and num1 != num2 and num1 != num3 and num2 != num3:
    print("Scalene")
elif result != 180:
    print("Error")
