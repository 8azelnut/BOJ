a = input()
b = input().split()

li = []
for i in a:
    if i in b:
        li.append(i.lower())
    else:
        li.append(i)

print("".join(li))
