li = list(input())

res = 0
for i in range(len(li)):
    li.insert(0, li[-1])
    del li[-1]

    s = ""
    for j in li:
        s += j

    res += int(s)

print(res)
