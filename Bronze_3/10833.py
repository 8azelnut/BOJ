res = 0
for i in range(int(input())):
    a, s = map(int, input().split())

    res += s % a

print(res)
