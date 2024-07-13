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
abc=[]
for _ in range(3):
    abc.append(list(map(int,input().split())))

abc.sort()

ax,ay=abc[0]
bx,by=abc[1]
cx,cy=abc[2]

long=[]
long.append(abs((bx-ax))**2+abs((by-ay))**2)
long.append(abs((cx-ax))**2+abs((cy-ay))**2)
long.append(abs((cx-bx))**2+abs((cy-by))**2)

ans="Unknow"
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and i != k:
                if long[i] + long[j] == long[k]:
                    ans="Yes"
                    break
                else:
                    continue
            else:
                continue
        else:
            continue
        break
    else:
        continue
    break
else:
    ans="No"
print(ans)
"""
#lv3
"""
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
#lv4
"""
"""
