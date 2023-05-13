n = int(input())
li = list(map(int, input().split()))

p = li.index(-1)

print(min(li[:p]) + min(li[p+1:]))
