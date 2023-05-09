t = int(input())

for i in range(t):
    s = input().split(" ")

    li = []
    for j in range(len(s[0])):
        a = ord(s[0][j]) - 64
        b = ord(s[1][j]) - 64

        if a > b:
            v = (b + 26) - a
        else:
            v = b - a

        li.append(v)

    print("Distances:", *li)
