li = [0] * 10001

for i in range(int(input())):
    x, y = map(int, input().split())

    for j in range(x, y):
        li[j] = 1

print(sum(li))
