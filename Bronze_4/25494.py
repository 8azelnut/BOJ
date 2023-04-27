num = int(input())

for i in range(num):
    x, y, z = map(int, input().split())

    min_value = min(x, min(y, z))

    print(min_value)
