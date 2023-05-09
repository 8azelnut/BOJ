s = input()

res = 0
for i in s:
    if i.isupper():
        res += ord(i) - 38
    else:
        res += ord(i) - 96

prime = False
for i in range(2, res):
    if res % i == 0:
        prime = True

if prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")
