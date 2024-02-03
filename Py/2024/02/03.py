#lv1
"""
s=input()
c=len(s)
for i in range(c):
    if s[c-i-1] == ".":
        ans=s[c-i::]
        break
print(ans)
"""
#lv2
"""
"""
h,w,n=map(int,input().split())
t=[]
for i in range(h):
    t.append(["."]*w)
x=0
y=0
r=0

for _ in range(n):
    #paint color & rotation
    if t[y][x] == ".":
        t[y][x] = "#"
        if r == 270:
            r=0
        else:
            r+=90
    else:
        t[y][x] = "."
        if r == 0:
            r=270
        else:
            r-=90
    #move
    if r == 0:
        y-=1
    elif r == 90:
        x+=1
    elif r == 180:
        y+=1
    elif r == 270:
        x-=1
    #out of range
    if w <= x:
        x=0
    elif x < 0:
        x=w-1
    if h <= y:
        y=0
    elif y < 0:
        y=h-1
#ans
for i in range(h):
    for j in range(w):
        print(t[i][j],end="")
    print()