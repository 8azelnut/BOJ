n = int(input())

STRAWBERRY = BANANA = LIME = PLUM = 0
for i in range(n):
    s, x = input().split()

    if s == "STRAWBERRY": STRAWBERRY += int(x)
    elif s == "BANANA": BANANA += int(x)
    elif s == "LIME": LIME += int(x)
    elif s == "PLUM": PLUM += int(x)


if STRAWBERRY == 5 or BANANA == 5 or LIME == 5 or PLUM == 5:
    print("YES")
else:
    print("NO")
