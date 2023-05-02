n = int(input())

for i in range(n):
    s = input()

    middle_s = len(s) // 2 - 1

    if s[middle_s] == s[middle_s + 1]:
        print("Do-it")
    else:
        print("Do-it-Not")
