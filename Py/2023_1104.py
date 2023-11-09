"""
#lv1
n=int(input())
s=input()
ans="Unknow" 
for i in range(n-1):
    if s[i] == "a" and  s[i+1] == "b":
        ans="Yes"
        break
    elif  s[i] == "b" and s[i+1] == "a":
        ans="Yes"
        break
    else:
        ans="No"
print(ans)
"""
#lv2
"""
b=int(input())
ans=-1
for i in range(16):
    i+=1
    num=i**i
    if b == num:
        ans=i
        break
print(ans)
"""
#lv3
a=[]
for i in range(9):
    a.append(list(map(int,input().split())))
ans="Unkown"

ansg=False
for i in range(9):
    gyou=set()
    for j in range(9):
        gyou.add(a[i][j])
    if len(gyou) < 9:
        break
else:
    ansg=True

ansr=False
for j in range(9):
    retu=set()
    for i in range(9): 
        retu.add(a[i][j])
    if len(retu) < 9:
        break
else:
    ansr=True

anss=False
sangyou=0
sanretu=0
for _ in range(9):
    sanmasu=set()
    for i in range(3):
        i+=sanretu
        for j in range(3):
            j+=sangyou
            sanmasu.add(a[i][j])
    if len(sanmasu) < 9:
        break
    sanretu+=3
    if sanretu == 9:
        sanretu=0
        sangyou+=3
    sanmasu=set()
else:
    anss=True

if ansg and ansr and anss:
    ans="Yes"
else:
    ans="No"
print(ans)
