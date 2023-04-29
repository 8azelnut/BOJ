max_value = 0
sum = 0
for i in range(4):
    num1, num2 = map(int, input().split())

    sum -= num1
    sum += num2

    max_value = max(sum, max_value)

print(max_value)
