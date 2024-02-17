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

#input
n=[int(input())]
count=1
ans=0
ndic=dict()
ndic[n[0]]=1

while count >= 1:
    new=[]
    for i in range(count):
        print(n)
        x=n[i]
        count-=1
        ans+=x*ndic[x]
        a=x//2
        if x%2 == 0:
            if a >= 2:
                ndic[a]=ndic[x]*2
                new.append(a)
                count+=1
        else:
            if a >= 2:
                ndic[a+1]+=ndic[x]*2
                ndic[a]+=ndic[x]*2
                new.append(a+1)
                new.append(a)
                count+=2
            else:
                continue
    n=new
print(ans)