n, q = map(int, input().split())

li = [0] * n

for i in range(q):
    a, b, c = map(int, input().split())

    if a == 1:
        li[b-1] += c
    elif a == 2:
        print(sum(li[b-1:c]))
