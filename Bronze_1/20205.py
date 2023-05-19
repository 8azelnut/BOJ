n, k = map(int, input().split())

for i in range(n):
    s = input().split()

    for j in range(k):
        for m in s:
            print(f"{m} " * k, end="")
        print()
