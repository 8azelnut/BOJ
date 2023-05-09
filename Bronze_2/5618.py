n = int(input())
li = sorted(list(map(int, input().split())))

if n == 2:
    for i in range(1, li[0]+1):
        if li[0] % i == 0 and li[1] % i == 0:
            print(i)
else:
    for i in range(1, li[0]+1):
        if li[0] % i == 0 and li[1] % i == 0 and li[2] % i == 0:
            print(i)
