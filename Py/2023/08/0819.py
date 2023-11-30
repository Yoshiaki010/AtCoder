"""
#lv1
s=list(input())
nos=list("aiueo")
ans=""

for i in s:
    if i not in nos:
        print(i,end="")
"""
"""
#lv2
m=int(input())
d=list(map(int,input().split()))
a=0
b=0
middled=(sum(d)+1)//2
for i in range(m):
    if  middled > d[i]:
        middled-=d[i]
    else:
        a=i+1
        b=middled
        break
print(a,b)
"""
#lv3
"""
"""
n=int(input())
ff,s=list(map(int,input().split()))
f=set()
f.add(ff)
ans=0
maxother=0
maxsame=0


for _ in range(n-1):
    print(f,s)
    print(maxsame,maxother)

    nf,t=list(map(int,input().split()))
    other = s+t
    if s >= t:
        same = s+(t//2)
    else:
        same = t+(s//2)

    if len(f) >= 2:
        if nf in f:
            f.remove(nf)

    if nf not in f:
        if maxother < other:
            f=set()
            f.add(nf)
            s = t
            maxsame = other
        elif maxsame == other:
            f.add(nf)
        else:
            continue
    else:
        if  maxsame < same:
            maxsame = same
            s = t
        elif maxsame == same:
            f.add(nf)
        else:
            continue

print(f,s)

if maxother > maxsame:
    ans=maxother
else:
    ans=maxsame
print(ans)
