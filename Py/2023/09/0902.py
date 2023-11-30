#lv1
"""
n,m,p=list(map(int,input().split()))
ans=0

day=n-m
if day < 0:
    ans=0
else:
    ans+=1
    ans+=day//p

print(ans)
"""
#lv2
"""
n=int(input())
table=[]
ans=0
for i in range(100):
    table+=[list("."*100)]

for i in range(n):
    a,b,c,d=list(map(int,input().split()))
    for i in range(d-c):
        for j in range(b-a):
            table[c+i][a+j]="#"

for i in range(100):
    ans+=table[i].count("#")

print(ans)
"""
#lv3
n,d,p=list(map(int,input().split()))
f=list(map(int,input().split()))
ans=0

tickets=((n//d)+1)*p

f.sort(reverse=True)
money=0
for i in range(n):
    money+=f[i]
    if money > p:
        ans+=p
        money=0
    elif i == n-1:
        ans+=money

if ans > tickets:
    ans=tickets
print(ans)
