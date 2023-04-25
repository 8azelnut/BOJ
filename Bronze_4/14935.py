def fa_func(num: int):
    s = str(num)

    if num == int(s[0]) * len(s):
        return "FA"

    return fa_func(int(s[0]) * len(s))


x = int(input())

print(fa_func(x))
