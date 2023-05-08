n = int(input())
li = list(map(int, input().split()))

check_li = [0] * 101

cnt = 0
for i in li:
    if check_li[i] != 0:
        cnt += 1
    else:
        check_li[i] += 1

print(cnt)
