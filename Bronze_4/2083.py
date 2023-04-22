while True:
    str_list = list(input().split())

    if str_list[0] == "#" and str_list[1] == "0" and str_list[2] == "0":
        quit()

    if int(str_list[1]) > 17 or int(str_list[2]) >= 80:
        print(f"{str_list[0]} Senior")
    else:
        print(f"{str_list[0]} Junior")
