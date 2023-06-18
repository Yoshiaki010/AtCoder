t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    psort=sorted(p)
    ans=0
    for i in range(n):
        if psort == p:
            ans+=n
            break
        else :
            if p[i]-(i+1) <0:
                ans+=1
    print(ans)
