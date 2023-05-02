t = int(input())

a_cnt = 0
b_cnt = 0
for i in range(t):
    a, b = map(int , input().split())

    if a > b:
        a_cnt += 1
    elif a < b:
        b_cnt += 1
    else:
        continue

print(a_cnt, b_cnt)