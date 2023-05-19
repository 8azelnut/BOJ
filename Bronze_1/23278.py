n, l, h = map(int, input().split())
li = sorted(list(map(int, input().split())))

print(sum(li[l:n-h]) / (n-l-h))
