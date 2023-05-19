n, s = input().split()

n = int(n)

res = ""
li = []
for i in range(n):
    nick, chat = input().split()

    if nick == s:
        res = chat

    li.append([nick, chat])

cnt = 0
for i in range(len(li)):
    if li[i][1] == res:
        if li[i][0] != s:
            cnt += 1
    if li[i][0] == s:
        print(cnt)
        break
