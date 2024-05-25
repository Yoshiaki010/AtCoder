#lv1
"""
a,b=map(int,input().split())
h=[0,0,0]
h[a-1]=1
h[b-1]=1
c=0
ans=-1
for i in range(3):
    if h[i] == 1:
        continue
    else:
        c+=1
        ans=i+1
if c == 2:
    ans=-1
else:
    pass
print(ans)
""" 
#lv2
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans="No"
a.sort()
for i in range(n-1):
    if a[i]+1 == a[i+1]:
        ans="Yes"
        break
    else:
        ans="No"
print(ans)
"""
"""
b=list(map(int,input().split()))
dica={}
for i in range(n):
    dica[a[i]] = []
for i in range(n-1):
    dica[a[i]] += [a[i+1]]
    dica[a[i+1]] += [a[i]]
c=a+b
c.sort()
for i in range(n+m-1):
    if c[i] in a:
        if c[i+1] in dica[c[i]]:
            ans="Yes"
            break
        else:
            continue
    else:
        continue
else:
    ans="No"
"""
#lv3
"""
"""
n,t=map(int,input().split())
a=list(map(int,input().split()))
c=[0]*(n*n)
ans=0
for i in range(t):
    c[a[i]-1]=1
    for j in range(3):
        tate=c[j::n]
        yoko=c[j*n:j*n+n]
        if set(tate) == {1} or set(yoko) == {1}:
            ans=i+1
    nanamex=c[0::n+1]
    nanamey=c[n-1:(n-1)*n+1:n-1]
    if set(nanamex) == {1} or set(nanamey) == {1}:
        ans=i+1
    if ans != 0:
        break
    else:
        continue
else:
    ans=-1
print(ans)
"""
"""    

#lv4
"""
"""
