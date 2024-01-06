#lv1
"""
s=input()
print(s[0:len(s)-1]+"4")
"""

#lv2
"""
n=int(input())
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if x+y+z <= n:
                print(x,y,z)
"""

#lv3
n,p=map(int,input().split())
d=[]
x=1
y=0
m=0
for i in range(p):
    q=input().split()
    if q[0] == "1":
        m+=1
        c=q[1]
        if c=="R":
            x+=1
        elif c=="L":
            x-=1
        elif c=="U":
            y+=1
        elif c=="D":
            y-=1
        d+=[[x,y]]
        if n < len(d):
            newd=d[1::]
            d=newd
            #d.pop(0)
    else:
        p=int(q[1])
        if p <= m:
            lend=len(d)
            print(d[lend-p][0],d[lend-p][1])
        else:
            print(p-m,0)
"""
"""
