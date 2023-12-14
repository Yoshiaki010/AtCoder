#lv4
n=int(input())
a=list(map(int,input().split()))
p=list(map(int,input().split()))
ans="?"
lastdif=a[0]
c={0}

newa=a
for i in range(n-1):
    if p[i]-1 in c:
        c.add(i+1)
        lastdif+=a[i+1]
    newa[p[i]-1]=a[i+1]

if lastdif == 0:
    ans=0
elif lastdif < 0:
    ans="-"
else:
    ans="+"
print(ans)
"""
"""