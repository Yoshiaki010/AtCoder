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
a=[]
for i in range(2**n):
    new=list(bin(i))
    a.append(["0"]*(n-len(new[2:]))+new[2:])
print(a,ans)
t=[]
for i in range(m):
    t.append(input().split())

for _ in range(2**n):
    for i in range(m):
        i