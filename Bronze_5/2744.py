input_str = input()

result = ""
for i in input_str:
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()

print(result)
