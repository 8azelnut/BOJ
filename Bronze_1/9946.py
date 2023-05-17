i = 1
while True:
    s1 = input()
    s2 = input()

    if s1 == "END" and s2 == "END":
        break

    s_s1 = sorted(list(s1))
    s_s2 = sorted(list(s2))

    if s_s1 == s_s2:
        print(f"Case {i}: same")
    else:
        print(f"Case {i}: different")

    i += 1
