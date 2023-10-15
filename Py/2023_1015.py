#lv3
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
two=n-m
one=m-two

for i in range(two):
    ans+=(a[i]+a[two*2-1-i])**2
for i in range(one):
    ans+=a[(two*2)+i]**2

print(ans)