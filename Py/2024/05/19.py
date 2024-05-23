#lv4
"""
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
p=""
for i in range(n):
    p+=str(i+1)
print(p)
ans=""
for i in range(n-1):
    if p[i]+1 == p[i+1] or p[i]-1 == p[i+1]:
        ans+=str(p[i])+" "
#lv5