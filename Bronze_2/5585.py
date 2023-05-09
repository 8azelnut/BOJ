m = int(input())
li = [500, 100, 50, 10, 5, 1]

balance = 1000 - m

cnt = 0
for i in li:
    cnt += balance // i
    balance %= i

print(cnt)
