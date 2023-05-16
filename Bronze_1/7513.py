for i in range(int(input())):
    li = [input() for _ in range(int(input()))]

    print(f"Scenario #{i + 1}:")

    for j in range(int(input())):
        p_li = list(map(int, input().split()))

        res = ""
        s = p_li[1:]

        for k in s:
            res += li[k]

        print(res)
    print()
