n, x = map(int, input().split())
li = list(map(int, input().split()))

while True:
    for i in range(n):
        if x <= li[i]:
            x += 1
        else:
            print(i + 1)
            quit()
