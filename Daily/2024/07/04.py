#lv2
"""
a,b,k=map(int,input().split())
ans=0
while a < b:
    ans+=1
    a*=k
print(ans)
"""
#lv2
"""
s=list(input())
s.sort()
n=len(s)
ans=""
for i in range(n):
    ans+=s[i]
print(ans)
"""
#lv3
"""
n=int(input())

hashigo=dict()
hashigo[1]=set()
for _ in range(n):
    a,b=map(int,input().split())
    if a in hashigo:
        hashigo[a].add(b)
    else:
        hashigo[a]={b}
    if b in hashigo:
        hashigo[b].add(a)
    else:
        hashigo[b]={a}

next=[1]
ans=0
while 0 < len(next):
    newnext=[]
    for now in next:
        if ans < now:
            ans=now
        newnext+=list(hashigo[now])
        hashigo[now]={}
    next=newnext
print(ans)
"""

#lv3
"""
"""
ah,aw=map(int,input().split())
a=[]
for _ in range(ah):
    a.append(list(map(int,input().split())))


bh,bw=map(int,input().split())
b=[]
for _ in range(bh):
    b+=list(map(int,input().split()))

for i in range(ah):
    print(a[i])
print(b)

sameplace=[]
samehw=0
ans="Unknow"
for i in range(ah):
    for j in range(aw):
        if samehw == bh*bw:
            break
        else:
            if a[i][j] == b[samehw]:
                sameplace.append(j)
                samehw+=1
            else:
                continue
    else:
        continue
    break
else:
    ans="No"

ans=[]
print(sameplace)

for i in range(bw-1):
    samei=sameplace[i::bw]
    samej=sameplace[i+1::bw]
    print(set(samei),set(samej))
    if len(set(samei)) == 1  and len(set(samej)) == 1 and samei[0] < samej[0]:
            continue
    else:
        ans="No"
        break
else:
    ans="Yes"
print(ans)
#lv4
"""
"""
