li = [int(input()) for i in range(8)]

s_li = sorted(li)

tmp = [li.index(i)+1 for i in s_li[-5:]]

tmp.sort()

print(sum(s_li[-5:]))
print(*tmp)
