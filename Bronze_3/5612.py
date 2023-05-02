n = int(input())
m = int(input())

max_value = m
for i in range(n):
    c1, c2 = map(int, input().split())

    m = m + (c1 - c2)

    if m < 0:
        max_value = 0
        break
    else:
        max_value = max(max_value, m)

print(max_value)
