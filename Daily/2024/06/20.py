#lv2
"""
n,d=map(int,input().split())
s=""
for _ in range(n):
    s+=input()
ans=0
now=0
for i in range(n):
    if s[i::d] == "o"*n:
        now+=1
    else:
        if ans < now:
            ans=now
        now=0
else:
    if ans < now:
        ans=now
print(ans)
"""
#lv3
"""
n,m=map(int,input().split())
p=[]
for i in range(n):
    p.append([n,i])

for i in range(m):
    x,y=map(int,input().split())
    p[y-1][0]=p[x-1][0]-1

maxp=0
for i in range(n):
    if p[i][0] == n:
        maxp+=1
        ans=p[i][1]+1

if 1 < maxp:
    ans=-1
print(ans)
"""
#lv3
"""
"""
n,m=map(int,input().split())
s=input()
c=list(map(int,input().split()))
s_colors=[]

def rotation(lis):
    all=len(lis)
    fast=lis[all-1]
    return fast+lis[1:all-1]

for i in range(m):
    s_colors.append([])

for i in range(n):
#lv3
"""
"""
#lv4
"""
"""
