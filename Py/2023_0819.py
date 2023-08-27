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
f,s=list(map(int,input().split()))
maxf=set()
maxf.add(f)
ans=0
maxother=0
maxsame=0

for _ in range(n-1):
    nf,t=list(map(int,input().split()))
    other=s+t
    if t > s:
        same=t+(s//2)
    else:
        same=s+(t//2)
    if nf not in maxf:
        if maxother < other:
            maxother=other
            if t > s:
                maxf=[]
                maxf+= [nf]
                s = t
            elif t == s:
                maxf+= [nf]

    else:
        if  maxsame < same:
            maxsame=same
            if t > s:
                maxf=[]
                maxf+= [nf]
                s = t
            elif t == s:
                maxf+= [nf]

if maxother > maxsame:
    ans=maxother
else:
    ans=maxsame
print(ans)
