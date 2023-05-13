n = int(input())

dt = {}
for i in range(n):
    a, b = input().split()

    dt[a] = int(b)

dt = sorted(dt.items(), key=lambda x: (-x[1], x[0]))

print(dt[0][0])
