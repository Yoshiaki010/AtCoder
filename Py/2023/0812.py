"""
#lv1
per=list("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
n=int(input())
for  i in range(n+2):
    print(per[i],end="")
"""
"""
#lv2
n=int(input())
a=[]
cans=[]
hit=[]
ans=[]

for _ in range(n):
    c=[int(input())]
    a+=[list(map(int,input().split()))]
x=int(input())

for i in range(n):
    if x in a[i]:
        hit+=[i+1]
        cans+=[len(a[i])]

if len(hit) > 0:
    minc=min(cans)

for i in range(len(hit)):
    if minc >= cans[i]:
        ans+=[hit[i]]

print(len(ans))
for i in ans:
    print(i,end=" ")
"""
"""
"""
#lv3
n,m=list(map(int,input().split()))
s=list(input())
c=list(map(int,input().split()))
front=[]
back=[]
changestr=0
changenum=0

for i in range(m):
    if c.count(i+1) > 1:
        changestr+=1
        front.append("F")
        back.append("B")

revs=s[::-1]
revc=c[::-1]

for i in range(n):
    if c.count(revc[i]) > 1:
        if back[revc[i]-1] == "B":
            back[revc[i]-1]=revs[i]
            changenum+=1
        if changenum == changestr:
            break

for i in range(n):
    if c.count(c[i]) > 1:
        front[c[i]-1]=s[i]
        s[i]=back[c[i]-1]
        back[c[i]-1]=front[c[i]-1]

for i in s:
    print(i,end="")
