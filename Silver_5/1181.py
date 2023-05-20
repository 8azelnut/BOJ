li = [input() for i in range(int(input()))]

li = list(set(li))
li.sort()
li = sorted(li, key=len)

print(*li)
