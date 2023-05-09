s = input()
li = [1, 0, 0]

for i in s:
    if i == "A":
        li[0], li[1] = li[1], li[0]
    elif i == "B":
        li[1], li[2] = li[2], li[1]
    else:
        li[0], li[2] = li[2], li[0]

print(li.index(1) + 1)
