n = int(input())
s = input()

cnt = bonus = res = 0
for i in s:
    cnt += 1

    if i == "O":
        res += cnt + bonus
        bonus += 1
    else:
        bonus = 0

print(res)
