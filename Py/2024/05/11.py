#lv1
"""
n=int(input())
h=list(map(int,input().split()))
b=h[0]
ans=-1
for i in range(n):
    if b < h[i]:
        b=h[i]
        ans=i+1
        break
print(ans)
"""
#lv2
"""
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=k
ans=1
for i in range(n):
    if c < a[i]:
        ans+=1
        c=k-a[i]
    else:
        c-=a[i]
print(ans)
"""
#lv3
"""
n=int(input())
a=list(map(int,input().split()))
ans=0
i=0
j=1
c=(n*(n-1))//2
print(c)
for _ in range(c):
    print(a[i]+a[j],(a[i]+a[j])%10**8)
    ans+=(a[i]+a[j])%10**8
    j+=1
    if n-1 < j:
        i+=1
        j=i+1
    else:
        continue
print(ans)
"""
n=int(input())
a=list(map(int,input().split()))
c=(n*(n-1))//2
ans=0
for i in range(n):
    print(a[i]*(n),a[i]*(n)%10**8)
    ans+=(a[i]*(n)%10**8)
print((10**8)*c,ans)
ans=(10**8)*c-ans
#ans+=10**8
print(ans)
#lv4
"""
"""

