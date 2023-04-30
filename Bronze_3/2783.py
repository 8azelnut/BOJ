x, y = map(int, input().split())
num = int(input())

gs_min = x * 1000 / y

for i in range(num):
    x_i, y_i = map(int, input().split())

    total = x_i * 1000 / y_i

    gs_min = min(gs_min, total)

print(round(gs_min, 2))
