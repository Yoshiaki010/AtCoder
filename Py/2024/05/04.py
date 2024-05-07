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
"""
#lv3
"""
n=int(input())
g=[]
o=[]
t=0
ans=0
for i in range(n):
    a,b=map(int,input().split())
    g.append([a,b])
    o.append([b-a,i])
o.sort()
for i in range(n):
    a=g[o[i][1]][0]
    b=g[o[i][1]][1]
    if i == n-1:
        ans+=t+b
    else:
        t+=a
print(ans)
"""

#lv4
"""
"""
