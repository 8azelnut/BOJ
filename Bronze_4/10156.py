price, count, balance = map(int, input().split())

value = price * count

if value <= balance:
    print("0")
else:
    print(value - balance)
