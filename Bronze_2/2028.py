t = int(input())

for i in range(t):
    n = int(input())

    n_square = str(n * n)
    n_len = len(str(n))

    if n_square[-n_len:] == str(n):
        print("YES")
    else:
        print("NO")
