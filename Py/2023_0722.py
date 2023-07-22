"""
#lv1
n=int(input())
s=list(input())
abc=set()
ans=0
for i in range(n):
    if s[i] == "A":
        abc.add(s[i])
    elif s[i] == "B":
        abc.add(s[i])
    elif s[i] == "C":
        abc.add(s[i])
    if len(abc) == 3:
        ans=i+1
        break
print(ans)
"""
"""
#lv2
n,d=list(map(int,input().split()))
s=[]
ans=0
for _ in range(n):
    s+=[list(input())]
ikeruhi=0
for i in range(d):
    for j in range(n):
        if s[j][i] != "o":
            ikeruhi=0
            break
    else:
        ikeruhi+=1
    if ikeruhi > ans:
        ans=ikeruhi
print(ans)
"""
#lv3
n=int(input())
a=list(map(int,input().split()))
m=0
b=[]

for i in range(n):
    
m=len(b)
print(m)
for i in b:
    print(i,end=" ")
