k = input()

li = []
for i in range(len(k)-1):
    li.append(int(k[i]) - int(k[i+1]))

if len(k) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
elif len(set(li)) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
