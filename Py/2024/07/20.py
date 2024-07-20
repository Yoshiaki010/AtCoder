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
import itertools
n,k=map(int,input().split())
s=input()
alls = itertools.permutations(s,n)
lists=[]
for nows in alls:
    lists+=[nows]

ans=set()
for nows in lists:
    print(nows)
    for i in range(n-k//2):
        lookhere=i+k-1
        print(nows[i],nows[lookhere],end=" ")
        if nows[i] == nows[lookhere]:
            lookhere-=1
            print("Much")
            break
        else:
            print("Next",lookhere)
            continue
    else:
        ans.add(nows)
    print()
        
for i in ans:
    print(i)
print(len(ans))