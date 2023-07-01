"""
#lv1
s=list(map(int,input().split()))
ans="No"

for i in range(len(s)-1):
    if s[i] > s[i+1]:
        break
    elif  s[i] < 100 or  675 < s[i]:
        break
    elif s[i] %25 !=0:
        break
else:
    ans="Yes"

print(ans)
"""
"""
#lv2
n,m=list(map(int,input().split()))
c=input().split()
color=["other"]
color+=list(input().split())
colormuch=list(map(int,input().split()))
ans=0

colordict={}

for i in range(m+1):
    colordict[color[i]] = colormuch[i]

for i in c:
    if i in colordict:
        ans+=colordict[i]
    else:
        ans+=colordict["other"]
print(ans)
"""
#lv3
n=int(input())
anslis=[]

for i in range(n):
    a,b=list(map(int,input().split()))
    p=a/(a+b)
    anslis+=[[i+1,p]]

anslis.sort(key=lambda x: x[1],reverse=True)

for i in anslis:
    print(i[0],end=" ")
