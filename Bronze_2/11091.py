n = int(input())
a = [chr(i) for i in range(97, 123)]

for i in range(n):
    s = input().lower()

    res = ""
    for j in range(len(a)):
        if s.find(a[j]) == -1:
            res += a[j]

    if not res:
        print("pangram")
    else:
        print(f"missing {res}")
