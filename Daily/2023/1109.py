#lv2
"""
n=int(input())
h=list(map(int,input().split()))
now=0
ans=0
for i in range(n-1):
    i+=1
    if h[now] < h[i]:
        now+=1
    else:
        break
ans=h[now]
print(ans)
"""
#lv2
"""
n,m=map(int,input().split())
s=[]
for i in range(n):
    s.append(list(input()))
ans=0
for x in range(n):
    for y in range(n):
        if x < y:
            for j in range(m):
                if s[x][j] == "x" and s[y][j] == "x":
                    break
            else:
                ans+=1
print(ans)
"""
"""
#lv3
n=int(input())
f=[]
for _ in range(n):
    f.append(list(map(int,input().split())))
f.sort( key=lambda x: (x[0], x[1]))
ans=0
bigcup=0
bigs=0
for i in range(n):
    i+=1
    if bigs <= f[-i][1]:
        firstcup=f[-i][0]
        s=f[-i][1]
        secondcup=bigcup
        t=bigs
    else:
        firstcup=bigcup
        s=bigs
        secondcup=f[-i][0]
        t=f[-i][1]
    if firstcup != secondcup:
        manzoku=s+t
    else:
        manzoku=s+(t//2)
    if ans < manzoku:
        bigs=s
        bigcup=firstcup
        ans=manzoku
print(ans)
"""
