t = int(input())

for i in range(t):
    m, p = input().split()
    li = list(input().split())

    if p == "C":
        for j in li:
            print(ord(j) - 64, end=" ")
        print()
    elif p == "N":
        for j in li:
            print(chr(int(j) + 64), end=" ")
        print()
