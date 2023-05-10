s = input()

res = 10
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        res += 10
    else:
        res += 5

print(res)
