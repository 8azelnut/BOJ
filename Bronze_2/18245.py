i = 1
while True:
    s = input()

    if s == "Was it a cat I saw?":
        break

    print(s[::i+1])

    i += 1
