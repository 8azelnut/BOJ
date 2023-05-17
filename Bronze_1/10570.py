from collections import Counter

for i in range(int(input())):

    li = []
    for j in range(int(input())):
        li.append(int(input()))

    li = Counter(li)

    s_li = sorted(li.items(), key=lambda x: (-x[1], x[0]))

    print(s_li[0][0])
