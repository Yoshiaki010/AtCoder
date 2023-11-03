#lv2
"""
n=int(input())
s=[]
t=[]
ans="No"
for i in range(n):  
    last,name=input().split()
    s.append(last)
    t.append(name)

for i in range(n):
    for j in range(n):
        if i != j:
            if s[i] == s[j] and t[i] == t[j]:
                ans="Yes"
                break
    if ans!="No":
        break
print(ans)
"""
#lv2
"""
n=int(input())
array=[]
ans=1

for i in range(n):
    array.append(input().split())

array.sort()

for i in range(n-1):
    if array[i] != array[i+1]:
        ans+=1

print(ans)
"""
#lv3
"""
"""
def number(n,m,lisa):
    lisa.append()
    number(n,m,lisa)
    
    
n,m=map(int,input().split())