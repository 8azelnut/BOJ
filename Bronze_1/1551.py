n, k = map(int, input().split())
li = list(map(int, input().split(",")))

res_li = []
for i in range(k):
    for j in range(1, len(li)):
        res_li.append(li[j] - li[j-1])

    li = res_li
    res_li = []

print(*li, sep=",")
