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

###input
n=[int(input())]
count=1
ans=0
ndic=dict()
ndic[n]=1

while count >= 1:
    new=[]
    for i in range(count):
        x=n[i]
        count-=1
        ans+=x*ndic[x]
        a=x//2
        ndic[a]=ndic[x]*2
        count+=1
        n.append(a)
        if x[0]%2 != 0:
            ndic[a+1]=ndic[x]*2
            n.append(a+1)
            count+=1
        else:
            count+=1
    n=new
print(ans)