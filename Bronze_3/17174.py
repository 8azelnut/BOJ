n, m = map(int, input().split())

cnt = n
while n >= m:
    n //= m
    cnt += n

print(cnt)
