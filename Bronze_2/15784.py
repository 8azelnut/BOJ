n, a, b = map(int, input().split())

li = [list(map(int, input().split())) for i in range(n)]

target = li[a-1][b-1]
for i in range(n):
    if target < li[i][b-1]:
        print("ANGRY")
        quit()
    if target < li[a-1][i]:
        print("ANGRY")
        quit()

print("HAPPY")
