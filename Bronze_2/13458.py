n = int(input())
li = list(map(int, input().split()))
b, c = map(int, input().split())

res = 0
for i in li:
    i -= b

    cnt = 1
    if i > 0:
        cnt += i // c
        if not i % c == 0:
            cnt += 1

    res += cnt

print(res)
