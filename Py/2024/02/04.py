t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    ans="No"
    if a <= n:
        if i == t-4:
            print(n*n//2+1)
        if a < n//2:
            if a%2 == 0:
                p= (n*n)//2-((n//2)*a)
            else:
                p= (n*n)//2-(((n//2)+1)*a)
        else:
            n-=a
            p= (n*n)//2+1
        if b <= p:
            ans="Yes"
    print(ans)