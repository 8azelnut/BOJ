num = int(input())

for i in range(num):
    li = list(map(int, input().split()))

    even_li = []
    for j in li:
        if j % 2 == 0:
            even_li.append(j)

    print(sum(even_li), min(even_li), end=" ")
