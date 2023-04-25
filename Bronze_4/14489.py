b1, b2 = map(int, input().split())
chicken_price = int(input())

sum_b = b1 + b2
double_price = chicken_price * 2

if sum_b >= double_price:
    print(sum_b - double_price)
else:
    print(sum_b)
