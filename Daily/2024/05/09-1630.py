#lv2
"""
"""
a,m,eru,r=map(int,input().split())
ans=0

#lv2
"""
s=input()
t=input()
ws=""
wt=""
ans="Unkow"
for i in range(len(s)-1):
    if s[i] != t[i] and s[i+1] != t[i+1]:
        if i+1 == len(s)-1:
            s=s[0:i]+s[i+1]+s[i]
        else:
            s=s[0:i]+s[i+1]+s[i]+s[i+2:]
        break
    else:
        continue
if s == t:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
#lv3
"""
"""

#lv3
"""
"""

#lv4
"""
"""
