a = input()
b = input()

li = []
for i in range(8):
    li.append(a[i])
    li.append(b[i])

while len(li) != 2:
    tmp = []

    for i in range(1, len(li)):
        n = (int(li[i]) + int(li[i-1])) % 10
        tmp.append(n)

    li = tmp

print(*li, sep="")
