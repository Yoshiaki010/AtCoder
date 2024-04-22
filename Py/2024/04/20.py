#lv1
"""
s=input()
t=int(s[3::])
ans="Unknow"
if 0 < t and t < 350 and t != 316:
  ans="Yes"
else:
    ans = "No"
print(ans)
"""
#lv2
"""
n,q=map(int,input().split())
t=list(map(int,input().split()))
status=[1]*n
ans=n
for i in range(q):
    if status[t[i]-1] == 1:
        ans-=1
        status[t[i]-1] = 0
    else:
        ans+=1
        status[t[i]-1] = 1
print(ans)
"""
n=int(input())
a=list(map(int,input().split()))
k=0
eru=[]
for i in range(n-1):
    if i+1 != a[i]:
        k+=1
        eru.append(i+1)
    else:
        continue

k//=2
if k%2 != 0:
    eru.append(n)
    k+=1
else:
print(k,eru)
for i in range(k):
    print(eru[i*2],eru[(i+1)*2])