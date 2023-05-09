a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

a_sum = b_sum = 0
res = ""

if a_li == b_li:
    print(10, 10)
    print("D")
else:
    for i in range(10):
        if a_li[i] > b_li[i]:
            res = "A"
            a_sum += 3
        elif a_li[i] < b_li[i]:
            res = "B"
            b_sum += 3
        elif a_li[i] == b_li[i]:
            a_sum += 1
            b_sum += 1

    print(a_sum, b_sum)

    if a_sum == b_sum:
        print(res)
    else:
        if a_sum > b_sum:
            print("A")
        else:
            print("B")
