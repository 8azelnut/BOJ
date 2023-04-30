coin_li = [25, 10, 5, 1]
for i in range(int(input())):
    num = int(input())

    li = []
    for j in coin_li:
        li.append(num // j)
        num = num % j

    for k in li:
        print(k, end=" ")
