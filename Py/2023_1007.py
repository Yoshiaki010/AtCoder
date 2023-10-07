"""
#lv1
s=list(map(int,input())) 
gu=s[1::2]
ans="Unknow"
if sum(gu) == 0:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
"""
#lv2
n=int(input())
r=[]
ans=[]
for i in range(n):
    r.append([i+1,0])
    s=list(input())
    for j in range(len(s)):
        if s[j] == "o":
            r[i][1]+=1
        elif s[j] == "x":
            r[i][1]-=1
        else:
            continue
ans=sorted(r, key=lambda x: x[1],reverse=True)
for i in range(n):
    print(ans[i][0],end=" ")
"""
#lv3
n,m=map(int,input().split())
a=list(map(int,input().split()))
p=[0]*n
noslv=[]
for i in range(n):
    noslv.append([])
    s=list(input())
    p[i]+=i+1
    for j in range(m):
        if s[j] == "o":
            p[i]+=a[j]
        else:
            noslv[i].append(a[j])
    noslv[i].sort(reverse=True)
onep=max(p)
onenum=p.count(onep)
for i in range(n):
    ans=1
    if onenum == 1:
        ans=0
    if onep != p[i]:
        ifp=p[i]
        for j in range(len(noslv[i])):
            ifp+=noslv[i][j]
            ans+=1
            if ifp >= onep:
                break
            else:
                continue
    print(ans)
