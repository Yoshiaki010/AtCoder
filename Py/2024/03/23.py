"""
#lv1
n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    b=a[i]*a[i+1]
    print(b,end=" ")
"""
"""
#lv2
s="wbwbwwbwbwbwwbwbwwbwbwbw"
w,b=map(int,input().split())
ans="No"
amari=(w+b)%12
bai=(w+b-amari)//12
sw=7
sb=5
wb=[sw*bai,sb*bai]
for i in range(12):
    nw=0
    nb=0
    for j in range(amari):
        if s[i+j] == "w":
            nw+=1
        else:
            nb+=1
    if [wb[0]+nw,wb[1]+nb] == [w,b]:
        ans="Yes"
        break
    else:
        continue
else:    
    ans="No"
print(ans)
"""

"""
#lv3
n,k=map(int,input().split())
a=list(map(int,input().split()))
if k == 1:
    ans=1
else:
    ans=(k+1)*k//2

see=set()
for i in range(n):
    if a[i] not in see and a[i] <= k:
        ans-=a[i]
        see.add(a[i])
    else:
        continue
print(ans)
"""
