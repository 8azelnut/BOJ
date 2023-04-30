a, b = map(int, input().split())
c, d = map(int, input().split())

li = [a / c + b / d, c / d + a / b, d / b + c / a, b / a + d / c]

max_value = max(li)

print(li.index(max_value))
