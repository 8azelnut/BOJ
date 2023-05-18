n, l = map(int, input().split())

li = [input() for i in range(n)]

li.sort()

print(li[l-1])
