#lv1
"""
s=input()
print(s.replace(".",""))
"""
#lv2
"""
m = int(input())
a = []
n = 0
for _ in range(20):
    if m % 3 == 0:
        for i in range(10):
            ai = 10 - i
            if m < 3 ** ai:
                continue
            else:
                n+= 1
                m-= 3 ** ai
                a+= [ai]
                break
    else:
        n += 1
        m -= 1
        a += [0]
    if 0 < m:
        continue
    else:
        break
print(n)
print(*a)
"""
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
            break
        else:
            continue
    
    s[int(x)-1]=c

    for i in range(3):
        i+=int(x)-3
        if "".join(s[i:i+3]) == "ABC":
            all+=1
            break
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
