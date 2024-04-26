#lv1
"""
s=input()
t=int(s[3::])
ans="Unknow"
if 0 < t and t < 350 and t != 316:
  ans="Yes"
else:
    ans = "No"
print(ans)
"""
#lv2
"""
n,q=map(int,input().split())
t=list(map(int,input().split()))
status=[1]*n
ans=n
for i in range(q):
    if status[t[i]-1] == 1:
        ans-=1
        status[t[i]-1] = 0
    else:
        ans+=1
        status[t[i]-1] = 1
print(ans)
"""
#lv3
"""
n=int(input())
a=list(map(int,input().split()))
status=[]
for i in range(n):
    status.append([])

for i in range(n):
    status[a[i]-1].append(i)
k=0
eru=[]
for i in range(n-1):
    new=0
    if status[i][0] != i:
        #入れ替え履歴追加
        k+=1    
        eru.append([i+1,status[i][0]+1])
        #入れ替え
        new = a[i]
        a[i] = a[status[i][0]]
        a[status[i][0]] = new
        #ステータス更新
        status[new-1][0]=status[i][0]
        status[i][0] = i
    else:
        continue
print(k)
for i in range(k):
    print(eru[i][0],eru[i][1])
"""
#lv3別解
"""
"""
n=int(input())
a=list(map(int,input().split()))
status=[0]*n
k=0
for i in range(n-1):
    if a[i] == i+1:
        status[i] = 1
    else:
        k+=1
        