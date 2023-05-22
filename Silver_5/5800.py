k = int(input())

for i in range(k):
    li = list(map(int, input().split()))

    tmp = li[1:]
    tmp.sort()

    max_value = 0
    for j in range(len(tmp)-1):
        max_value = max(max_value, abs(tmp[j] - tmp[j+1]))

    print(f"Class {i+1}")
    print(f"Max {max(tmp)}, Min {min(tmp)}, Largest gap {max_value}")
