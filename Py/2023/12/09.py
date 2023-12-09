#lv4
n=int(input())
a=list(map(int,input().split()))
p=list(map(int,input().split()))
ans="?"
newa=a
lastdif=0
difdict={}
c={0}

for i in range(n):
    difdict[i]=0

for i in range(n-1):
    dif=a[p[i]-1]+a[i+1]
    print(dif)
    difdict[p[i]-1]+=dif
    newa[p[i]-1]=dif
    if p[i]-1 in c:
        c.add(i+1)
a=newa
list(c)
for i in c:
    lastdif+=difdict[i]
print(c)
print(a)
print(difdict)
"""
if num["+"] == num["-"]:
    ans=0
elif num["+"] < num["-"]:
    ans="-"
else:
    ans="+"
"""
#print(num)
print(lastdif)
print(ans)
"""
"""