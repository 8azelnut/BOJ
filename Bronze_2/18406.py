n = input()

mid = len(n) // 2

left = right = 0
for i in n[:mid]:
    left += int(i)

for i in n[mid:]:
    right += int(i)

print("LUCKY" if left == right else "READY")
