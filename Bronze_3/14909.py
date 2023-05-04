li = list(map(int, input().split()))

cnt = 0
for i in li:
    if i > 0:
        cnt += 1

print(cnt)
