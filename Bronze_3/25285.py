t = int(input())

for i in range(t):
    cm, kg = map(int, input().split())

    bmi = float(kg / (cm * 0.01 * cm * 0.01))

    if cm < 140.1:
        print(6)
    elif 140.1 <= cm < 146:
        print(5)
    elif 146 <= cm < 159:
        print(4)
    elif 159 <= cm < 161:
        if 16.0 <= bmi < 35.0:
            print(3)
        else:
            print(4)
    elif 161 <= cm < 204:
        if 20.0 <= bmi < 25.0:
            print(1)
        elif 18.5 <= bmi < 20.0 or 25.0 <= bmi < 30.0:
            print(2)
        elif 16.0 <= bmi < 18.5 or 30.0 <= bmi < 35.0:
            print(3)
        else:
            print(4)
    elif 204 <= cm:
        print(4)
