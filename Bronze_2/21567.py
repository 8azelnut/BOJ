a = int(input())
b = int(input())
c = int(input())

li = [0] * 10

s = str(a * b * c)

for i in s:
    li[int(i)] += 1

print(*li, sep="\n")
