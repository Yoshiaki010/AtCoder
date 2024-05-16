#lv2
"""
p,q=input().split()
line={"A":0,"B":3,"C":4,"D":8,"E":9,"F":14,"G":23}
if line[p] < line[q]:
    ans=line[q]-line[p]
else:
    ans=line[p]-line[q]
print(ans)
"""
#lv2
"""
a=[]
c=0
q=int(input())
for i in range(q):
    n,xk=map(int,input().split())
    if n == 1:
        a.append(xk)
        c+=1
    else:
        print(a[c-xk])
"""
#lv3
"""
"""
n,m=map(int,input().split())
s=[]
for _ in range(n):
    s.append(input())

t=[]
miss=0
while miss < 2:
    for i in range(m):
        

ans="No"
for i in range(n-1):
    t=t[i]
    nextt=t[i+1]
    miss=0
    for j in range(m):
        if t[j] == nextt[j]:
            continue
        else:
            miss+=1
    if 1 < miss:
        ans="No"
        break
    else:
        continue
else:
    ans="Yes"
print(s,ans)
#lv3
"""
n=int(input())
ans=0
k=0
for i in range(n):
    ans+=i+1
ans%=998244353
print(ans)
"""
#lv4
"""
"""
