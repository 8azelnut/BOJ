cute_res = 0
not_cute_res = 0
for i in range(int(input())):
    s = input()

    if s == "1":
        cute_res += 1
    else:
        not_cute_res += 1

if cute_res > not_cute_res:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
