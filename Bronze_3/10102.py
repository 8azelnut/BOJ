v = int(input())

s = input()

for i in s:
    if s.count("A") > s.count("B"):
        print("A")
        break
    elif s.count("A") < s.count("B"):
        print("B")
        break
    else:
        print("Tie")
        break
