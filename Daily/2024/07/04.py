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
n=int(input())
keyset=set()
hashigolist=[]
for i in range(n):
    a,b=map(int,input().split())
    hashigolist.append([a,b])
    keyset.add(a)
    keyset.add(b)

keylist=list(keyset)

hashigodict=dict()
hashigodict[1]=[]
for i in range(len(keylist)):
    hashigodict[keylist[i]]=[]

for i in range(n):
    a,b=hashigolist[i]
    hashigodict[a].append(b)
    hashigodict[b].append(a)

print(hashigolist)
print(hashigodict)

worked=set()
nexts=[1]
ans=0
"""
while 0 < nexts:
    newnext=set()
    for now in nexts:
        next=hashigo[now]
        if next in newnext:
            continue
        else:
            newnext.add(next)
    next.append(hashigo[now])
    hashigo[now]=[]

print(ans)
"""
#lv3
"""
"""

#lv4
"""
"""
