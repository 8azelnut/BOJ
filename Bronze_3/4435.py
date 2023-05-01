t = int(input())

for i in range(1, t+1):
    g_li = list(map(int, input().split()))
    s_li = list(map(int, input().split()))

    g_res = g_li[0] + g_li[1] * 2 + g_li[2] * 3 + g_li[3] * 3 + g_li[4] * 4 + g_li[5] * 10
    s_res = s_li[0] + s_li[1] * 2 + s_li[2] * 2 + s_li[3] * 2 + s_li[4] * 3 + s_li[5] * 5 + s_li[6] * 10

    if g_res > s_res:
        print(f"Battle {i}: Good triumphs over Evil")
    elif g_res < s_res:
        print(f"Battle {i}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i}: No victor on this battle field")
