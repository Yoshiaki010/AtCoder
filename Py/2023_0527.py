'''
#lev1
n=int(input())
s=list(input())
t=list(input())
ans="No"
fans="No"
for i in range(n):
    if s[i]=="l":
        if t[i]=="1":
            ans="Yes"
    elif s[i]=="1":
        if t[i]=="l":
            ans="Yes"
    elif s[i]=="o":
        if t[i]=="0":
            ans="Yes"
    elif s[i]=="0":
        if t[i]=="o":
            ans="Yes"
    elif s[i]==t[i]:
        ans="Yes"
    else:
        fans="Yes"

if fans == "No":
    print(ans)
else:
    print("No")
'''
'''
#lev2
n,m= map(int,input().split())
all= {} 
ans=0
for i in range(n):
    all[i]=set()
for _ in range(m):
    for i in [list(map(int,input().split()))]:
        for j in range(n-1):
            all[i[j]-1].add(i[j+1]-1)
            all[i[j+1]-1].add(i[j]-1)

print(all)
for i in range(n):
    ans+=n-len(all[i])-1
print(ans//2)
'''
