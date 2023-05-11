n = int(input())

for i in range(n):
    a, b = input().split()

    a = sorted(a)
    b = sorted(b)

    if a == b:
        print("Possible")
    else:
        print("Impossible")
