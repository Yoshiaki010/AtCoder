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
ans=[]
left=[]
right=[n-1]
for i in range(n):
    i+=1
    if a[-i] == a[right[-1]]:
        continue
    else:
        if a[0]-1.5+m < a[-i]:
            right.append(n-i)
right.sort()
j=0
for i in range(n):
    if j < len(right):
        if a[right[j]]+0.5-m <= a[i]:
            left.append(i)
            j+=1
        else:
            continue
for i in range(len(right)):
    ans.append(right[i]-left[i]+1) 
print(max(ans))
#lv4
"""
"""