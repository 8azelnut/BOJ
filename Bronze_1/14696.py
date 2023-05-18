for i in range(int(input())):
    a_li = list(map(int, input().split()))[1:]
    b_li = list(map(int, input().split()))[1:]

    a_star_cnt, b_star_cnt = a_li.count(4), b_li.count(4)
    a_circle_cnt, b_circle_cnt = a_li.count(3), b_li.count(3)
    a_square_cnt, b_square_cnt = a_li.count(2), b_li.count(2)
    a_triangle_cnt, b_triangle_cnt = a_li.count(1), b_li.count(1)

    if a_star_cnt > b_star_cnt: print("A")
    elif a_star_cnt < b_star_cnt: print("B")
    elif a_circle_cnt > b_circle_cnt: print("A")
    elif a_circle_cnt < b_circle_cnt: print("B")
    elif a_square_cnt > b_square_cnt: print("A")
    elif a_square_cnt < b_square_cnt: print("B")
    elif a_triangle_cnt > b_triangle_cnt: print("A")
    elif a_triangle_cnt < b_triangle_cnt: print("B")
    else: print("D")
