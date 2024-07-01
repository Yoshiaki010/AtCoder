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
import sys
sys.setrecursionlimit(400000)

n,m=map(int,input().split())
g=[]
for _ in range(n):
    g.append(list(input()))


def move(now,couse):
    x,y=now
    while g[y][x] != "#":
        now=[x,y]
        if g[y][x] == "!":
            pass
        else:
            g[y][x] = "o"
        if couse == "U":
            y-=1
        elif couse == "D":
            y+=1
        elif couse == "L":
            x-=1
        else:
            x+=1
    stop(now,couse)
    return()

def stop(now,couse):
    x,y=now
    if g[y][x] == "!":
        return ()
    else:
        g[y][x] = "!"
        if g[y-1][x] != "#" and couse != "D":
            move([x,y-1],"U")
        if g[y+1][x] != "#" and couse != "U":
            move([x,y+1],"D")
        if g[y][x-1] != "#" and couse != "R":
            move([x-1,y],"L")
        if g[y][x+1] != "#" and couse != "L":
            move([x+1,y],"R")
        return ()
    
move([1,1],"R")
print("fin")
#move([1,1],"D")

ans=0
for i in range(n):
    for j in range(m):
        if g[i][j] == "o" or g[i][j] == "!":
            ans+=1
        else:
            continue
print(ans)
"""
