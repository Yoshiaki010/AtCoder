#lv1
"""
n=int(input())
ans="L"+"o"*n+"ng"
print(ans)
"""
#lv2
"""
n=int(input())
ans=-1
if n % 2 != 0:
    ans=0
elif n == 0:
    ans=1
else:
    ans=0
    while n % 2 == 0:
        n//=2
        ans+=1
print(ans)
"""
#lv3
"""
"""
n=int(input())
g=[0,2,4,6,8]
ans=[]
k=n//5
while n > 4:
    n/=5

print(k)
