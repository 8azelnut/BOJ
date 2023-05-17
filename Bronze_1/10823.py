res = ""
while True:
    try:
        res += input()
    except:
        break

print(sum(map(int, res.split(","))))
