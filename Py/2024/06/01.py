#lv1
"""
n,l,r=map(int,input().split())
ans=""
for i in range(n):
    i+=1
    if i < l or r < i:
        ans+=str(i)
    else:
        ans+=str((r-i)+l)
    ans+=" "
print(ans)
"""
#lv2
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans="Unknow"
for _ in range(n):
    x=list(map(int,input().split()))
    for j in range(m):
        a[j]-=x[j]
for i in range(m):
    if 0 < a[i]:
        ans="No"
        break
    else:
        continue
else:
    ans="Yes"
print(ans)
"""
#lv3
"""
"""
n,m,k=map(int,input().split())
ans=2**n
a=3
y=0
def all(x,c):
    x-=1
    if 0 < x:
        for _ in range(2):
            c+="1"
            all(x,c)
    else:
        c+=" "
        print(c)
    return()

print(all(a,""))

for i in range(2):
    new=[]
    for j in range(2):
        for k in range(2):
            new=[i,j,k]
#            print(new)
#print(a,ans)