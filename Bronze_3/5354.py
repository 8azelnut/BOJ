t = int(input())

for i in range(t):
    n = int(input())

    for j in range(n):
        for k in range(n):
            if 1 <= j < n-1 and 1 <= k < n-1:
                print("J", end="")
            else:
                print("#", end="")
        print()

    print()
