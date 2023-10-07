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
j=-1
for i in range(12):
    if i%4 == 0:
        print(i)
        j+=1
    p=list(input())
    for k in range(4):
        if p[k] == "#":
            mino[j].append(1)
        else:
            mino[j].append(0)
print(mino)
