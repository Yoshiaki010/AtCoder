#lv1 
"""
l,r=map(int,input().split())
ans="Unknow"
if l+r == 1:
    if l == 1:
        ans="Yes"
    else:
        ans="No"
else:
    ans="Invalid"
print(ans)
"""

#lv2
"""
n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

i=0
for j in range(n):
    if j-1 < i:
        i=a[i][j]-1
    else:
        i=a[j][i]-1
print(i+1)
"""

#lv3
"""
s=list(input())
t=list(input())
n=len(s)
wrong=0
wrong_place=[]
for i in range(n):
    if s[i] == t[i]:
        continue
    else:
        wrong+=1
        wrong_place.append(i)
print(wrong)
for _ in range(wrong):
    now=wrong_place[0]
    wrong_place=wrong_place[1:]
    snum=ord(s[now])
    tnum=ord(t[now])
    if snum < tnum:
        wrong_place.append(now)
    else:
        s[now] = t[now]
        wrong-=1
        print("".join(s))
wrong_place.sort(reverse=True)
for _ in range(wrong):
    now=wrong_place[0]
    wrong_place=wrong_place[1:]
    wrong-=1
    s[now] = t[now]
    print("".join(s))
"""
#lv4　爆弾のある位置から上下左右に見た時、最初に見えた壁を破壊。ただし、端の壁は対象外
