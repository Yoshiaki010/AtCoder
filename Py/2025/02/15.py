#lv1
"""
s1,s2 = input().split()

ans = 0
if s1 == "fine":
    if s2 == "fine":
        ans = 4
    else:
        ans = 3
else:
    if s2 == "fine":
        ans = 2
    else:
        ans = 1
print(ans)
"""
#lv2
"""
"""
s = input()

ans = 0
for k in range(len(s)//2):
    k += 1
    for i in range(len(s)-(k*2)):
        if s[i:i+k*3:k] == "ABC":
            ans += 1
        else:
            continue
print(ans)
#lv3
"""
"""
