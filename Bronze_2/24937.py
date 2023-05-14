n = int(input()) % 10

s = "SciComLove"
s = list(s)
for i in range(n):
    s.append(s[0])
    del s[0]

print("".join(s))
