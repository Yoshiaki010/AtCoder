t=int(input())

for _ in range(t):
    ans="No"
    baisu=set()
    n=int(input())
    for i in range(n//2):
        i+=2
        if n % i == 0:
            baisu.add(i)
        else:
            continue
    print(baisu)
    a=[]
    for i in baisu:
        a.append(i)
        if sum(a) == n:
            if len(a) <= n:
                ans="Yes"
            else:
                print
                break
    else:
        ans="Yes"
    print(ans)
