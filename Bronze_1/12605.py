for i in range(int(input())):
    li = list(input().split())

    print(f"Case #{i+1}:", *li[::-1])
