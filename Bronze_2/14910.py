li = list(map(int, input().split()))

sorted_li = sorted(li)

if sorted_li == li:
    print("Good")
else:
    print("Bad")
