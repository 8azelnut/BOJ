li = [i+1 for i in range(20)]

for _ in range(10):
    i, j = map(int, input().split())

    li[i-1:j] = li[i-1:j][::-1]

print(*li)
