"""
#lv1
n=int(input())
w=n%5
ans=0

if w==0:
    ans=n
elif w>=3:
    s=5-w
    ans=n+s
elif w<=2:
    ans=n-w

print(ans)

#lv2
point=[3,1,4,1,5,9]
ans=0
p=[ord(i)-65 for i in input().split()]

p.sort()

for i in point[p[0]:p[1]]:
    ans+=i

print(ans)
"""
#lv3
h,w=map(int,input().split())
s=[]
sets=set()
nocookieh=0
nocookie=501
x=1
ans=0,0


for i in range(h):
    array=list(input())
    s+=[array]
    if array.count("#") < nocookie and array.count("#") >=1:
        nocookie=array.count("#")
        nocookieh=i

for i in range(w):
    if h-1:
        x=-1
    if s[nocookieh][i] == "." and s[nocookieh+x][i]=="#":
       ans=nocookieh+1,i+1

print(ans)