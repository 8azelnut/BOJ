n = int(input())
s = input()

res = 0
for i in s:
    res += ord(i) - 64

print(res)
