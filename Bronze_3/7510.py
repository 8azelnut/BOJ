n = int(input())

for i in range(1, n+1):
    li = sorted(map(int, input().split()))

    if li[2] ** 2 == li[0] ** 2 + li[1] ** 2:
        print(f"Scenario #{i}:")
        print("yes")
        print()
    else:
        print(f"Scenario #{i}:")
        print("no")
        print()
