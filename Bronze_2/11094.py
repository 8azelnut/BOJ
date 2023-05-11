n = int(input())

for i in range(n):
    s = input()

    index = s.find("Simon says")

    if not index == -1:
        print(s[index+10:])
