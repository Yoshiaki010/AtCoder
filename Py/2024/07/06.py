# lv1
"""
n,k,x=map(int,input().split())
a=input().split()
b=[]
b+=a[0:k]+[x]+a[k::]
for i in range(n+1):
    print(b[i],end=" ")
"""

# lv2
"""
a,b,c,d,e,f=map(int,input().split())
g,h,i,j,k,l=map(int,input().split())

a=[a,b,c,d,e,f]
g=[g,h,i,j,k,l]

xyz=[]
for i in range(3):
    aone=a[i]
    atwo=a[i+3]
    gone=g[i]
    gtwo=g[i+3]
    if aone < gone:
        if gtwo < atwo:
            xyz.append(gtwo - gone)
        elif gtwo > atwo:
            xyz.append(atwo - gone)
        else:
            xyz.append(0)
    else:
        if gtwo < atwo:
            xyz.append(gtwo - aone)
        elif gtwo > atwo:
            xyz.append(atwo - aone)
        else:
            xyz.append(0)
x,y,z=xyz
v=x*y*z
if 0 < v:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
# lv3 
"""
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

allpatern=[]
c=0
for i in range(k+1):
    allpatern.append(a[i+(n-k-1)] - a[i])
    c+=1

ans=a[-1]-a[0]
for i in range(c):
    if allpatern[i] < ans:
        ans=allpatern[i]
print(ans)
"""
