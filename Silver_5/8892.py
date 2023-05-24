for _ in range(int(input())):
    li = [input() for _ in range(int(input()))]

    flag = False
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == (li[i] + li[j])[::-1]:
                print(li[i] + li[j])
                flag = True
                break
            elif li[j] + li[i] == (li[j] + li[i])[::-1]:
                print(li[j] + li[i])
                flag = True
                break
        if flag:
            break

    if not flag:
        print(0)
