t = int(input())

for i in range(t):
    a, n = map(int, input().split())

    res = ""
    while a > 0:
        res += str(hex(a % n)[2:])
        a //= n

    if res == res[::-1]:
        print(1)
    else:
        print(0)
