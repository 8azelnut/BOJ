n, q = map(int, input().split())
li = list(map(int, input().split()))

for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        a, b = query[1], query[2]

        print(sum(li[a-1:b]))

        li[a-1], li[b-1] = li[b-1], li[a-1]
    else:
        a, b, c, d = query[1], query[2], query[3], query[4]

        print(sum(li[a-1:b]) - sum(li[c-1:d]))
