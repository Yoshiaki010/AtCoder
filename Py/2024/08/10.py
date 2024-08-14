#lv1
"""
n,t,a=map(int,input().split())
diff=abs(t-a)
vote=n-(t+a)
ans="Unknow"
if vote < diff:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
#lv2
"""
n=int(input())
alls=[]
allm=[]
for _ in range(n):
    s=input()
    alls.append(s)
    allm.append(len(list(s)))
allm.append(allm[0])

t=[]
m=max(allm)
for i in range(m):
    t.append("")

for i in range(n):
    for j in range(m):
        if -1 < j and j < allm[i]:
            t[j]=alls[i][j]+t[j]
        else:
            if j < allm[i-1]:
                t[j]="*"+t[j]
                allm[i]+=1
            else:
                break

for i in range(m):
    print(t[i])
"""

#lv3 
"""
q=int(input())
balls=dict()
ballkindnum=0
for _ in range(q):
    x=input().split()
    if x[0] == "1":
        if x[1] not in balls:
            balls[x[1]]=1
        else:
            balls[x[1]]+=1
        if balls[x[1]] == 1:
            ballkindnum+=1
    elif x[0] == "2":
        balls[x[1]]-=1
        if balls[x[1]]==0:
            ballkindnum-=1
        else:
            pass
    else:
        print(ballkindnum)
"""