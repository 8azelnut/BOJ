a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())

ga, gb = a1 + a2, b1 + b2
ea, eb = a3 + a4, b3 + b4

if ga - ea + gb - eb == 0:
    print("Tie")
elif ga - ea + gb - eb > 0:
    print("Gunnar")
else:
    print("Emma")
