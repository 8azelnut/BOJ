t = int(input())

for i in range(t):
    s = input()

    res = ""
    for j in range(len(s)-1, -1, -1):
        if j % 2 == 0:
            n = int(s[j]) * 2
            if n >= 10:
                n = n // 10 + n % 10

            res += str(n)
        else:
            res += s[j]

    ans = 0
    for k in res:
        ans += int(k)

    if ans % 10 == 0:
        print("T")
    else:
        print("F")
