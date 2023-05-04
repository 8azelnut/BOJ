n = int(input())

li = []
for i in range(n):
    li.append(input())

k = int(input())

if k == 1:
    print(*li, sep="\n")
elif k == 2:
    for i in li:
        print(i[::-1], sep="\n")
else:
    print(*li[::-1], sep="\n")
