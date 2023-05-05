li = list(map(int, input().split()))

score_li = [100, 100, 200, 200, 300, 300, 400, 400, 500]

is_hacker = False
for i in range(9):
    if li[i] > score_li[i]:
        is_hacker = True
        break

if is_hacker:
    print("hacker")
elif sum(li) < 100:
    print("none")
else:
    print("draw")
