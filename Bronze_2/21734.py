s = input()

for i in s:
    v = ord(i) // 100 + (ord(i) // 10) % 10 + ord(i) % 10

    print(i * v)
