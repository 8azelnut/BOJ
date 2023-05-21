s = int(input())

cnt = res = 0
while True:
    cnt += 1
    res += cnt

    if res > s:
        break

print(cnt-1)
