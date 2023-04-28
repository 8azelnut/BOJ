num = int(input())

for i in range(1, num+1):
    print("*" * i + " " * 2 * (num - i) + "*" * i)

print(end="")

for i in range(num-1, 0, -1):
    print("*" * i + " " * 2 * (num - i) + "*" * i)
