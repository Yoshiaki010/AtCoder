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
"""
n=int(input())
num=set()
data=[]
for i in range(n):
    a,b=map(int,input().split())
    data.append([a,b])
    num.add(a)
    num.add(b)

numlist=list(num)

hashigo=dict()
hashigo[1]=[]
for i in range(len(numlist)):
    hashigo[numlist[i]]=[]

for i in range(n):
    a,b=data[i]
    hashigo[a].append(b)
    hashigo[b].append(a)

allnexts=[]
nexts=[1]
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
#lv3
"""
"""

#lv4
"""
"""
