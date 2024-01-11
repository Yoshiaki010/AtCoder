#lv2
"""
sarray=["ABC","ARC","AGC","AHC"]
for i in range(3):
    s=input()
    sarray.remove(s)
print(sarray[0])
"""
#lv2
"""
"""
n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
all=sum(a)
ans=-2
if all-a[-1] >= x:
    ans=0
else:
    diff=x-(all-(a[0]+a[-1]))
    if diff <= 100:
        ans=diff
    else:
        if all-a[0] >=x:
            ans=a[-1]
        else:
            ans=-1
print(ans)