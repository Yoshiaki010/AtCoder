"""
"""
#lv2
n=int(input())
a=[]
b=[]
onebool=False
ans="No"
for _ in range(n):
    i=list(map(int,input().split()))
    a.append(i)
    seta=set(i)
    if 1 in seta:
        onebool=True
for _ in range(n):
    b.append(list(map(int,input().split())))

for _ in range(4):
    if onebool:
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1:
                    if b[i][j] == 1:
                        continue
                    else:
                        break
            else:
                ans="Yes"
                break
        newaa=[]
        for i in range(n):
            newa=[]
            for j in range(n):
                j+=1
                newa.append(a[n-j][i])
            newaa.append(newa)
        a=newaa
    else:
        ans="Yes"
        break
print(ans)
#lv2
"""
n,m=map(int,input().split())
sara=dict()
c=input().split()
d=input().split()
p=list(map(int,input().split()))
ans=0
for i in range(m):
    sara[d[i]]=p[i+1]
for i in range(n):
    if c[i] in sara:
        ans+=sara[c[i]]
    else:
        ans+=p[0]
print(ans)
"""
#lv3
"""
n,m,h,k=list(map(int,input().split()))
s=list(input())
x=0
y=0
item=[]
ans="Yes"
for i in range(m):
    item.append(list(map(int,input().split())))
for i in range(n):
    if h < 0:
        h-=1
        if s[i] == "R":
            x+=1
        elif s[i] == "L":
            x-=1
        elif s[i] == "U":
            y+=1
        else:
            y-=1
        if h < k:
            if []         
    else:

        ans="No"
print(ans)
"""
#lv3

