s = input()

res = ""
for i in s:
    k = ord(i) - 3

    if k < 65:
        k = ord(i) + 23

    res += chr(k)

print(res)
