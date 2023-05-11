n, m = map(int, input().split())

li = [int(input()) for i in range(n)]

for i in range(1, m+1):
    for j in range(1, len(li)):
        if li[j-1] % i > li[j] % i:
            li[j], li[j-1] = li[j-1], li[j]

print(*li, sep="\n")
