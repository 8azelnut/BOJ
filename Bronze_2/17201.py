n = int(input())
s = input()

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        print("No")
        quit()

print("Yes")
