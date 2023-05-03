n = int(input())

p1_score = p2_score = 100
for i in range(n):
    p1, p2 = map(int, input().split())

    if p1 < p2:
        p1_score -= p2
    elif p1 > p2:
        p2_score -= p1

print(p1_score)
print(p2_score)
