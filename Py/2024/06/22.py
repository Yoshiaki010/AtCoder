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
ans=abs(sx-tx)+(abs(sy-ty))//2
print(ans)