#A lv1
"""
n=int(input())
ans=0
for _ in range(n):
    s=input()
    if s == "Takahashi":
        ans+=1
    else:
        continue
print(ans)
"""
#B lv2
"""
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    for j in range((n*2)-2):
        if i+1 == a[j]:
            if a[j] == a[j+2]:
                ans+=1
            break
        else:
            continue
print(ans)
"""
#C lv3
"""
"""
sx,sy=map(int,input().split())
tx,ty=map(int,input().split())
ans=abs(sy-ty)
now=[]

print(ans)

if sx%2 == 0:
    now+=[sx,sx+1]
else:
    now+=[sx-1,sx]

print(sx,sy)
print(tx,ty)
print(now)
print(now[0]-ans,now[1]+ans+1)

if tx < now[0]-ans:
    print("tx<")
    ans+=(abs(tx-(now[0]+1)))//2
elif now[1]+ans < tx:
    print("<tx")
    ans+=(abs(tx-(now[1]-1)))//2
else:
    print("<tx<")
    ans+=0
print(ans)
