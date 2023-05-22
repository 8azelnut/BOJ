find_s = input()

cnt = 0
for i in range(int(input())):
    s = input()

    flag = False
    if s.find(find_s) != -1:
        flag = True

    # YZAAAAAAAX
    # XYZAAAAAAA
    # AXYZAAAAAA
    for j in range(len(find_s)):
        s = s[-1] + s[0:len(s)-1]

        if s.find(find_s) != -1:
            flag = True
            break

    if flag:
        cnt += 1

print(cnt)
