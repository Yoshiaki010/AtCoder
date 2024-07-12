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
h,w=map(int,input().split())
a=[]
for _ in range(h):
    a.append(list(map(int,input().split())))
h,w=map(int,input().split())
b=[]
for _ in range(h):
    b.append(list(map(int,input().split())))
print(a)
print(b)

#lv4
"""
"""
