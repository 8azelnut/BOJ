t = int(input())

for i in range(t):
    li = input().split()

    a, b, c = int(li[0]), int(li[2]), int(li[4])
    op = li[1]

    res = 0
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        res = a // b

    print("correct" if res == c else "wrong answer")
