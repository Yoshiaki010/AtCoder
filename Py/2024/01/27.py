#lv1
"""
s=input()
ans="Unknow"
if s[0] != s[0].lower():
    for i in range(len(s)-1):
        if s[i+1] == s[i+1].upper():
            ans="No"
            break
    else:
        ans="Yes"
else:
    ans="No"
print(ans)
"""
#lv2
"""
s=input()
smax=0
ans=[]
lenans=0
dct=dict()
for i in s:
    dct[i]=0

for i in s:
    dct[i]+=1
    if max < dct[i]:
        max=dct[i]
        lenans=1
        ans=[i]
    elif max == dct[i]:
        lenans+=1
        ans.append(i)
    else:
        continue
if 1 <= lenans:
    ans.sort()
print(ans[0])
"""
#lv3
n=int(input())
q=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ansa=0
ansb=0
maxdish=0
for i in range(n):
    max=0
    maxa=q[i]//a[i]
    maxb=q[i]//b[i]
    if maxa < maxb:
        maxa-=1
        maxb=(q[i]-a[i]*(maxa))//b[i]
        max=maxa+(q[i]-a[i]*maxa)//b[i]
    else:
        maxb-=1
        maxa=(q[i]-b[i]*(maxb))//a[i]
        max=maxb+(q[i]-b[i]*maxb)//a[i]
    print(max,"a=",maxa,"b=",maxb)
    if maxa < ansa and maxb < ansb:
        if maxdish < max:
            maxdish= max
            ansa=maxa
            ansb=maxb
            print("Yes")
print(maxdish)
print(ansa,ansb)
"""
"""
