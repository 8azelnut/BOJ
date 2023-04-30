num = int(input())

for i in range(num):
    space = input()
    students = int(input())

    res = 0
    for j in range(students):
        candy = int(input())
        res += candy

    if res % students == 0:
        print("YES")
    else:
        print("NO")
