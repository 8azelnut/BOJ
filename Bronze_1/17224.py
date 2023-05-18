n, l, k = map(int, input().split())

li = []
for i in range(n):
    sub1, sub2 = map(int, input().split())

    if sub2 <= l:
        li.append(140)
    elif sub1 <= l:
        li.append(100)

li = sorted(li, reverse=True)

print(sum(li[:k]))
