from collections import Counter

li = []
for i in range(10):
    li.append(int(input()))

print(sum(li) // len(li))

cnt = Counter(li)
li = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

print(li[0][0])
