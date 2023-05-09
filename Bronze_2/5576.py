w_li = []
k_li = []
for i in range(10):
    w_li.append(int(input()))

for i in range(10):
    k_li.append(int(input()))

w_li.sort()
k_li.sort()

print(sum(w_li[-3:]), sum(k_li[-3:]))
