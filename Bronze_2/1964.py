n = int(input())

first = 5
cnt = 7
for i in range(1, n):
    first += cnt
    cnt += 3

print(first % 45678)
