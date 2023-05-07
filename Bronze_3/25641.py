n = int(input())
li = list(input())

while True:
    if li.count("s") == li.count("t"):
        break
    else:
        li.pop(0)

print(*li, sep="")
