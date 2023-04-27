num = int(input())

cnt = 0
for i in range(num):
    day = input()

    if int(day[2:]) <= 90:
        cnt += 1

print(cnt)
