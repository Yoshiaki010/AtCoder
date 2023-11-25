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
for i in range(d):
    x=1
    while x**2 < d:
        y=(d-ans)-(x**2)
        if (x**2)+((y//2)**2) == d-ans:
            print(d-ans,x**2,y**2)
            break
        print(x**2,(y//2)**2)
        x+=1
    else:
        ans+=1
    break
print(ans)