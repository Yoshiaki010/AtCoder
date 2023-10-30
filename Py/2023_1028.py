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
"""
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
left=0
right=0
for i in range(n):
    if a[i] < a[0]+m-0.5:
        right = i
    else:
        break
for i in range(n-right):
    if a[right+i]
    if ans < right - left:
        ans= right - left
print(left,right,ans)
#lv4
"""
"""