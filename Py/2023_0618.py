t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    psort=sorted(p)
    ans=0
    rank=[]
    for i in range(n):
        if psort == p:
            ans+=n
            break
        else:
            if p[i] < (i+1):
                rank+=[[p[i],i+1]]
                ans+=1
    
    rank.sort()
    for i in range(len(rank)-1):
        if rank[i][1] > rank[i+1][1]:
            ans-=1

    print(ans)