i = 1
while True:
    s = list(input().split())

    if s[1] == "E":
        break

    flag = False
    if s[1] == "!=":
        flag = int(s[0]) != int(s[2])
    elif s[1] == "<":
        flag = int(s[0]) < int(s[2])
    elif s[1] == ">":
        flag = int(s[0]) > int(s[2])
    elif s[1] == "<=":
        flag = int(s[0]) <= int(s[2])
    elif s[1] == ">=":
        flag = int(s[0]) >= int(s[2])
    elif s[1] == "==":
        flag = int(s[0]) == int(s[2])

    print(f"Case {i}: {str(flag).lower()}")

    i += 1
