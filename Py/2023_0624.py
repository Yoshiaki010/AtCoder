"""
#lv1
n=int(input())
a=list(map(int,input().split()))
k=0
ans=0

for i in a:
    k+=1
    ans+=i
    if k==7:
        print(ans ,end=" ")
        ans=0
        k=0
"""
"""
#lv2
n=int(input())
s=[]
ans="No"

for i in range(n):
    s+=[list(input())]

for i in range(n):
    for j in range(n):
        if i!=j:
            if s[j][-1] == s[i][0]:
                t=s[i]+s[j]
                for k in range(len(t)):
                    if t[k]!=t[(len(t)+1)-(k+1)-1]:
                        break
                else:                        
                    ans="Yes"
                    break
print(ans)
"""

#lv3
ans="No"
abx=[]
for i in range(3):
    h,w=list(map(int,input().split()))
    hashc=0
    for _ in range(h):
        abx+=[[]]
        array=list(input())
        print(array)
        abx[i]+=[array]
        for j in array:
            print(j)
            if j == "#":
                hashc+=1
    abx[i]+=[hashc]

print(abx)
print(abx[0])
print(abx[1])
print(abx[2])
if max(abx[0][-1],abx[1][-1]) < abx[2][-1]:
    
    ans="Yes"

print(ans)