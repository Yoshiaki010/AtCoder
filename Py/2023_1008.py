t=int(input())
for _ in range(t):
    ans="No"
    n,x,y=input().split()
    lisx=list(x)
    lisy=list(y)
    x=[]
    for i in range(int(n)):
        i+=1
        if lisx[-i] != lisy[-i]:
            if lisx[-i] == "B" and lisy[-i] == "A":
                if int(n) -i != 0:
                    if lisx[-i-1] != "C" and lisy[-i-1] != "B":
                        break
    else:
        ans="Yes"
    print(ans)