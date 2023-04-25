input_list = []
for i in range(5):
    input_list.append(int(input()))

if input_list[0] < 0:
    print((abs(input_list[0]) * input_list[2]) + input_list[3] + (input_list[1] * input_list[4]))
else:
    print((input_list[1] - input_list[0]) * input_list[4])
