"""
#lv1
n=int(input())
s=[]
a=[]
prionof="OFF"
for i in range(n):
    for j in [input().split()]:
        s+=[j]
        a+=[int(j[1])]

small=min(a)

for i in s:
    if prionof=="OFF":
        if i[1]==str(small):
            prionof="ON"
        else:
            s+=[i]
    if prionof=="ON":
        print(i[0])
"""
"""
#lv2
lisn=list(input())
n=int("".join(lisn))
if len(lisn)<=3:
    print(n)
elif len(lisn)<=4:
    n-=int("".join(lisn[-1]))
    print(n)
elif len(lisn)<=5:
    n-=int("".join(lisn[3::]))
    print(n)
elif len(lisn)<=6:
    n-=int("".join(lisn[3::]))
    print(n)
elif len(lisn)<=7:
    n-=int("".join(lisn[3::]))
    print(n)
elif len(lisn)<=8:
    n-=int("".join(lisn[3::]))
    print(n)
elif len(lisn)<=9:
    n-=int("".join(lisn[3::]))
    print(n)
"""
#lv3
import math
n,d=map(int,input().split())
human=[]
kansen=[0]
for i in range(n):
    human+=[list(map(int,input().split()))]
print(human)
print(n,d)
print("Yes")

for j in kansen:
    print(j)
    for i in range(n):
        x=i+1
        a=(human[j][0]-human[i][0])*(human[j][0]-human[i][0])
        b=(human[j][1]-human[i][1])*(human[j][1]-human[i][1])
        r=math.sqrt((a+b))
        print(r)
        if d>=r:
            print("Yes")
            kansen+=[i]
        else:
            print("No")
