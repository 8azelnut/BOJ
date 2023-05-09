t = int(input())

for i in range(t):
    n = input()

    r_n = str(int(n) + int(n[::-1]))

    if r_n == r_n[::-1]:
        print("YES")
    else:
        print("NO")
