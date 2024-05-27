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
tate=[0]*(n+1)
yoko=[0]*(n+1)
naname=[0]*3
for i in range(t):
    tate[(a[i]-1)%n]+=1
    yoko[(a[i]-1)//n]+=1
    if tate[n] < tate[(a[i]-1)%n]:
        tate[n]=tate[(a[i]-1)%n]
    else:
        pass
    if yoko[n] < yoko[(a[i]-1)//n]:
        yoko[n]=yoko[(a[i]-1)//n]
    else:
        pass
    if a[i]-1 == (n*n-1)//2:
        naname[0]+=1
        naname[1]+=1
    elif (a[i]-1)%(n+1) == 0:
        naname[0]+=1
    elif (a[i]-1)%(n-1) == 0:
        naname[1]+=1
    else:
        pass
    if naname[2] < naname[0]:
        naname[2]=naname[0]
    elif naname[2] < naname[1]:
        naname[2]=naname[1]
    else:
        pass
    if n == tate[n] or n == yoko[n] or n == naname[2]:
        ans=i+1
        break
    else:
        continue
else:
    ans=-1
print(ans)
#lv4
"""
"""