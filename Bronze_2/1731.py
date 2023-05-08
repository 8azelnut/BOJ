n = int(input())

li = []
for i in range(n):
    li.append(int(input()))

for i in li:
    if li[2] - li[1] == li[1] - li[0]:
        res = li[1] - li[0]
        li[-1] += res

        print(li[-1])
        break
    else:
        res = li[1] // li[0]
        li[-1] *= res

        print(li[-1])
        break
