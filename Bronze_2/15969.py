n = int(input())
li = sorted(list(map(int, input().split())))

print(max(li) - min(li))
