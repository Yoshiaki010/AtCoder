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
#lv3
n=int(input())
aji=[]
for _ in range(n):
    aji.append(list(map(int,input().split())))
ans=0
bigcup=aji[0][0]
bigs=aji[0][1]
for i in range(n-1):
    i+=1
    if bigs <= aji[i][1]:
        s=aji[i][1]
        t=bigs
        cup=bigcup
        bigs=s
        bigcup=aji[i][0]
    else:
        s=bigs
        t=aji[i][1]
        cup=aji[i][0]
    if bigcup != cup:
        manzoku=s+t
    else:
        manzoku=s+(t//2)
    if ans < manzoku:
        ans=manzoku
print(ans)