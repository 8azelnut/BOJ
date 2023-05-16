n = int(input())

li = [[], [], []]

for i in range(n):
    a, b, c = map(int, input().split())

    li[0].append(a)
    li[1].append(b)
    li[2].append(c)

score = [0] * n
for i in range(3):
    for j in range(n):
        if li[i].count(li[i][j]) == 1:
            score[j] += li[i][j]
        else:
            score[j] += 0

print(*score, sep="\n")
