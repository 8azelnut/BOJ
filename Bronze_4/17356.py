num1, num2 = map(int, input().split())

m = (num2 - num1) / 400

print(1 / (1 + 10 ** m))
