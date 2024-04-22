#lv1 
"""
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    if a[i] % k == 0:
        print(a[i]//k,end=" ")
    else:
        continue
"""
#lv2
"""
s=input()
n=len(s)
ans=0
lists=[]
for i in range(n):
    new=0
    for j in range(n):
        j+=1
        if s[i:j] not in lists and i != j and s[i:j] != "":
            lists.append(s[i:j])
            new+=1
        else:
            continue
    ans+=new
print(ans)
"""
"""
"""
#lv3
n,a,b=map(int,input().split())
d=list(map(int,input().split()))
ans="Unknow"
holid=[0,a+1]
for i in range(n-1):
    now=d[i+1]-d[0]
    w=d[i+1]//(a+b)
    next=(a+b)*w
    if holid[0]+next < now and now < holid[1]+next:
        print(holid[0]+next,now,holid[1]+next)
        continue
    else:
        ans="No"
        break
else:
    ans="Yes"
print(ans)