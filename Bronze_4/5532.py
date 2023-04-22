from math import ceil

homework_list = []
for i in range(5):
    homework_list.append(int(input()))

k = ceil(homework_list[1] / homework_list[3])
m = ceil(homework_list[2] / homework_list[4])

max_value = max(k, m)

print(homework_list[0] - max_value)
