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
#lv3
"""
n=int(input())

def cut(n,a):
    atate=[]
    ayoko=[]
    for i in range(n):
        for j in range(n):
            if a[j] == "#":
                ayoko.append(j)
                atate.append(i)
            else:
                continue
    ayoko.sort()
    new=[]
    for i in range(n):
        if atate[0] <= i and i <= atate[-1]:
            new.append(a[i][ayoko[0]:ayoko[-1]+1])
    return(new)
s=[]
t=[]
for _ in range(n):
    s.append(input())
for _ in range(n):
    t.append(input())

s=cut(n,s)
t=cut(n,t)
print(s,t)
"""

#lv4
"""
"""
