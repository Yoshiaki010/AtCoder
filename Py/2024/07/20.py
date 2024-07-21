#lv1
"""
r=int(input())
upline=[100,200,300]

ans=0
if 199 <= r:
    ans=upline[2]-r
elif 99 < r:
    ans=upline[1]-r
else:
    ans=upline[0]-r
print(ans)
"""
#lv2
"""
n,t,p=map(int,input().split())
long=list(map(int,input().split()))
diff=[]
clearp=0

for i in range(n):
    if t <= long[i]:
        diff.append(0)
    else:
        diff.append(t-long[i])

diff.sort()

ans=diff[p-1]
print(ans)
"""
#lv3
"""
"""
import itertools
n,k=map(int,input().split())
s=input()
alls = itertools.permutations(s,n)
sets=set()
for nows in alls:
    sets.add(nows)

ans=set()
for nows in sets:
    print(nows)
    j=0
    for i in range(n-k+1):
        print(i,nows[i+j],nows[i+k-(j*1)-1],end="/")
        if nows[i+j] == nows[i+k-(j*1)-1]:
            j+=1
            print("Much +j")
        else:
            print("Reset j")
            j=0
        print("||")
        if j == k-1:
            print(j,k-1,"All much")
            break
        else:
            print(j,k-1,"Not all")
    else:
        print("This Nomuch +1")
        ans.add(nows)
    print()
    print("Next")
    continue
        
print(len(ans))
