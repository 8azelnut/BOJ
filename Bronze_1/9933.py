li = [input() for i in range(int(input()))]

cnt = 0
res = ""
for i in li:
    if i[::-1] in li:
        cnt = len(i)
        res = i[cnt//2]

print(cnt, res)
