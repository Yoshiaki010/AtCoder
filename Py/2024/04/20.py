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
n=int(input())
a=list(map(int,input().split()))
k=0
eru=[]
status=[]
for i in range(n-1):
    status.append(i)
print(status)
i=0
for _ in range(n-1):
    if status[0]+1 == a[i]:
        status.pop(i)
    else:
        if a[i] != i+1:
            j=a[i]-1
            if a[j] == i+1:
                status.pop(i)
            else:
                pass
            k+=1
            status.pop(j)
            #入れ替え
            eru.append([i+1,a[i]])
            new=a[j]
            a[j] = a[i]
            a[i] = new
        else:
            status.pop(i)
            continue
    print(status)
print(k)
for i in range(k):
    print(eru[i][0],eru[i][1])