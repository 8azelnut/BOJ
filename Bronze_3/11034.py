while True:
    try:
        a, b, c = map(int, input().split())

        max_value = max(b - a, c - b)

        print(max_value - 1)

    except:
        break
