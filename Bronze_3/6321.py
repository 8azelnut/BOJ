n = int(input())

for i in range(1, n+1):
    s = input()

    res_s = ""
    for j in s:
        res_s += chr(int(ord(j) + 1)).replace("[", "A")

    print(f"String #{i}")
    print(res_s)
    print()
