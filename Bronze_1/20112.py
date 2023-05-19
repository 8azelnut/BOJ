n = int(input())

li = [[] for i in range(n)]
for i in range(n):
    s = input()
    for j in s:
        li[i].append(j)

tmp = [["" for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        tmp[i][j] = li[j][i]

print("YES" if li == tmp else "NO")

# n = int(input())
#
# li = [input() for i in range(n)]
#
# res = "".join(li)
#
# tmp = ""
# for i in range(n):
#     for j in range(n):
#         tmp += li[j][i]
#
# print("YES" if res == tmp else "NO")
