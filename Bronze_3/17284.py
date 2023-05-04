li = list(map(int, input().split()))

res = 0
for i in li:
    if i == 1:
        res += 500
    elif i == 2:
        res += 800
    else:
        res += 1000

print(5000 - res)
