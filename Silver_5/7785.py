n = int(input())

di = {}
for i in range(n):
    name, record = input().split()

    if record == "enter":
        di[name] = record
    else:
        del di[name]

di = sorted(di.keys(), reverse=True)

print(*di, sep="\n")
