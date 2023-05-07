n = int(input())
s = input()

s_cnt = b_cnt = 0
ss = ""

for i in s:
    ss += i

    if ss == "security":
        s_cnt += 1
        ss = ""
    elif ss == "bigdata":
        b_cnt += 1
        ss = ""

if s_cnt > b_cnt:
    print("security!")
elif s_cnt < b_cnt:
    print("bigdata?")
else:
    print("bigdata? security!")
