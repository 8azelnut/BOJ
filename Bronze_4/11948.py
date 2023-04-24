score_list = []
for i in range(6):
    score_list.append(int(input()))

f_max = sorted(score_list[:4])
s_max = max(score_list[4:])

print(sum(f_max[1:]) + s_max)
