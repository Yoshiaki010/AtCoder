"""
#lv1
a,b=list(map(int,input().split()))
ans="No"
if a % 3 != 0:
    if a+1 == b:
        ans="Yes"
print(ans)
"""
"""
#lv2
n=int(input())
b=[]
ans=[]
for i in range(n):
    b+=[list(map(int,input()))]

for i in range(n):
    if i == 0:
        ans+=[[b[1][0]]+b[0][:n-1]]
    elif i == n-1:
        ans+=[b[n-1][1:n]+[b[n-2][n-1]]]
    else:
        ans+=[[b[i+1][0]]+b[i][1:n-1]+[b[i-1][n-1]]]
for i in ans:
    for j in i:
        print(j,end="")
    print()
"""
"""
#lv3
n,k=list(map(int,input().split()))
ab=[]
total=0
ans=1
p=[]
for i in range(n):
    a,b=list(map(int,input().split()))
    ab.append([a,b])
    total+=b

ab.sort(key=lambda x:x[0])

for i in ab:
    if total<=k:
        break
    else:
        ans=i[0]+1
        total-=i[1]
print(ans)
"""