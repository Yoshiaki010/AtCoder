"""
#lv1
n=int(input())
s=list(input())
ans=0
for i in range(n-2):
    n=s[i:i+3]
    if n == ["A","B","C"]:
        ans=i+1
        break
    else:
        continue
else:
    ans=-1
print(ans)
"""
"""
#lv2
n,m=list(map(int,input().split()))
s=list(input())
t=list(input())
ans=3
if t[0:n] == s and t[m-n::] == s:
    ans=0
elif t[0:n] == s and t[m-n::] != s:
    ans=1
elif t[0:n] != s and t[m-n::] == s:
    ans=2
else:
    ans=3
print(ans)
"""
"""
#lv3
n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
up=0
for i in range(n-1):
    i+=1
    if a[up] == i:
        print(0)
        up+=1
    else:
        print(a[up]-i)
print(0)
"""
#lv4
mino=[[],[],[]]
blackmino=0
whitemino=0
ans="Unknow"
for i in range(3):
    minop=[]
    for j in range(4):
        p=list(input())
        for k in range(4):
            if p[k] == "#":
                minop.append(1)
                if (j+k)%2 == 0:
                    blackmino+=1
                else:
                    whitemino+=1
            else:
                minop.append(0)
    mino[i].append(minop)
    print(mino[i])
if blackmino+whitemino == 16:
    minoone=mino[0]
    minotwo=mino[1]
    minothre=mino[2]
    print(minoone)
    print(minotwo)
    print(minothre)
    ans="Yes"
else:
    ans="No"
print(ans)