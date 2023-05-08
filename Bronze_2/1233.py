from collections import Counter

s1, s2, s3 = map(int, input().split())

li = []
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            res = 0
            res += i + j + k
            li.append(res)

cnt_items = Counter(li)

max_items = sorted(cnt_items.items(), key=lambda x: x[1], reverse=True)

print(max_items[0][0])
