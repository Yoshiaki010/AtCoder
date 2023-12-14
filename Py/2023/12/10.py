"""
#lv1
n,s,k=map(int,input().split())
ans=0
for i in range(n):
    p,q=map(int,input().split())
    ans+=p*q
if s <= ans:
    ans+=0
else:
    ans+=k
print(ans)
"""
"""
#lv2
k,g,m=map(int,input().split())
ansg,ansm=0,0
for _ in range(k):
    if ansg == g:
        ansg=0
    elif ansm == 0:
        ansm=m
    else:
        if g-ansg < ansm:
            ansm-=g-ansg
            ansg=g
        else:
            ansg=ansm
            ansm=0
print(ansg,ansm)
"""
"""
#lv3
n,m=map(int,input().split())
s=list(input())
gt=0
stock=[m,0]
for i in range(n):
    if s[i] == "0":
        stock=[m,gt]
    elif s[i] == "1":
        if 0 < stock[0]:
            stock[0]-=1
        elif 0 < stock[1]:
            stock[1]-=1
        else:
            gt+=1
    else:
        if 0 < stock[1]:
            stock[1]-=1
        else:
            gt+=1
print(gt)
"""
#lv4
h,w=map(int,input().split())
ah=[]
bh=[]
aw=[]
bw=[]
gridseta=[]
ans=0

for i in range(h):
    a=list(map(int,input().split()))
    if i == 0:
        aw+=a
    ah.append(a[0])
    gridseta.append(set(a))
    

for i in range(h):
    b=list(map(int,input().split()))
    if i == 0:
        bw+=b
    bh.append(b[0])
    setb=set(b)
    for i in range(h):
        print(setb,gridseta[i])
        if setb in gridseta[i]:
            break
        else:
            continue
    else:
        ans=-1

print(aw,ah)
print(bw,bh)
if ans == 0:
    for i in range(h):
        if ah[i] != bh[i]:
            print(ah[i],end=" ")
            print("TASU ")
            ans+=1
        else:
            continue
    print(ans)
    for i in range(w):
        if aw[i] != bw[i]:
            print(aw[i],end=" ")
            print("TASU ")
            ans+=1
        else:
            continue
    print()
    ans//=2
else:
    ans=-1
print(ans)