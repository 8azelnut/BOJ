for i in range(int(input())):
    n = int(input())

    c_res = 0
    g_res = 0
    for j in range(n):
        c, g = map(float, input().split())

        c_res += int(c)
        g_res += c * g

        gpa = g_res / c_res

    print(c_res, "%.1f" % gpa)
