while True:
    try:
        n, m = map(int, input().split())

        cnt = 0
        for i in range(n, m+1):
            flag = True
            for j in range(len(str(i))-1):
                for k in range(j+1, len(str(i))):
                    if str(i)[j] == str(i)[k]:
                        flag = False
                        break

            if flag:
                cnt += 1

        print(cnt)
    except:
        break
