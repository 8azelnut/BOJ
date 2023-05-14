n = int(input())
li = sorted(list(map(int, input().split())))
x, y = map(int, input().split())

r = x // n

res_li = []
for i in li:
    if i >= y:
        res_li.append(i)

print((n * x // 100), len(res_li))
