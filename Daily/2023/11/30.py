"""
#lv2
s,t=map(int,input().split()) 
ans=0
for i in range(s+1):
    a=i
    for i in range(s+1):
        b=i
        for i in range(s+1):
            c=i
            if a+b+c<=s and a*b*c<=t:
                ans+=1
print(ans)
"""
"""
#lv2
n,m=map(int,input().split())
tdic=dict()
ans=0
for i in range(m):
    tdic[i+1]=set()

for _ in range(m):
    u,v=map(int,input().split())
    tdic[u].add(v)

if 3<=n and 3<=m:
    for i in range(n):
        a=i+1
        for j in list(tdic[a]):
            b=j
            if a < b:
                for k in list(tdic[b]):
                    c=k
                    if b < c and c in tdic[a]:
                        ans+=1
print(ans)
"""
"""
#lv3
n,q=map(int,input().split())
a=[]
adic=dict()
for i in range(n):
    a.append(i+1)
    adic[i+1]=i

for i in range(q):
    x=int(input())
    if adic[x] < n-1:
        r=a[adic[x]+1]

        adic[x]+=1
        adic[r]-=1
        a[adic[x]]=x
        a[adic[r]]=r
    else:
        h=a[adic[x]-1]

        adic[x]-=1
        adic[h]+=1
        a[adic[x]]=x
        a[adic[h]]=h

for i in a:
    print(i,end=" ")
"""
#lv3
q=int(input())
s={}
cs={}

for i in range(q):
    lisq=input().split()
    if lisq[0] == "1":
        x = int(lisq[1])
        if x in s:
            cs[x]=0
        else:
            cs[x]+=1
        s.append(x)
    elif lisq[0] == "2":
        x = int(lisq[1])
        c = int(lisq[2])
        if c < cs[x]:
            t=s[x:c]
    else:
        s.sort()
        print(s[-1]-s[0])