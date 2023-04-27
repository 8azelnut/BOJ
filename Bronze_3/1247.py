for i in range(3):
    num = int(input())

    li = []
    for j in range(num):
        li.append(int(input()))

    if sum(li) == 0:
        print("0")
    elif sum(li) > 0:
        print("+")
    else:
        print("-")
