#lv1
"""
s=input()
print(s.replace(".",""))
"""
#lv2
"""
"""
m=int(input())
n=0
a=[]
f=0
for _ in range(20):
    f+=1
    if 0 < m % 3:
        n+=1
        a.append(0)
        m-=1
    else:
        for i in range(9):
            if 3**(9-i) < m+1:
                n+=1
                a.append(9-i)
                m-=3**(9-i)
                break
            else:
                continue
    if m < 1:
        break
    else:
        continue
print(n)
for i in range(n):
    print(a[i],end=" ")
#lv3
"""
n,q=map(int,input().split())
s=list(input())
all=0
for i in range(n-2):
    if "".join(s[i:i+3]) == "ABC":
        all+=1
    else:
        continue

for i in range(q):
    x,c=input().split()
    for i in range(3):
        i+=int(x)-3
        if "".join(s[i:i+3]) == "ABC":
            all-=1
        else:
            continue
    
    s[int(x)-1]=c

    for i in range(3):
        i+=int(x)-3
        if "".join(s[i:i+3]) == "ABC":
            all+=1
        else:
            continue
    print(all)
"""

#lv4
"""
n=int(input())
h=list(map(int,input().split()))
print(h)

maxh=[]
max=h[1]
for i in range(n-1):
    if max < h[i+1]:
        max=h[i+1]
    else:
        pass
    maxh.append(max)
print(maxh)

f=0
for i in range(n):
    maxh[n-i]
    f+=1
print(f)
"""
