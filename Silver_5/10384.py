for i in range(int(input())):
    s = input().lower()

    check = [0 for _ in range(26)]

    for j in s:
        if 97 <= ord(j) <= 122:
            check[ord(j)-97] += 1

    if min(check) == 0:
        print(f"Case {i+1}: Not a pangram")
    elif min(check) == 1:
        print(f"Case {i+1}: Pangram!")
    elif min(check) == 2:
        print(f"Case {i+1}: Double pangram!!")
    elif min(check) == 3:
        print(f"Case {i + 1}: Triple pangram!!!")
