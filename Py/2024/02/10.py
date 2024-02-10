#lv1
"""
a,b,d=map(int,input().split())
print(a,end=" ")
r=(b-a)//d
ans=a
for _ in range(r):
    ans+=d
    if a <= b:
        print(ans,end=" ")
    else:
        break
"""
#lv2
"""
q=int(input())
a=[]
counta=0
for _ in range(q):
    num,xk=map(int,input().split())
    if num == 1:
        counta+=1
        a.append(xk)
    else:
        print(a[counta-xk])
"""
#lv3
n=int(input())
ndic=dict()
ndic[n]=1
count=1
ans=0
how=0
while count >= 1:
    new=[]
    how+=1
    for i in range(count):
        if n[i][0] >= 2:
            x=n[i]
        else:
            continue
        ans+=x[0]*x[1]
        count-=1
        da=[x[0]//2,x[1]*2]
        if x[0]%2 != 0:
            ua=[x[0]//2+1,x[1]*2]
        else:
            ua=[1]
        lisa=[da,ua]
        for i in range(2):
            a=lisa[i]
            if a[0] >= 2:
                new.append(a)
                count+=1
    n=new
    print(n)
print(how)
print(ans)