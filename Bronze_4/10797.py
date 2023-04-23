num = int(input())
car_list = list(map(int, input().split()))

cnt = 0
for i in car_list:
    if num == i:
        cnt += 1

print(cnt)
