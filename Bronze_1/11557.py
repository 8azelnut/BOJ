for i in range(int(input())):
    li = {}

    for j in range(int(input())):
        s, l = input().split()

        li[s] = int(l)

    li = sorted(li.items(), key=lambda x: x[1], reverse=True)

    print(li[0][0])
