m = int(input())
n = int(input())

i = 1
li = []
while i < n:
    res = i * i

    if m <= res <= n:
        li.append(res)

    i += 1

if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)
