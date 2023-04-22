input_list = []
for i in range(5):
    input_list.append(int(input()))

h_min = min(input_list[0], input_list[1], input_list[2])
b_min = min(input_list[3], input_list[4])

print(h_min + b_min - 50)
