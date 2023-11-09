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
x=0
for y in range(n):
    if x != y:
        if aji[x][0] != aji[y][0]:
            manzoku=aji[x][1]+aji[y][1]
        else:
            manzoku=aji[x][1]+(aji[y][1]//2)
        if ans < manzoku:
            ans=manzoku
    if y == n-1:
        x+=1
print(ans)