s = input()

key = ord(s[0]) ^ ord("C")

res = ""
for i in s:
    res += chr(ord(i) ^ key)

print(res)
