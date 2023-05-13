n = int(input())
s = list(input())

for i in range(n):
    if not s[i] == "?":
        s[-1-i] = s[i]
    else:
        s[i] = "a"

print(*s, sep="")
