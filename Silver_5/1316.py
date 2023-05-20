cnt = 0
for i in range(int(input())):
    s = input()

    flag = True
    for j in range(len(s)-1):
        if s[j] != s[j+1] and s[j] in s[j+1:]:
            flag = False

    if flag:
        cnt += 1

print(cnt)
