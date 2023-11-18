"""
#A
n=int(input())
p=list(map(int,input().split()))
p+=[0]
ans=0
saikyo=max(p[1::])
if p[0] > saikyo:
    ans=0
else:
    ans=saikyo-p[0]+1
print(ans)
"""
"""
#B
n,m=list(map(int,input().split()))
ans=-1
x,y=[],[]
for i in range(n):
    x+=[i+1]

if m >= n-1:
    for _ in range(m):
        a,b=list(map(int,input().split()))
        if b not in y:
            x.remove(b)
            y+=[b]
    if len(x) == 1:
        ans=x[0]

print(ans)
"""
