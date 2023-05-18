s = input()
k = input()

res = ""
for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        res += i

if k in res:
    print(1)
else:
    print(0)
