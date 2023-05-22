vo = ["a", "e", "i", "o", "u"]
ex = ["ee", "oo"]

while True:
    s = input()

    if s == "end":
        break

    flag = True
    cnt = 0
    # 1. 모음 하나를 반드시 포함하여야 한다.
    for i in s:
        if i in vo:
            flag = True
            break
        else:
            flag = False

    # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(len(s)-2):
        if s[i] in vo and s[i+1] in vo and s[i+2] in vo:
            flag = False
        elif s[i] not in vo and s[i+1] not in vo and s[i+2] not in vo:
            flag = False

    # 3. 같은 글자가 연속적으로 두 번 오면 안되나, ee와 oo는 허용한다.
    for i in range(len(s)-1):
        if s[i] == s[i+1] and s[i] + s[i+1] not in ex:
            flag = False

    if flag:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
