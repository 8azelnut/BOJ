n = int(input())
ans = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

li = []
for i in range(9):
    sc_li = list(map(int, input().split()))
    li.append(max(sc_li))

max_value = max(li)

for i in range(9):
    if max_value == li[i]:
        print(ans[i])
        break
