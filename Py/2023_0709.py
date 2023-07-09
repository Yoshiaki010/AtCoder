t=int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    ans="No"
    if n == k :
        ans="Yes"
    elif n%3 == 0:
        ans="Yes"
    elif n%3 != 0:
        amari = n%3
        m=k-amari
        if 3*m == n-amari:
            ans="Yes"
    print(ans)
