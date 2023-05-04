a_ad, a_li = map(int, input().split())
b_ad, b_li = map(int, input().split())

while True:
    a_li -= b_ad
    b_li -= a_ad

    if a_li <= 0 and b_li <= 0:
        print("DRAW")
        break
    elif a_li <= 0:
        print("PLAYER B")
        break
    if b_li <= 0:
        print("PLAYER A")
        break
