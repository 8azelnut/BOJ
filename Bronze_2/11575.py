t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    s = input()

    for j in s:
        print(chr((a * (ord(j) - 65) + b) % 26 + 65), end="")

    print()
