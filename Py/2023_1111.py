"""
#lv1
n,x=map(int,input().split())
s=list(map(int,input().split()))
ans=0
for i in range(n):
    if s[i] <= x:
        ans+=s[i]
print(ans)
"""
#lv2
"""
n=int(input())
d=list(map(int,input().split()))
ans=0
for i in range(n):
    m=str(i+1)
    setm=set(list(m))
    if len(setm) == 1:
        date=int(m[-1])
        if (date*10+date) <= d[i]:
            ans+=2
        elif date <= d[i]:
            ans+=1
print(ans)
"""
#lv3
"""
n,q=map(int,input().split())
s=list(input())
anss=[0]
num=0
for i in range(n-1):
    if s[i] == s[i+1]:
        num+=1
    anss.append(num)
for _ in range(q):
    ans=0
    l,r=map(int,input().split())
    ans=anss[r-1]-anss[l-1]
    print(ans)
"""
