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


hashigodict=dict()
hashigodict[1]=[]
for i in keyset:
    hashigodict[i]=[]

for i in range(n):
    a,b=hashigolist[i]
    hashigodict[a].append(b)
    hashigodict[b].append(a)

print(hashigolist)
print(hashigodict)

worked={}
nexts=[hashigodict[1]]
ans=0
while 0 < nexts:
    newnext=[]
    for next in nexts:
        i
    newnext=hashigodict[nexts[0]]
    next.append(hashigodict[nexts])
    hashigodict[nexts]=[]

print(ans)
#lv3
"""
"""

#lv4
"""
"""
