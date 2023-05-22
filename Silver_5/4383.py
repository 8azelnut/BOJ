while True:
    try:
        s = input().split()

        n = int(s[0])
        tmp = s[1:]

        t_li = [i for i in range(1, n)]

        if n == 1:
            print("Jolly")
        else:
            li = sorted(set([abs(int(tmp[i]) - int(tmp[i+1])) for i in range(len(tmp)-1)]))

            if li == t_li:
                print("Jolly")
            else:
                print("Not jolly")
    except:
        break
