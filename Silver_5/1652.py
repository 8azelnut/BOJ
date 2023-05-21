n = int(input())

li = [list(input()) for i in range(n)]

row_cnt = col_cnt = 0
for i in range(n):
    row_res = col_res = ""

    for j in range(n):
        if li[i][j] == ".":
            row_res += "."
        else:
            row_res = ""
        if len(row_res) == 2:
            row_cnt += 1

        if li[j][i] == ".":
            col_res += "."
        else:
            col_res = ""
        if len(col_res) == 2:
            col_cnt += 1

print(row_cnt, col_cnt)
