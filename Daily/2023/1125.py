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
while ans < 33:
    f=d-ans
    x=1
    while x**2 < f:
        print(x)
        y=1
        while y**2 < f-x:
            if (x**2)+(y**2) == f:
                break
            y+=1
        else:
            x+=1
            continue
        break
    else:
        ans+=1
        continue
    break
print(ans)