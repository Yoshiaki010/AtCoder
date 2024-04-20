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
<<<<<<< HEAD
    s=d[i+1]-d[0]
    w=d[i+1]//(d[0]+a+b)
    p=d[i+1]%(d[0]+a+b)
    print(p)
#    next=(d[0]+a+b)*w
    print(s,holid[0]+next,holid[1]+next)
    if s < holid[0]+next or holid[1]+next < s:
=======
    now=d[i+1]-d[0]
    w=d[i+1]//(a+b)
    next=(a+b)*w
    if holid[0]+next < now or now < holid[1]+next:
        print(now)
        continue
    else:
>>>>>>> dd162713a7875b1f149f554a57facf829a0a65b8
        ans="No"
        break
else:
    ans="Yes"
<<<<<<< HEAD
print(ans)
=======
print(ans)
>>>>>>> dd162713a7875b1f149f554a57facf829a0a65b8
