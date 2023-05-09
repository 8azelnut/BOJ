n = int(input())

for i in range(n):
    s = list(input().split())

    for j in range(2, len(s)):
        print(s[j], end=" ")

    print(s[0], s[1])
