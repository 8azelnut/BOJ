import sys

for i in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())

    cnt = 0
    for j in range(n, m+1):
        s = str(j)
        cnt += s.count("0")

    print(cnt)
