n = int(input())
k = int(input())

li = [0] * (n+1)

for i in range(2, n+1):
    if li[i] == 0:
        for j in range(i, n+1, i):
            if j % i == 0:
                li[j] = max(li[j], i)

cnt = 0
for i in li:
    if i <= k:
        cnt += 1

print(cnt-1)
