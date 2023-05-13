n = int(input())

li = [i for i in range(1, n+1)]

while len(li) != 1:
    tmp = []

    for index, value in enumerate(li):
        if index % 2:
            tmp.append(value)

    li = tmp

print(*li)
