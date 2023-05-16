t = int(input())

for i in range(t):
    s1, s2 = input().split()

    s_s1 = sorted(list(s1))
    s_s2 = sorted(list(s2))

    if s_s1 == s_s2:
        print(f"{s1} & {s2} are anagrams.")
    else:
        print(f"{s1} & {s2} are NOT anagrams.")
