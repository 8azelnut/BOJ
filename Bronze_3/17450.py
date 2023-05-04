r_li = []
for i in range(3):
    li = list(map(int, input().split()))

    price = li[0] * 10
    weight = li[1] * 10

    if price >= 5000:
        price -= 500

    r_li.append(weight / price)

max_index = r_li.index(max(r_li))

if max_index == 0:
    print("S")
elif max_index == 1:
    print("N")
elif max_index == 2:
    print("U")
