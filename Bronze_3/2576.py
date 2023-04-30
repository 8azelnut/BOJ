li = []
odd_li = []
for i in range(7):
    li.append(int(input()))

    if li[i] % 2 != 0:
        odd_li.append(li[i])

if len(odd_li) == 0:
    print(-1)
else:
    print(sum(odd_li))
    print(min(odd_li))
