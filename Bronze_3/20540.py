s = input()
li = ["E", "I", "S", "N", "T", "F", "J", "P"]

for i in s:
    li.remove(i)

res = "".join(li)

print(res)
