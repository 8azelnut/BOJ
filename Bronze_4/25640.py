my_mbti = input()
num = int(input())

str_list = []
for i in range(num):
    str_list.append(input())

cnt = 0
for i in str_list:
    if i == my_mbti:
        cnt += 1

print(cnt)
