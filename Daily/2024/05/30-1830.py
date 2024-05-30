#lv2
"""
n=int(input())
a=set(map(int,input().split()))
ans=len(a)
print(ans)
"""
#lv2
"""
n,p=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    if a[i] < p:
        ans+=1
    else:
        continue
print(ans)
"""
#lv3
"""
n=int(input())
now=[1]*9
for _ in range(n-1):
    new=[]
    for i in range(9):
        if i == 0:
            new.append((now[i]+now[i+1])%998244353)
        elif i == 8:
            new.append((now[i]+now[i-1])%998244353)
        else:
            new.append((now[i-1]+now[i]+now[i+1])%998244353)
    now=new
ans=0
for i in range(9):
    ans=(ans+now[i])%998244353
print(ans)
"""
#lv3
"""
"""
n=int(input())

def cut(n,a):
    tate=[]
    yoko=[]
    for i in range(n):
        for j in range(n):
            if a[i][j] == "#":
                yoko.append(j)
                tate.append(i)
            else:
                continue
    yoko.sort()
    new=""
    nx=yoko[-1]-yoko[0]+1
    for i in range(n):
        if tate[0] <= i and i <= tate[-1]:
            new+=a[i][yoko[0]:yoko[-1]+1]
    return(new,nx)

s=[]
t=[]
for _ in range(n):
    s.append(input())
for _ in range(n):
    t.append(input())

s,sk=cut(n,s)
t,tk=cut(n,t)
print(s,t,tc,tk)

for i in range(4):
    if s == t:
        ans="Yes"
        break
    else:
        pass
    new=""
    for i in range():
    new+=t[tc-tk:]+t[:tc-tk]
    t=new
    print(t)
else:
    ans="No"
print(ans)
#lv4
"""
"""
