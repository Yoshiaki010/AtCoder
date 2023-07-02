t=int(input())
for i in range(t):
    plis=[]
    kill=0
    n=int(input())
    p=list(map(int,input().split()))
    for j in range(len(p)):
        rank=j+1
        plis.append([rank,p[j],True])


    for a in plis:
        for teki in plis:
            if a[0]<teki[0] and a[1]>teki[1]:
                kill+=1
                break
    ans=n-kill
    print(ans)