t = int(input())

for i in range(t):
    s = int(input())
    n = int(input())

    price = s

    for j in range(n):
        q, p = map(int, input().split())

        price += q * p

    print(price)
