s = input()

a = "BCDF"
b = "CDF"
c = "DF"

if "A" in s:
    for i in s:
        if i in a:
            s = s.replace(i, "A")
elif "B" in s:
    for i in s:
        if i in b:
            s = s.replace(i, "B")
elif "C" in s:
    for i in s:
        if i in c:
            s = s.replace(i, "C")
else:
    s = "A" * len(s)

print(s)
