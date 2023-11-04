#lv1
"""
x,y=map(int,input().split())
ans="No"
if x > y:
    if x - y <= 3:
        ans="Yes"
else:
    if y - x <= 2:
        ans="Yes"
print(ans)
"""
#lv2
"""
n=input()
inn=int(n)
for _ in range(920-inn):
    lisn=list(map(int,n))
    if lisn[0]*lisn[1] == lisn[2]:
        ans=inn
        break
    inn+=1
    n=str(inn)

print(ans)
"""
    
#lv3
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
right=0
left=0
prezent=0

while right <= n-1:
    if a[right] < a[left]-0.5+m:
        prezent+=1
        right+=1
    else:
      left+=1
    if ans < right - left:
        ans=right - left
else:
    if ans < right - left:
        ans=right - left
print(ans)
"""
#lv4
"""
"""