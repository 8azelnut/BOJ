s = input()

joi_cnt = ioi_cnt = 0

for i in range(len(s)-2):
    res = ""
    res += s[i] + s[i+1] + s[i+2]

    if res == "JOI":
        joi_cnt += 1
    if res == "IOI":
        ioi_cnt += 1

print(joi_cnt)
print(ioi_cnt)
