import re


def trans(num, q):
    res = ""

    while num:
        num, mod = divmod(num, q)
        res += str(mod)

    return res[::-1]


n, k = map(int, input().split())
str_trans = trans(n, k)

li = re.split(r'[0]', str_trans)

ans = 0
for i in li:
    if i.isdigit():
        ans += int(i)

print(trans(ans, k))
