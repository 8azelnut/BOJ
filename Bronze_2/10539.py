n = int(input())
li = list(map(int, input().split()))

res_li = []
for i in range(n):
    res_li.append((li[i] * (i + 1)) - sum(res_li))

print(*res_li)
