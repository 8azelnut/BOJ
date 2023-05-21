n = int(input())

li = [list(map(int, input().split())) for i in range(n)]

li = sorted(li, key=lambda x: -x[2])

print(li[0][0], li[0][1])
print(li[1][0], li[1][1])

for i in range(2, len(li)):
    if li[i][0] == li[i-1][0] == li[i-2][0]:
        continue
    else:
        print(li[i][0], li[i][1])
        break
