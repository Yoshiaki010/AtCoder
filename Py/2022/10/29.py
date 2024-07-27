#lv1
"""
n=int(input())
h=list(map(int,input().split()))
ans=0
for i in range(n):
    if h[ans] < h[i]:
        ans=i
    else:
        continue
print(ans+1)
"""

#lv2
"""
a,b,c,d,e,f=map(int,input().split())
a%=998244353
b%=998244353
c%=998244353
d%=998244353
e%=998244353
f%=998244353
abc=(a*b*c)%998244353
fed=(d*e*f)%998244353
ans=abc-fed
print(ans%998244353)
"""

#lv3
"""
"""
