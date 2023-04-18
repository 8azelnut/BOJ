num_list = list(map(int, input().split()))

sum = 0
for i in num_list:
    sum += i*i

print(sum % 10)
