#lv1
"""
s=input()
rice=0
miso=0
for i in range(3):
    if s[i] == "R":
        rice=i
    elif s[i] == "M":
        miso=i
    else:
        continue
if rice < miso:
    ans="Yes"
else:
    ans="No"
print(ans)
"""
#lv2
"""
s,t=input().split()
ns=len(s)-1
ans="Unkow"
for w in range(ns-1):
    w+=1
    for c in range(w):
        if c <= w:
            if s[c::w] == t:
                ans="Yes"
                break
            else:
                continue
    else:
        continue
    break
else:
    ans="No"
print(ans)

"""
#lv3
"""
n=int(input())
a=list(map(int,input().split()))
w=list(map(int,input().split()))
all=[]
for i in range(n):
    all.append([a[i],w[i]])
all.sort()
ans=0
for i in range(n-1):
    if all[i][0] == all[i+1][0]:
        ans+=all[i][1]
    else:
        continue
print(ans)
"""
#lv4
"""
"""
