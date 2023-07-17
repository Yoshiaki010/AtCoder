"""
#lv1
n,p,q=list(map(int,input().split()))
d=[]
d+=list(map(int,input().split()))
if p > q+min(d):
    ans=q+min(d)
else:
    ans=p
print(ans)
"""
"""
#lv2
n,m=list(map(int,input().split()))
ans="No"
s=[]

for _ in range(n):
    s.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i != j:
            jp=s[j][0]
            jc=s[j][1]
            jf=set(s[j][2::])
            p=s[i][0]
            c=s[i][1]
            f=set(s[i][2::])    
            if p  >= jp:
                for t in f:
                    if t not in jf:
                        break
                else:
                    if p > jp or jc-c >=1:
                        ans="Yes"
                        break
print(ans)
"""
#lv3
n=int(input())
all=set()
ans=0
for _ in range(n):
    ans+=1
    s=input()
    liss=list(s)
    ress=liss[::-1]
    if s in all or "".join(ress) in all:
        ans-=1
    else:
        all.add(s)
print(ans,all)
