input_list = list(map(int, input().split()))

max = max(input_list)
min = min(input_list)

value = sum(input_list) - (max + min)

print(abs((max + min) - value))
