while True:
    n = int(input())

    if n == -1:
        break

    li = [i for i in range(1, n) if n % i == 0]

    if sum(li) == n:
        res_li = [str(i) for i in li]

        print(f"{n} =", " + ".join(res_li))
    else:
        print(f"{n} is NOT perfect.")
