n = int(input())
li = list(map(int, input().split()))

m = int(input())
tmp = list(map(int, input().split()))

di = {}
for i in range(len(li)):
    di[li[i]] = 0

for i in range(m):
    if tmp[i] not in di:
        print(0, end=" ")
    else:
        print(1, end=" ")
