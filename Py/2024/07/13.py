#lv1
"""
color=list(map(int,input().split()))
c=input()
if c == "Red":
    color.pop(0)
elif c == "Green":
    color.pop(1)
else:
    color.pop(2)
ans=min(color)
print(ans)
"""
#lv2
"""
n=3
all=[]
for i in range(n):
    abc=list(map(int,input().split()))
    all.append(abc)

all+=all

long=[]
for i in range(n):
    x1,y1=all[i]
    x2,y2=all[i+1]
    long.append(abs(x2-x1)**2+abs((y2-y1))**2)

long+=long

ans="Unknow"
for i in range(n):
    if long[i]+long[i+1] == long[i+2]:
        ans="Yes"
        break
    else:
        continue
else:
    ans="No"

print(ans)
"""

#lv3
"""
n=int(input())

LR=[]
diff=0
sumL=0
x=[]
for _ in range(n):
    l,r=map(int,input().split())
    LR.append([l,r])
    diff+=r-l
    sumL+=l
    x.append(l)

ans="Unknow"
if sumL == 0:
    ans="Yes"
else:
    sumL=abs(sumL)
    if sumL < diff:
        ans="Yes"
        for i in range(n):
            if sumL < LR[i][1]-LR[i][0]:
                x[i]+=sumL
                sumL=0
            else:
                x[i]=LR[i][1]
                sumL-=LR[i][1]-LR[i][0]
    else:
        ans="No"

print(ans)
if ans == "Yes":
    for i in range(n):
        print(x[i],end=" ")
else:
    pass
"""

#lv4
"""
"""
