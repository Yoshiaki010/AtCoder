#lv1
"""
n=int(input())
ans="Unknow"
s=input()
for i in range(n-2):
    next=input()
    if s == "sweet" and s == next:
        ans="No"
        break
    else:
        s=next
else:
    ans="Yes"
print(ans)
"""

#lv2
"""
h,w=map(int,input().split())
gridy,gridx=map(int,input().split())
grid=[["*"]*(w+2)]

for i in range(h):
    grid.append(["*"]+list(input())+["*"])
grid+=[["*"]*(w+2)]

x=input()

next=[gridx,gridy]
for i in range(len(x)):
    gridx,gridy=next
    if x[i] == "U":
        gridy-=1
    elif x[i] == "D":
        gridy+=1
    elif x[i] == "R":
        gridx+=1
    else:
        gridx-=1
    if grid[gridy][gridx] == ".":
        next=[gridx,gridy]
    else:
        pass

print(next[1],next[0])
"""
#lv3 
"""
n,x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

ansa=0
suger=0
for i in range(n):
    ansa+=1
    suger+=a[i]
    if x < suger:
        break
    else:
        continue

ansb=0
solt=0
for i in range(n):
    ansb+=1
    solt+=b[i]
    if y < solt:
        break
    else:
        continue
if ansa < ansb:
    ans=ansa
else:
    ans=ansb

print(ans)
"""
#lv4
"""
n,q=map(int,input().split())
a=list(map(int,input().split()))
all=[]
bk=[]
for i in range(n):
    all.append(["a",a[i]])

for _ in range(q):
    b,k=map(int,input().split())
    bk.append([b,k])
    all.append(["b",b,k])

a.sort()
bk.sort()
sortall=sorted(all,key=lambda x:x[1])
print(a)
print(bk)
print(all)
print(sortall)
"""
