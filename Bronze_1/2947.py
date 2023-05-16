li = list(map(int, input().split()))
ans = [1, 2, 3, 4, 5]

while True:
    for i in range(1, len(li)):
        if li[i] < li[i-1]:
            li[i], li[i-1] = li[i-1], li[i]
            print(*li)

    if ans == li:
        break
