import sys

li = []
for i in range(int(sys.stdin.readline())):
    li.append(int(sys.stdin.readline()))

li.sort()

print(*li, sep="\n")
