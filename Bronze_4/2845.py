num1, num2 = map(int, input().split())
p_list = list(map(int, input().split()))

multiple = num1 * num2

for i in p_list:
    print(i - multiple, end=" ")
