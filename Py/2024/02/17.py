#lv1
"""
n=int(input())
ans="10"*n+"1"
print(ans)
"""
#lv2
"""
n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    s,t=map(int,input().split())
    if s <= a[i]:
        a[i+1]+=t*(a[i]//s)
        a[i]%=s
    else:
        continue
print(a[n-1])
"""
#lv3
h,w,n=map(int,input().split())
t=input()
s=[]
for i in range(h):
    s.append(list(input()))
for i in range(h):
    print(s[i])