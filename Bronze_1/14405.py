s = input()

li = ["pi", "ka", "chu"]

for i in li:
    if i in s:
        s = s.replace(i, "*")

flag = True
for i in s:
    if i != "*":
        flag = False

print("YES" if flag else "NO")
