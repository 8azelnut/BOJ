t = int(input())

for i in range(t):
    n, s = input().split()

    n = int(n)

    print(s[:n-1] + s[n:])
