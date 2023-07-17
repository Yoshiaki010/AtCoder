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
s=[]
ans=[]
for _ in range(n):
    s.append(list(input()))
for i in range(n):
    for j in range(n):
        if i < j:
            if j not in ans:
                sj=s[j]
                revs=sj[::-1]
                if s[i] == s[j] or s[i] == revs:
                    ans+=[j]
                    
print(len(ans))