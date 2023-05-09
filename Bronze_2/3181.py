s = list(input().split())
a = ["i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"]

res = s[0][0]
for i in range(1, len(s)):
    if s[i] not in a:
        res += s[i][0]

print(res.upper())
