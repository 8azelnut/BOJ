n = int(input())

flag = True
for i in range(2, 10):
    v = n
    tmp = ""

    while v:
        tmp += str(v % i)
        v = v // i

    if tmp == tmp[::-1]:
        flag = False
        print(f"{i} {tmp}")

if str(n) == str(n)[::-1]:
    print(f"10 {str(n)}")
elif flag:
    print("NIE")
