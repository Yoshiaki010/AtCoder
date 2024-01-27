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
maxdish=0
for i in range(n):
    max=0
    maxa=q[i]//a[i]
    maxb=q[i]//b[i]
    if maxa < maxb:
        max=(maxa-1)+(q[i]-a[i]*(maxa-1))//b[i]
    else:
        max=(maxb-1)+(q[i]-b[i]*(maxb-1))//a[i]
    if maxdish < max:
        maxdish= max
    print(max)
"""
"""
