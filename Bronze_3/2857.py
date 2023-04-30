li = []
for i in range(1, 6):
    s = input()

    if "FBI" in s:
        li.append(i)

if len(li) == 0:
    print("HE GOT AWAY!")
else:
    print(*li)
