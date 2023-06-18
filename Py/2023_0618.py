t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    psort=sorted(p)
    ans=0
    for i in range(n):
        timedif=[]
        if psort == p:
            ans+=n
            break
        else: 
            if p[i] == i+1:
                ans+=1
            elif (i+1)-p[i] > 0:
                timedif+=[(i+1)-p[i]]
    else:
        maxdif=max(timedif)
        for i in timedif:
            if maxdif == i:
                ans+=1
    print(ans)