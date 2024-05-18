#lv1
"""
h=int(input())
ans=0
f=0
for i in range(30):
    f+=2**i
    if h < f:
        ans=i+1
        break
    else:
        continue
print(ans)
"""
#lv2
"""
n=int(input())
t=0
all=[]
for i in range(n):
    s,c=input().split()
    all.append(s)
    t+=int(c)
all.sort()
print(all[t%n])
"""
#lv3
"""
"""
n=int(input())
all=[]
m=0
for i in range(n):
    a,c=map(int,input().split())
    all.append([a,c,i])
    m+=1
all.sort(reverse=True)
ans=[all[0][2]]
for i in range(n-1):
    
print(ans)
print(m,all)
#lv4
"""
"""
