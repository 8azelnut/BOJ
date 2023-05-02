for i in range(1, int(input())+1):
    li = sorted(map(int, input().split()))

    if li[0] + li[1] <= li[2]:
        print(f"Case #{i}: invalid!")
    elif li[0] == li[1] == li[2]:
        print(f"Case #{i}: equilateral")
    elif li[0] == li[1] or li[0] == li[2] or li[1] == li[2]:
        print(f"Case #{i}: isosceles")
    else:
        print(f"Case #{i}: scalene")
