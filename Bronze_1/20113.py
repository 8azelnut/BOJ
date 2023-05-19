n = int(input())
li = list(map(int, input().split()))

tmp = [0] * n

for i in li:
    if i == 0:
        continue
    else:
        tmp[i-1] += 1

if tmp.count(max(tmp)) >= 2 or max(tmp) == 0:
    print("skipped")
else:
    print(tmp.index(max(tmp)) + 1)
