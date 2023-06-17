"""
#lv1
n=input()
s=list(input())
for i in s:
    print(i*2,end="")
"""
"""
#lv2
a=list(map(int,input().split()))
ans=0
for i in range(64):
    ans+=a[i]*(2**i)
print(ans)
"""
"""
#lv3
n=int(input())
a=list(map(int,input().split()))
alist=[]
ans=[]

for i in range(n):
    alist+=[[i+1]]

for i in range(n*3):
    alist[a[i]-1]+=[i+1]


ans= sorted(alist, key=lambda x:(x[2]))

for i in range(n):
    print(ans[i][0],end=" ")
"""
#lv4
n=int(input())
takahasi=[[0,0]]
ans=0

for _ in range(n):
    i=list(map(int,input().split()))
    if i[0]==takahasi[-1][0]:
        takahasi[-1]+=[i[1]]
    else:
        takahasi[-1]=max(takahasi[-1][1::])
        takahasi+=[i]
else:
    takahasi[-1]=max(takahasi[-1][1::])

for i in range(len(takahasi)):
    if ans + takahasi[i] > -1:
        ans+=takahasi[i]
    else:
        break

print(ans)