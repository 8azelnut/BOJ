n = int(input())
li = list(input().split())

res = set()

for i in range(n):
    res.add(li[i][0])

print(1 if len(res) == 1 else 0)
