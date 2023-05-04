x_li, y_li = [], []
for i in range(int(input())):
    x, y = map(int, input().split())

    x_li.append(x)
    y_li.append(y)

print((max(x_li) - min(x_li) + max(y_li) - min(y_li)) * 2)
