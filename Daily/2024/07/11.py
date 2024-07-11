#lv2
"""
n=int(input())
angle=0
x=0
y=0
t=input()
for i in range(n):
    if t[i] == "S":
        if angle == "u":
            y+=1
        elif angle == "d":
            y-=1
        elif angle == "l":
            x-=1
        else:
            x+=1
    else:
        if angle == "u":
            angle="r"
        elif angle == "d":
            angle="l"
        elif angle == "l":
            angle="u"
        else:
            angle="d"
print(x,y)
"""

#lv2
"""
n=int(input())
a=list(map(int,input().split()))

all=[0]*n

for i in range(n):
    for j in range(i+1):
        all[j]+=a[i]

ans=0
for i in range(n):
    if 3 < all[i]:
        ans+=1
print(ans)
"""
#lv3
"""
n,m=map(int,input().split())
tree=[]


for i in range(n):
    tree.append([])

for _ in range(m):
    u,v=map(int,input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

def check(nexts):
    while 0 < len(nexts):
        morenexts=[]
        for next in nexts:
            if treeflat[next] == "x":
                continue
            else:
                treeflat[next] = "x"
                morenexts+=tree[next]
        nexts=morenexts

ans=0
treeflat=list("o"*n)
for i in range(n):
    if treeflat[i] != "x":
        ans+=1
        check(tree[i])
    else:
        continue

print(ans)
"""
#lv3
"""
n,m,h,k=map(int,input().split())
s=input()
items=dict()
for _ in range(m):
    x,y=map(int,input().split())
    items[(x,y)] = True
x=0
y=0
ans="Unkow"
for i in range(n):
    if s[i] == "U":
        y+=1
    elif s[i] == "D":
        y-=1
    elif s[i] == "L":
        x-=1
    else:
        x+=1
    h-=1
    if h < 0:
        ans="No"
        break
    else:
        if (x,y) in items:
            if items[ (x,y) ] and h < k:
                items[(x,y)] = False
                h=k
            else:
                continue
        else:
            continue
else:
    ans="Yes"
print(ans)
"""
#lv4
"""
"""