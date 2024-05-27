#lv1
"""
a,b=map(int,input().split())
h=[0,0,0]
h[a-1]=1
h[b-1]=1
c=0
ans=-1
for i in range(3):
    if h[i] == 1:
        continue
    else:
        c+=1
        ans=i+1
if c == 2:
    ans=-1
else:
    pass
print(ans)
""" 
#lv2
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dica={}

c=a+b
c.sort()

ans="No"
for i in range(n+m-1):
    if c[i] in a and c[i+1] in a:
        ans="Yes"
        break
    else:
        continue
else:
    ans="No"
print(ans)
"""

#lv3
"""
"""
n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=0
tate=[0]*n
yoko=[0]*n
naname=[0]*2
for i in range(t):
    tate[a[i]%n]+=1
    yoko[a[i]%n]+=1
    if a == a:
        naname[0]+=1
    else:
        naname[1]+=1
print(ans)

#lv4
"""
"""