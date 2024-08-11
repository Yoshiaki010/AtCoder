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
"""
n=int(input())
alls=[]
allm=[]
for _ in range(n):
    s=input()
    alls.append(s)
    allm.append(len(list(s)))
alls.append(alls[0])

t=[]
m=max(allm)
for i in range(m):
    t.append("")

print(alls,allm)

for i in range(n):
    si=allm[i]
    for j in range(m):
        if -1 < j and j < si:
            t[j]+=alls[i][j]
        else:
            if si-1 < j and j < m:
                t[j]+="*"
            else:
                break

for i in range(m):
    print(t[i])

#lv3 
"""
    print("Q:",x)
    print("bag:",bag)
q=int(input())
bag=dict()
bagnum=0
for _ in range(q):
    x=input().split()
    if x[0] == "1":
        if x[1] not in bag:
            bag[x[1]]=1
            bagnum+=1
        else:
            bag[x[1]]+=1
    elif x[0] == "2":
        bag[x[1]]-=1
        if bag[x[1]]==0:
            bagnum-=1
        else:
            pass
    else:
        print(bagnum)
"""
