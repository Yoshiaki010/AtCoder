S = input()

o_num = 0
for Si in S:
    if Si == "o":
        o_num+=1

ans = "Unknow"
if o_num % 2 == 0:
    ans = "even"
else:
    ans = "odd"

print(ans)