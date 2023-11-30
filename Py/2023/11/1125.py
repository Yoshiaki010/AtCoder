"""
#lv1
n,eru=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    if a[i] >= eru:
        ans+=1
print(ans)
"""

"""
#lv2
n,eru,r=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    ans=eru
    if eru <= a[i]:
        if a[i] <= r:
            ans=a[i]
        else:
            ans=r
    print(ans,end=" ")
"""

"""
"""
#lv3
d=int(input())
ans=0
x=int(d**0.5)
y=int((d-x**2)**0.5)
ans=abs((x**2+y**2)-d)
print(x,y)
print(ans)