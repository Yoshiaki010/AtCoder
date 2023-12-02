"""
#lv1
am,ad=map(int,input().split()) 
y,m,d=map(int,input().split())
d+=1
if ad < d+1:
    d=1
    m+=1
if am < m:
    m=1
    y+=1
print(y,m,d)
"""
"""
#lv2
n,s,m,b=map(int,input().split())
ans=[]
nums=n//6+2
numm=n//8+2
numb=n//12+2
for i in range(nums):
    for j in range(numm):
        for k in range(numb):
            kosuu=i*6+j*8+k*12
            if n <= kosuu:
                nedan=s*i+m*j+b*k
                ans.append(nedan)
print(min(ans))
"""
"""
#lv3
n=int(input())
a=list(map(int,input().split()))
b=[]
bdic={}
all=0
for i in range(n):
    b.append(a[i])
b.sort()
num=b[0]
for i in range(n):
    all+=a[i]
c=0
bdic[b[-1]]=all
for i in range(n-1):
    c+=b[i]
    if b[i] < b[i+1]:
        bdic[b[i]]=c
for i in range(n):
    ans=all-bdic[a[i]]
    print(ans,end=" ")
"""
