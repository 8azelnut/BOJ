li = []
max_len = 0
for i in range(5):
    li.append(input())

    max_len = max(max_len, len(li[i]))

res = ""
for i in range(max_len):
    for j in range(5):
        if i < len(li[j]):
            res += li[j][i]

print(res)
