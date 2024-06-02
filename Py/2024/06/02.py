#lv3
n,k=map(int,input().split())
a=list(map(int,input().split())) 
all=0
x=sorted(a)
for i in range(n):
    all+=x[i]
ans="Unknow"
ansa=[]
now=0
for _ in range(n):
    if x[0]+now < k:
        now+=x[-1]
        ansa.append(x[-1])
        x.pop(-1)
    else:
        now+=x[0]
        ansa.append(x[0])
        x.pop(0)
y=[0]
for i in range(n):
    y.append(y[i]+ansa[i])
c=0
now="small"
for i in range(n+1):
    if y[i] < k and now == "big":
        ans="No"
        break
    else:
        if k <= y[i] and now == "small":
            now="big"
        else:
            continue
else:
    ans="Yes"
        
print(ans)
if ans == "Yes":
    for i in range(n):
        print(ansa[i],end=" ")
else:
    pass