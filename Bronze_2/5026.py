n = int(input())

for i in range(n):
    s = input()

    if s == "P=NP":
        print("skipped")
    else:
        s = s.split("+")

        print(sum(list(map(int, s))))
