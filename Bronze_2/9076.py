t = int(input())

for i in range(t):
    li = sorted(list(map(int, input().split())))

    li.remove(li[4])
    li.remove(li[0])

    if max(li) - min(li) >= 4:
        print("KIN")
    else:
        print(sum(li))
