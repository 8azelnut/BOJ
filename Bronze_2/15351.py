n = int(input())

for i in range(n):
    s = input().replace(" ", "")

    res = 0
    for j in s:
        res += ord(j) - 64
        
    if res == 100:
        print("PERFECT LIFE")
    else:
        print(res)
