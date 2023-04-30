num = int(input())

alphabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

for i in range(num):
    s = set(input())

    m = alphabet - s

    res = 0
    for j in m:
        res += ord(j)

    print(res)
