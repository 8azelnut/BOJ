n = int(input())

q_1 = q_2 = q_3 = q_4 = axis = 0

for i in range(n):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        axis += 1
    elif x > 0 and y > 0:
        q_1 += 1
    elif y < 0 < x:
        q_4 += 1
    elif x < 0 < y:
        q_2 += 1
    else:
        q_3 += 1

print(f"Q1: {q_1}")
print(f"Q2: {q_2}")
print(f"Q3: {q_3}")
print(f"Q4: {q_4}")
print(f"AXIS: {axis}")
