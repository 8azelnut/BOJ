num = int(input())

max_value = 0
score = 0
for i in range(num):
    a, d, g = map(int, input().split())

    score = a * (d + g)

    if a == d + g:
        score *= 2

    max_value = max(score, max_value)

print(max_value)
