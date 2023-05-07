n = int(input())

for i in range(n):
    m = int(input())

    res = 0
    price_li = []
    for j in range(m):
        price_li.append(list(map(int, input().split())))

    kda_li = list(map(int, input().split()))

    for j in price_li:
        tmp = 0
        for k in range(3):
            if k != 1:
                tmp += j[k] * kda_li[k]
            else:
                tmp -= j[k] * kda_li[k]

        if tmp > 0:
            res += tmp

    print(res)
