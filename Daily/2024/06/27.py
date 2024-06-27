#lv2
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans="Unkow"
for i in range(m):
    if b[i] in a:
        a.remove(b[i])
    else:
        ans="No"
        break
else:
    ans="Yes"
print(ans)
"""
#lv2 
"""
n,m=map(int,input().split())
price=[]
kinounum=[]
kinouall=[]
for i in range(n):
    pcf=list(map(int,input().split()))
    price.append(pcf[0])
    kinounum.append(pcf[1])
    kinouall.append(set(pcf[2::]))

for i in range(n):
    for j in range(n):
        if i != j:
            if price[i] >= price[j]:
                if kinouall[i] - kinouall[j] == set():
                    if price[i] > price[j] or kinounum[i] < kinounum[j]:
                        ans="Yes"
                        break
    else:
        continue
    break
else:
    ans="No"
print(ans)
"""
#lv3
"""
s=list(input())
dics=dict()
for i in range(len(s)):
    if s[i] not in dics:
        dics[s[i]]=0
    else:
        continue
for i in range(len(s)):
    dics[s[i]]+=1

ans=0
liss=list(dics)
n=len(liss)
if n < 2:
    ans=1
else:
    dicsnum=list(dics)
    for i in range(n):
        for j in range(n-1-i):
            j+=i+1
            ans+=dics[liss[i]]*dics[liss[j]]
print(ans)
"""
#lv3
"""
n=int(input())

ac=[]
color=dict()
for _ in range(n):
    a,c=map(int,input().split())
    ac.append([a,c])
    if c not in color:
        color[c]=10**9
    else:
        continue

for i in range(n):
    a,c=ac[i]
    if a < color[c]:
        color[c] = a
    else:
        continue

ans=[0]
colorskey=list(color)
for i in range(len(colorskey)):
    ans.append(color[colorskey[i]])
print(max(ans))
"""
#lv4
"""
"""
