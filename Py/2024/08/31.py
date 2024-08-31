#lv1
"""
a,b=map(int,input().split())
diff=abs(a-b)
if diff == 0:
    ans=1
elif diff%2 == 0:
    ans=3
else:
    ans=2
print(ans)
"""
#lv2
"""
n=int(input())
leftpos=0
rightpos=0
tired=0

for i in range(n):
    pos,hand=input().split()
    if hand == "L":
        if leftpos == 0:
            leftpos=int(pos)
        else:
            tired+=abs(leftpos-int(pos))
            leftpos=int(pos)
    else:
        if rightpos == 0:
            rightpos=int(pos)
        else:
            tired+=abs(rightpos-int(pos))
            rightpos=int(pos)
print(tired)
"""
#lv3
"""
n=int(input())
a=list(map(int,input().split()))
difflong=[[-1,0]]
diffnum=0
before=0
for i in range(n-1):
    j=i+1
    if difflong[before][0] == a[j]-a[i] and difflong[before][1] == i:
        difflong[before][1]+=1
        difflong[before][2]+=1
    else:
        difflong.append([a[j]-a[i],j,2])
        diffnum+=1
        before+=1
difflong=difflong[1:]

ans=n
for i in range(diffnum):
    ans+=difflong[i][2]*(difflong[i][2]-1)//2
print(ans)
"""
