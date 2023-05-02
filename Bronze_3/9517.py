k = int(input())
n = int(input())

time_limit = 0
for i in range(n):
    t, z = input().split()

    time_limit += int(t)

    if time_limit >= 210:
        print(k)
        break

    if z == "T":
        k += 1

    if k > 8:
        k = 1

