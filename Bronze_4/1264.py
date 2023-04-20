str_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

while True:
    input_str = input()

    if input_str == "#":
        break

    cnt = 0
    for i in input_str:
        if i in str_list:
            cnt += 1

    print(cnt)
