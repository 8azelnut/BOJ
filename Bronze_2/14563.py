t = int(input())
li = list(map(int, input().split()))

for i in range(t):

    res = 0
    res_li = []
    for j in range(1, li[i]+1):
        if li[i] % j == 0:
            res_li.append(j)

    res = sum(res_li[:-1])

    if res == li[i]:
        print("Perfect")
    elif res < li[i]:
        print("Deficient")
    elif res > li[i]:
        print("Abundant")
