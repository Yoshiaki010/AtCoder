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

for i in range(h):
    array=list(input())
    s+=[array]
    if array.count("#") < nocookie and array.count("#") >=1:
        nocookie=s.count("#")
        nocookieh=i
ans=0,0
for _ in range(h):
    s+=[list(input())]

print(h,w)
print(s)
print(nocookieh)
print(nocookie)

for i in s[nocookieh]:
    if s[i]!=s[i+1]:
        for j in s[i]:
            print(j)
for i in range(h-1):
    print(i)
    for j in range(w-1):
        print(s[i+1][j])
        if s[i+1][j]=="#":
            if s[i][j]==".":    
                print(s[i][j])
                ans=i,j
print(ans)
