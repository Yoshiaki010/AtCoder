#lv1
"""
s,t=input().split()
ans="Unkow"
if s == "AtCoder" and t == "Land":
    ans="Yes"
else:
    ans="No"
print(ans)
"""
#lv2
"""
n,a=map(int,input().split())
t=list(map(int,input().split()))
time=0
for i in range(n):
    if time < t[i]:
        time=t[i]
    time+=a
    print(time)
"""
#lv3
"""
"""
n,m=map(int,input().split())
s=[]
for i in range(n):
    s.append(list(input()))

ans=0
for i in range(n-1):
    ans=1
    memo=s[i]
    for j in range(n-(i+1)):
        ans+=1
        now=s[i]
        j=j+i+1
        print("defult:",s[i],s[j])
        for q in range(m):
            if now[q] == "x" and s[j][q] == "o":
                now[q] = "o"
            else:
                continue
        now+=str(j)
        print("specal:",now)

#print(ans)