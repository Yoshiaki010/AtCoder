"""
#lv1
s=list(input())
for i in s:
    print(i,end=" ")
"""
"""
#lv2
n=int(input())
a=list(map(int,input().split()))
maxa=max(a)
ans=0
for i in a:
    if i < maxa:
        if ans <= i:
            ans=i
print(ans)
"""
"""
#lv3
n=int(input())
s=list(input())
kugiris=[[s[0]]]
ns=0
for i in range(n-1):
    if s[i+1] in kugiris[ns]:
        kugiris[ns].append(s[i+1])
    else:
        ns+=1
        kugiris.append([s[i+1]])

kugiris.sort()
anss=[kugiris[-1]]
for i in range(len(kugiris)-1):
    i+=2
    if anss[-1][0] == kugiris[-i][0]:
        if len(anss[-1]) < len(kugiris[-i]):
            anss.remove(anss[-1])
            anss.append(kugiris[-i])
    else:
        anss.append(kugiris[-i])

ans=0
for i in range(len(anss)):
    ans+=len(anss[i])
print(ans)
"""
"""
#lv4
n,m=map(int,input().split())
p=[]
for i in range(n):
    p.append(0)
ans=1
a=list(map(int,input().split()))
for i in range(m):
    p[a[i]-1]+=1
    if p[ans-1] < p[a[i]-1]:
        ans=a[i]
    elif p[ans-1] == p[a[i]-1]:
        if a[i] < ans:
            ans=a[i]
    print(ans)
"""
#lv5
n,m=map(int,input().split())
s=list(input())
t=list(input())
x=[]

nolast=t[0:m-1]

print(n,m)
print(s)
print(t)
print(nolast)
ans="Yes"
for i in range(n):
    i+=1
    
print(ans)