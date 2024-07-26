#lv2
"""
n=int(input())
a=list(map(int,input().split()))
angle=0
angles=[0]
for i in range(n):
    angle+=a[i]
    if 360 < angle:
        overangle=angle-360
        angle=overangle
        angles.append(overangle)
    else:
        angles.append(angle)

angles.sort()

ans=[]
for i in range(n):
    ans.append(angles[i+1]-angles[i])
ans.append(360-sum(ans))
print(max(ans))
"""

#lv2
"""
n=int(input())
a=list(map(int,input().split()))
now=0
ans=""

for i in range(n-1):
    if abs(a[i] - a[i+1]) == 1:
        ans+=str(a[i])+" "
    else:
        if a[i] < a[i+1]:
            for j in range(a[i+1]-a[i]):
                ans+=str(a[i]+j)+" "
        else:
            for j in range(a[i]-a[i+1]):
                ans+=str(a[i]-j)+" "
ans+=str(a[-1])+" "

print(ans)
"""

#lv3
"""
"""

#lv3
"""
"""

#lv4
"""
"""