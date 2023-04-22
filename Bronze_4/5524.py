num = int(input())

for i in range(num):
    input_str = input()

    result = ""
    for j in input_str:
        if j.isupper():
            result += j.lower()
        else:
            result += j

    print(result)
