a, b, c = map(int, input().split())
n = int(input())

li = []
for i in range(n):

    res = 0
    max_li = []
    for j in range(3):
        x, y, z = map(int, input().split())

        res = (a * x) + (b * y) + (c * z)

        max_li.append(res)

    li.append(sum(max_li))

print(max(li))
