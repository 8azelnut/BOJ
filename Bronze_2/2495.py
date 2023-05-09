for i in range(3):
    s = input()

    cnt = 1
    max_value = 0
    for j in range(1, len(s)):
        if s[j] == s[j-1]:
            cnt += 1
        else:
            max_value = max(max_value, cnt)
            cnt = 1

    max_value = max(max_value, cnt)

    print(max_value)
