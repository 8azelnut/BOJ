li = list(map(int, input().split()))

odd = False
odd_res = 1
even_res = 1
for i in li:
    if i % 2 == 1:
        odd_res *= i
        odd = True
    else:
        even_res *= i

if odd:
    print(odd_res)
else:
    print(even_res)
