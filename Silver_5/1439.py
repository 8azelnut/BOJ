s = input()

cnt = 0
check = True
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if not check:
            check = True
        else:
            cnt += 1
            check = False

print(cnt)
