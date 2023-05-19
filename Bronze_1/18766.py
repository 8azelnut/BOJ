for i in range(int(input())):
    n = int(input())
    o_li = sorted(list(input().split()))
    k_li = sorted(list(input().split()))

    print("NOT CHEATER" if o_li == k_li else "CHEATER")
