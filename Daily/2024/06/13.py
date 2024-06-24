#C lv2
"""
n=int(input())
ans=[]
c=0
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if n < x+y+z:
                continue
            else:
                ans.append(str(x)+" "+str(y)+" "+str(z))
                c+=1
for i in range(c):
    print(ans[i])
"""
#D lv2
"""
import math
n=int(input())

t=[]
for i in range(n):
    x,y=map(int,input().split())
    t.append([x,y])

ans=0
for i in range(n):
    for j in range(n):
        now =math.sqrt(abs((t[i][0]-t[j][0]))**2+abs(t[i][1]-t[j][1])**2)
        if ans < now:
            ans=now
        else:
            continue
print(ans)
"""
#E lv3 
"""
n,k=map(int,input().split())
s=[]
for _ in range(n):
    s.append(sum(map(int,input().split())))
rank=sorted(s)
for i in range(n):
    if rank[-k] <= s[i]+300:
        print("Yes")
    else:
        print("No")
"""
#F lv3 
"""
n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
ans=[0]*n

now=t[0]
for _ in range(2):
    for i in range(n):
        if t[i] < now:
            now=t[i]
        ans[i]=now
        now+=s[i]
for i in range(n):
    print(ans[i])
"""
#別解
"""
n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
mintime=max(t)
mingeter=0
t=t+t
s=s+s
for i in range(n):
    if t[i] < mintime:
        mintime = t[i]
        mingeter = i
    else:
        continue

ans=[0]*n
for i in range(n):
    if t[mingeter+i] < mintime:
        mintime=t[mingeter+i]
    ans[(mingeter+i)%n] = mintime
    mintime+=s[mingeter+i]

for i in range(n):
    print(ans[i])
"""
#G lv4
"""
"""
n,m=map(int,input().split())
g=[]
for _ in range(n):
    g.append(list(input()))

def move(now,couse):
    y,x=now
    g[y][x] = "o"
    if couse == "U":
        y-=1
    elif couse == "D":
        y+=1
    elif couse == "L":
        x-=1
    else:
        x+=1
    if g[y][x] == "#":
        stop(now)
    else:
        move([y,x],couse)
    return ()

stopplace=[]
def stop(now):
    if now in stopplace:
        return ()
    else:
        stopplace.append(now)
        y,x=now
        if g[y-1][x] != "#":
            move([y-1,x],"U")
        if g[y+1][x] != "#":
            move([y+1,x],"D")
        if g[y][x-1] != "#":
            move([y,x-1],"L")
        if g[y][x+1] != "#":
            move([y,x+1],"R")
        return ()
    
move([1,1],"R")
move([1,1],"D")

ans=0
for i in range(n):
    for j in range(m):
        if g[i][j] == "o":
            ans+=1
        else:
            continue
print(ans)