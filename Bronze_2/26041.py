a = list(input().split())
b = input()

cnt = 0
for i in a:
    if i != b and i[:len(b)] == b:
        cnt += 1

print(cnt)
