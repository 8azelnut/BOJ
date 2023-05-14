n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i in range(len(b)):
    if b[i] == 0:
        res += a[i]

print(sum(a))
print(res)
