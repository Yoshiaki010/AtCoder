#lv2
"""
s=input()
t="oxx"*7
n=len(s)
ans="Unknow"
for i in range(9):
    if t[i:i+n] == s:
        ans="Yes"
        break
else:
    ans="No"
print(ans)
"""
#lv2
"""
h,w,n=map(int,input().split())
trace=[]

for i in range(h):
    trace.append(["."]*w)

now=[0,0]
couse="U"
for i in range(n):
    y,x=now
    if trace[y][x] == ".":
        trace[y][x] = "#"
        if couse == "U":
            couse="R"
            x+=1
        elif couse == "R":
            couse="D"
            y+=1
        elif couse == "D":
            couse="L"
            x-=1
        else:
            couse="U"
            y-=1
    else:
        trace[y][x] = "."
        if couse == "U":
            couse="L"
            x-=1
        elif couse == "L":
            couse="D"
            y+=1
        elif couse == "D":
            couse="R"
            x+=1
        else:
            couse="U"
            y-=1
    if x < 0:
        x=w-1
    elif w-1 < x:
        x=0
    if y < 0:
        y=h-1
    elif h-1 < y:
        y=0
    now=y,x

for i in range(h):
    for j in range(w):
        print(trace[i][j],end="")
    print()
"""
#lv3
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
f=[0]
for i in range(n):
    f.append(f[i]+a[i])

max=0
for i in range(m):
    max+=a[i]*(i+1)

ans=max
for i in range(n-m):
    max-=f[i+m]-f[i]
    max+=a[i+m]*m
    if ans < max:
        ans=max
print(ans)
"""
#lv3
"""
n=int(input())
a=list(map(int,input().split()))
anum=[]
for i in range(n*3):
    anum.append([a[i],i])

anum.sort()
mida=anum[1::3]
ans=sorted(mida,key=lambda x: x[1])

for i in range(n):
    print(ans[i][0],end=" ")
"""
#lv4
"""
"""
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

diff=[]
for i in range(n):
    diff.append(b[i]-a[i]+1)
print(diff)
ans=1
for i in range(n):
    ans*=diff[i]
ans%=998244353
print(ans)