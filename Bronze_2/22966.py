n = int(input())

li = []
for i in range(n):
    s, l = input().split()

    li.append([s, int(l)])

    li.sort(key=lambda x: x[1])

print(li[0][0])
