#lv1
"""
ans=0
for i in range(12):
    s=input()
    if len(s) == i+1:
        ans+=1
    else:
        continue
print(ans)
"""
#lv2
"""
s=input()
keybord=[]
for i in range(26):
    keybord+=[[s[i],i]]

keybord.sort()

move=0
for i in range(25):
    front=keybord[i][1]
    next=keybord[i+1][1]
    move+=abs(front-next)
print(move)
"""
#lv3
"""
n=int(input())
a=list(map(int,input().split()))
amax=a[0]

b=list(map(int,input().split()))
bmax=b[0]

for i in range(n):
    if amax < a[i]:
        amax = a[i]
    else:
        pass
    if bmax < b[i]:
        bmax = b[i]
    else:
        pass

print(amax + bmax)
"""
#lv4
"""
"""

n,m=map(int,input().split())
dict={}
print(n,m)
for i in range(n):
    dict[i]=0
print(dict)
q=[]
for _ in range(m):
    u,v,w=map(int,input().split())
    q.append([u,v,w])
    dict[v-1]=w
print(dict)

"""
ans=[]
for i in range(n):
    ans+=[dict[i]]
print(*ans)
for i in range(m):
    u,v,w=q[i]
    diff=dict[v-1]-dict[u-1]-w
    print(dict[v-1]-dict[u-1],w,diff)
    if 0 < diff:
        dict[v-1]-=diff
    else:
        dict[v-1]+=diff
"""

dict[0]=0
dict[1]=-18169343
dict[2]=-307110901
dict[3]=-130955934
dict[4]=-307110901 - 385208968 + 770417936

ans=[]
for i in range(n):
    ans+=[dict[i]]
print("ans:",*ans)

for i in range(m):
    u,v,w=q[i]
    diff=dict[v-1]-dict[u-1]-w
    print(u,v)
    print(dict[v-1]-dict[u-1],w,diff)
