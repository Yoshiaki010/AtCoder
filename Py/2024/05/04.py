#lv1
"""
n,x,y,z=map(int,input().split())
ans="Unknow"
if x < y:
    if x < z and z < y:
        ans="Yes"
    else:
        ans="No"
else:
    if y < z and z < x:
        ans="Yes"
    else:
        ans="No"
print(ans)
"""
#lv2
"""
"""
s=input()
t=input()
a=[]
now=0
c=len(t)
for i in range(c):
    if t[i] == s[now]:
        print(i+1,end=" ")
        if c-1 < now+1:
            break
        else:
            now+=1
    else:
        continue
#lv3
"""
"""
