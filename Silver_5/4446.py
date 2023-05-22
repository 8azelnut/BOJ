while True:
    try:
        s = input()

        vo = ["a", "i", "y", "e", "o", "u"]
        co = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]

        res = ""
        for i in range(len(s)):
            if s[i].lower() in vo:
                if s[i].isupper():
                    tmp = s[i].lower()

                    for j in range(len(vo)):
                        if tmp == vo[j]:
                            a = vo[(j+3)%6]
                            res += a.upper()
                else:
                    for j in range(len(vo)):
                        if s[i] == vo[j]:
                            a = vo[(j+3)%6]
                            res += a
            elif s[i].lower() in co:
                if s[i].isupper():
                    tmp = s[i].lower()

                    for j in range(len(co)):
                        if tmp == co[j]:
                            a = co[(j+10)%20]
                            res += a.upper()
                else:
                    for j in range(len(co)):
                        if s[i] == co[j]:
                            a = co[(j+10)%20]
                            res += a
            else:
                res += s[i]

        print(res)
    except:
        break
