#lv1
"""
x,y=map(int,input().split())
ans="No"
if x > y:
    if x - y <= 3:
        ans="Yes"
else:
    if y - x <= 2:
        ans="Yes"
print(ans)
"""
#lv2
"""
n=input()
inn=int(n)
for _ in range(920-inn):
    lisn=list(map(int,n))
    if lisn[0]*lisn[1] == lisn[2]:
        ans=inn
        break
    inn+=1
    n=str(inn)

print(ans)
"""
    
#lv3
"""
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
mina=a[0]
pre=[]
maxpre=0
for x in a:
    pre.append(0)
    if x < mina+m:
        map(+1,pre)
    else:
        if ans < maxpre:
            ans=maxpre
            maxpre=0
print(pre)
print(ans)
#lv4
"""
"""