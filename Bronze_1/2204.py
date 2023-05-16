while True:
    n = int(input())

    if n == 0:
        quit()

    li = []
    for i in range(n):
        s = input()
        li.append(s)

    li.sort(key=lambda value: value.lower())

    print(li[0])
