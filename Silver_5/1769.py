n = input()

cnt = 0
while len(n) >= 2:
    res = 0
    for i in n:
        res += int(i)

    n = str(res)
    cnt += 1

print(cnt)

if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")
