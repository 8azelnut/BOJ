t = int(input())

for i in range(t):
    s = input()

    s_upper = s[0].upper()

    s = s_upper + s[1:]

    print(s)
