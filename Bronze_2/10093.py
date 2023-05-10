a, b = map(int, input().split())

li = []
for i in range(min(a, b)+1, max(a, b)):
    li.append(i)

print(len(li))

if li:
    print(*li)
