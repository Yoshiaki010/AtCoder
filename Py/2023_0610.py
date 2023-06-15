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
ans=[]
cookieh=0
cookiew=0

cookies=0
for i in range(h):
    a=list(input())
    s+=[a]
    nowcookies=0
    for j in range(len(a)):
        if a[j]=="#":
            nowcookies+=1
    if nowcookies >=1:
        if nowcookies - cookies == 1:
            cookieh=i-1
        elif nowcookies - cookies == -1:
            cookieh=i
        cookies=nowcookies

cookies=0
for i in range(w):
    nowcookies=0
    for j in range(h):
        if s[j][i]=="#":
            nowcookies+=1
    if nowcookies >=1:
        if nowcookies - cookies == 1:
            cookiew=i-1
        elif nowcookies - cookies == -1:
            cookiew=i
        cookies=nowcookies

ans+=cookieh+1,cookiew+1
print(ans[0],ans[1])
"""
h,w=map(int,input().split())
s=[]
sets=set()
nocookieh=0
nocookie=501
x=1
ans=[]

for i in range(h):
    array=list(input())
    s+=[array]
    if array.count("#") < nocookie and array.count("#") >=1:
        nocookie=array.count("#")
        nocookieh=i

for i in range(w):
    if nocookieh >= w-1:
        x=-1
    if s[nocookieh][i] == "." and s[nocookieh+x][i]=="#":
       ans+=[nocookieh+1,i+1]

print(ans[0],ans[1])
"""