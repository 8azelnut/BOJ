while True:
    try:
        s = input()

        l_cnt = u_cnt = s_cnt = n_cnt = 0
        for i in s:
            if i.isupper():
                u_cnt += 1
            elif i.islower():
                l_cnt += 1
            elif i.isspace():
                s_cnt += 1
            elif i.isnumeric():
                n_cnt += 1

        print(l_cnt, u_cnt, n_cnt, s_cnt)
    except EOFError:
        break
