from collections import deque

n = int(input())

li = deque([i+1 for i in range(n)])

tmp = []
while len(li) > 1:
    tmp.append(li.popleft())
    li.append(li.popleft())

print(*tmp, *li)
