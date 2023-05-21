import sys

t = int(input())

for _ in range(t):
    space = input()

    r, c = map(int, input().split())

    li = []
    for _ in range(r):
        li.append(sys.stdin.readline())

    cnt = 0
    for i in range(r):
        for j in range(c-2):
            if li[i][j] == ">" and li[i][j+1] == "o" and li[i][j+2] == "<":
                cnt += 1

    for i in range(r-2):
        for j in range(c):
            if li[i][j] == "v" and li[i+1][j] == "o" and li[i+2][j] == "^":
                cnt += 1

    print(cnt)
