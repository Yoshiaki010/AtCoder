#lv1
"""
a=sum(map(int,input().split()))
b=sum(map(int,input().split()))
ans=a-b
ans+=1
print(ans)
"""
#lv2
"""
n=int(input())
a=[]
b=[]
ans=[-1,-1]
for i in range(n):
    a.append(list(input()))
for i in range(n):
    b.append(list(input()))
for i in range(n):
    for j in range(n):
        if a[i][j] != b[i][j]:
            ans=[i,j]
            break
        else:
            continue
    else:
        continue
    break
print(ans[0]+1,ans[1]+1)
"""
#lv3
"""
n=int(input())
a=list(map(int,input().split()))
now=[]
ans=0
for i in range(n):
    now.append(a[i])
    ans+=1
    while 1 < ans:
        if now[-1] == now[-2]:
            new=now[-1]+1
            now.pop(-1)
            now.pop(-1)
            now.append(new)
            ans-=1
        else:
            break
print(ans)
"""
#lv4
h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))
print(s)

now=[]
c=0
#再帰呼び出し、動的計画法
def walk(i,j,d):
    if s[i][j-1] == "." and s[i][j+1] == "." and s[i-1][j] == "." and s[i+1][j] == ".":
        d+=1
    else:
        pass
    return(d)

for i in range(h):
    for j in range(w):
        if s[i][j] != "#":
